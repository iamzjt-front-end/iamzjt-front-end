#!/usr/bin/env python3
"""Refresh only the marked Writing block from public Juejin data.

No cookies or API keys are required. A failed/incomplete response leaves the
README untouched and fails the job visibly; the next scheduled run retries.
"""

import argparse
from datetime import datetime
from html import escape
import json
from pathlib import Path
import re
import time
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo

USER_ID = "958429872532632"
API = "https://api.juejin.cn"
START = "<!-- writing:start -->"
END = "<!-- writing:end -->"


def request(path, payload=None):
    for attempt in range(3):
        try:
            req = Request(
                API + path,
                data=json.dumps(payload).encode() if payload is not None else None,
                headers={"Content-Type": "application/json", "User-Agent": "j-tide-profile/1.0"},
            )
            with urlopen(req, timeout=25) as response:
                result = json.load(response)
            if result.get("err_no") != 0 or result.get("data") is None:
                raise ValueError("Juejin returned an unsuccessful response")
            return result
        except (OSError, ValueError):
            if attempt == 2:
                raise
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
    latest_columns = sorted(unique_columns.values(), key=lambda c: number(c["column"]["ctime"]), reverse=True)[:3]
    lines = [f"在掘金记录技术实践：**{count} 篇文章** · **{views:,} 次阅读**。", ""]
    if latest_columns:
        lines += ["**最新专栏**", ""]
        for item in latest_columns:
            column, version = item["column"], item["column_version"]
            total = number(column["article_cnt"])
            label = f"{total} 篇" if total else "新建专栏"
            lines.append(f'- {link("column", column["column_id"], version["title"])} · {label}')
        lines.append("")
    if latest_articles:
        lines += ["**最近文章**", ""]
        for article in latest_articles:
            date = datetime.fromtimestamp(number(article["ctime"]), ZoneInfo("Asia/Shanghai")).strftime("%Y-%m-%d")
            lines.append(f'- {date} · {link("post", article["article_id"], article["title"])}')
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    update(parser.parse_args().readme)
