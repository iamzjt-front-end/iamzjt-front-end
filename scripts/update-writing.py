#!/usr/bin/env python3
"""Refresh only the marked Writing block from public Juejin data.

No cookies or API keys are required. Temporary Juejin API outages leave the
README untouched and finish with a warning so the profile workflow stays
healthy; the next scheduled run retries. Incomplete or invalid data still
fails loudly before any file is written.
"""

import argparse
from html import escape
import json
from pathlib import Path
import re
import time
from urllib.request import Request, urlopen

USER_ID = "958429872532632"
API = "https://api.juejin.cn"
START = "<!-- writing:start -->"
END = "<!-- writing:end -->"
REQUEST_ATTEMPTS = 5


class JuejinUnavailable(RuntimeError):
    """The public Juejin API could not provide a usable response after retries."""


def request(path, payload=None):
    for attempt in range(REQUEST_ATTEMPTS):
        try:
            req = Request(
                API + path,
                data=json.dumps(payload).encode() if payload is not None else None,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Origin": "https://juejin.cn",
                    "Referer": "https://juejin.cn/",
                    "User-Agent": "j-tide-profile/1.0",
                },
            )
            with urlopen(req, timeout=25) as response:
                result = json.load(response)
            if not isinstance(result, dict):
                raise JuejinUnavailable("Juejin returned a non-object response")
            if result.get("err_no") != 0 or result.get("data") is None:
                code = result.get("err_no", "unknown")
                message = str(result.get("err_msg", "no message")).strip()
                raise JuejinUnavailable(f"Juejin returned err_no={code}: {message}")
            return result
        except (OSError, ValueError, JuejinUnavailable) as error:
            if attempt == REQUEST_ATTEMPTS - 1:
                raise JuejinUnavailable(
                    f"Juejin request failed after {REQUEST_ATTEMPTS} attempts: {error}"
                ) from error
            time.sleep(2 ** attempt)


def paginated(path, extra):
    items, seen = [], set()
    cursor = "0"
    for _ in range(100):
        if cursor in seen:
            raise ValueError("Juejin pagination repeated a cursor")
        seen.add(cursor)
        page = request(path, {"user_id": USER_ID, "cursor": cursor, "limit": 20, **extra})
        if not isinstance(page["data"], list) or not isinstance(page.get("has_more"), bool):
            raise ValueError("Incomplete Juejin list response")
        items.extend(page["data"])
        if not page["has_more"]:
            if len(items) < number(page["count"]):
                raise ValueError("Juejin returned a partial list")
            return items
        if not page["data"] or not page.get("cursor"):
            raise ValueError("Incomplete Juejin pagination")
        cursor = str(page["cursor"])
    raise ValueError("Juejin pagination exceeded the safety limit")


def number(value):
    if isinstance(value, bool) or not re.fullmatch(r"\d+", str(value)):
        raise ValueError("Invalid Juejin number")
    return int(value)


def link(kind, identifier, title):
    identifier = str(identifier)
    if not re.fullmatch(r"\d+", identifier) or not isinstance(title, str) or not title.strip():
        raise ValueError("Invalid Juejin link")
    # HTML text avoids Markdown titles injecting links, tags, or marker comments.
    title = escape(" ".join(title.split()))
    return f'<a href="https://juejin.cn/{kind}/{identifier}">{title}</a>'


def metric(label, value):
    return f"{label} {number(value):,}"


def render(user, articles, columns):
    if str(user["user_id"]) != USER_ID:
        raise ValueError("Unexpected Juejin user")
    count = number(user["post_article_count"])
    views = number(user["got_view_count"])
    article_by_id = {str(item["article_id"]): item["article_info"] for item in articles}
    if count > len(article_by_id):
        raise ValueError("Article list is incomplete; keep the previous Writing block")
    for article in article_by_id.values():
        if str(article["user_id"]) != USER_ID:
            raise ValueError("Unexpected article author")
        number(article["ctime"])
        number(article["view_count"])
        number(article["digg_count"])
        link("post", article["article_id"], article["title"])
    unique_columns = {}
    for item in columns:
        column, version = item["column"], item["column_version"]
        if str(column["user_id"]) != USER_ID:
            raise ValueError("Unexpected column author")
        number(column["article_cnt"])
        number(column["ctime"])
        link("column", column["column_id"], version["title"])
        unique_columns[str(column["column_id"])] = item

    latest_articles = sorted(article_by_id.values(), key=lambda a: number(a["ctime"]), reverse=True)[:3]
    popular_articles = sorted(article_by_id.values(), key=lambda a: (
        number(a["view_count"]), number(a["ctime"]), str(a["article_id"])
    ), reverse=True)[:3]
    latest_columns = sorted(unique_columns.values(), key=lambda c: number(c["column"]["ctime"]), reverse=True)[:3]
    lines = [f"在掘金写作 · **{count} 篇文章** · **{views:,} 次阅读**", ""]
    if latest_columns:
        lines += [f"**最新专栏** · [全部专栏 ↗](https://juejin.cn/user/{USER_ID}/columns)", ""]
        for item in latest_columns:
            column, version = item["column"], item["column_version"]
            total = number(column["article_cnt"])
            ids = set(str(i) for i in column["content_sort_ids"])
            if len(ids) != total or not ids.issubset(article_by_id):
                raise ValueError("Column membership is incomplete; cannot calculate cumulative reads")
            column_views = sum(number(article_by_id[i]["view_count"]) for i in ids)
            source = (' · <a href="https://github.com/j-tide/zjt-mini-vue3">配套源码 ↗</a>'
                      if str(column["column_id"]) == "7168612212133593095" else "")
            lines.append(f'- {link("column", column["column_id"], version["title"])}'
                         f' · {total} 篇 · {metric("文章累计阅读", column_views)}{source}')
        lines.append("")
    for heading, selection in [("最新文章", latest_articles), ("热门文章 · 阅读量 Top 3", popular_articles)]:
        if not selection:
            continue
        more = f" · [全部文章 ↗](https://juejin.cn/user/{USER_ID}/posts?sort=newest)" if selection is latest_articles else ""
        lines += [f"**{heading}**{more}", ""]
        for article in selection:
            lines.append(f'- {link("post", article["article_id"], article["title"])}'
                         f' · {metric("阅读", article["view_count"])}'
                         f' · {metric("点赞", article["digg_count"])}')
        lines.append("")
    return "\n".join(lines).rstrip()


def replace_block(readme, block):
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must have exactly one Writing marker pair")
    before, rest = readme.split(START)
    _, after = rest.split(END)  # Also rejects an end marker preceding the start.
    return before + START + "\n" + block + "\n" + END + after


def update(path):
    original = path.read_text(encoding="utf-8")
    replace_block(original, "")  # Fail before fetching if the template is invalid.
    user = request(f"/user_api/v1/user/get?user_id={USER_ID}")["data"]
    articles = paginated("/content_api/v1/article/query_list", {"sort_type": 2})
    columns = paginated("/content_api/v1/column/self_center_list", {})
    updated = replace_block(original, render(user, articles, columns))
    if updated == original:
        print("Writing is already up to date.")
        return
    # No file writes until every response and the complete replacement validate.
    path.write_text(updated, encoding="utf-8")
    print(f"Updated Writing: {len(articles)} articles, {len(columns)} columns.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    try:
        update(parser.parse_args(argv).readme)
    except JuejinUnavailable as error:
        print(f"::warning::Skipped Juejin writing sync: {error}")
        print("Juejin is temporarily unavailable; the existing Writing block was kept.")


if __name__ == "__main__":
    main()
