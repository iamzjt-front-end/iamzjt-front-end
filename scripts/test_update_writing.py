import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("writing", Path(__file__).with_name("update-writing.py"))
writing = importlib.util.module_from_spec(spec)
spec.loader.exec_module(writing)


def article(identifier, timestamp, title="Article"):
    return {"article_id": identifier, "article_info": {
        "article_id": identifier, "user_id": writing.USER_ID,
        "ctime": timestamp, "title": title,
    }}


class WritingTests(unittest.TestCase):
    def test_latest_not_api_or_pinned_order_and_safe_titles(self):
        articles = [article(str(i), 1700000000 + i) for i in [1, 4, 2, 3]]
        articles[1]["article_info"]["title"] = '<script> & [x](bad)\nnext'
        user = {"user_id": writing.USER_ID, "post_article_count": 4, "got_view_count": 12345}
        columns = [{"column": {"column_id": str(i), "user_id": writing.USER_ID,
                    "ctime": i, "article_cnt": 0}, "column_version": {"title": f"Series {i}"}}
                   for i in [1, 4, 2, 3]]
        result = writing.render(user, articles, columns)
        self.assertLess(result.index('/post/4'), result.index('/post/3'))
        self.assertNotIn('/post/1', result)
        self.assertLess(result.index('/column/4'), result.index('/column/3'))
        self.assertNotIn('/column/1', result)
        self.assertIn('新建专栏', result)
        self.assertIn('12,345 次阅读', result)
        self.assertIn('&lt;script&gt; &amp;', result)
        self.assertNotIn('<script>', result)

    def test_only_marked_region_changes_and_is_idempotent(self):
        original = f"Hero\n{writing.START}\nold\n{writing.END}\nProjects"
        updated = writing.replace_block(original, "new")
        self.assertEqual(updated, original.replace("old", "new"))
        self.assertEqual(writing.replace_block(updated, "new"), updated)
        for invalid in ["no markers", original + writing.START, writing.END + writing.START]:
            with self.assertRaises(ValueError):
                writing.replace_block(invalid, "new")

    def test_failed_fetch_does_not_touch_readme(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            original = f"before\n{writing.START}\nlast good data\n{writing.END}\nafter"
            path.write_text(original)
            user = {"user_id": writing.USER_ID, "post_article_count": 1, "got_view_count": 10}
            with patch.object(writing, "request", return_value={"data": user}), \
                 patch.object(writing, "paginated", side_effect=[[article("1", 1)], OSError("API down")]):
                with self.assertRaises(OSError):
                    writing.update(path)
            self.assertEqual(path.read_text(), original)

    def test_incomplete_list_rejected(self):
        user = {"user_id": writing.USER_ID, "post_article_count": 3, "got_view_count": 10}
        with self.assertRaises(ValueError):
            writing.render(user, [article("1", 1)], [])
        with patch.object(writing, "request", return_value={"data": [], "count": 2, "has_more": False}):
            with self.assertRaises(ValueError):
                writing.paginated("/list", {})

    def test_pagination_follows_cursor_and_rejects_loop(self):
        pages = [{"data": [1], "cursor": "next", "has_more": True},
                 {"data": [2], "count": 2, "has_more": False}]
        with patch.object(writing, "request", side_effect=pages) as request:
            self.assertEqual(writing.paginated("/list", {}), [1, 2])
            self.assertEqual(request.call_args_list[1].args[1]["cursor"], "next")
        with patch.object(writing, "request", return_value={"data": [1], "cursor": "0", "has_more": True}):
            with self.assertRaises(ValueError):
                writing.paginated("/list", {})


if __name__ == "__main__":
    unittest.main()
