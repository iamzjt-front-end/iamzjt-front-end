"""Render the profile's linked project cards; fetch real star counts on each run.

Usage: python3 scripts/generate-project-cards.py [output-directory]
Icons: Primer Octicons (MIT), see icons/LICENSE. No runtime dependencies.
"""
import json
import os
from pathlib import Path
import sys
from urllib.request import Request, urlopen
from xml.sax.saxutils import escape
import xml.etree.ElementTree as ET

PROJECTS = [
    ("git-workflow", "AI 提交与代码审查，让 Git 工作流更顺畅。", ["AI 提交与代码审查，", "让 Git 工作流更顺畅。"], "TypeScript · CLI"),
    ("codex-bar", "在菜单栏掌握 Codex 任务、额度与用量。", ["在菜单栏掌握 Codex", "任务、额度与用量。"], "Swift · macOS"),
    ("llmops", "LLM 应用与工具插件平台，持续构建中。", ["LLM 应用与工具插件平台，", "持续构建中。"], "Python · LLM"),
    ("code-review-mpx", "面向 Mpx 小程序的代码审查 Skill。", ["面向 Mpx 小程序的", "代码审查 Skill。"], "Agent Skill"),
    ("fund-pulse", "在菜单栏查看基金持仓、估值与收益。", ["在菜单栏查看基金持仓、", "估值与收益。"], "Swift · macOS"),
    ("Tide", "本地番茄钟与专注统计，记录工作节奏。", ["本地番茄钟与专注统计，", "记录工作节奏。"], "Swift · macOS"),
]


def icon(name, x, y, color, size=16):
    root = ET.parse(Path(__file__).parent / "icons" / f"{name}-16.svg").getroot()
    paths = "".join(f'<path d="{p.attrib["d"]}"/>' for p in root)
    return f'<g transform="translate({x} {y}) scale({size / 16})" fill="{color}">{paths}</g>'


def card(name, description, mobile_lines, meta, stars, mobile=False, column=0):
    width, height = (308, 160) if mobile else (410, 146)
    # Only the inner edge has a gutter; both outer edges align with the cover.
    left_gutter = 8 if not mobile and column == 1 else 0
    right_gutter = 8 if not mobile and column == 0 else 0
    right, padding = width - right_gutter - 21, left_gutter + 21
    title_size, body_size = (20, 14) if mobile else (23, 16)
    footer = height - 33
    lines = mobile_lines if mobile else [description]
    body = "".join(f'<text x="{padding}" y="{69 + i * 21}" font-size="{body_size}" fill="#C5D3E0">{escape(line)}</text>' for i, line in enumerate(lines))
    count = str(stars)
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title description">
<title id="title">{escape(name)}</title>
<desc id="description">{escape(description)} {escape(meta)}. {stars} GitHub stars.</desc>
<rect x="{left_gutter + 0.5}" y="0.5" width="{width - left_gutter - right_gutter - 1}" height="{height - 11}" rx="8" fill="#151E25" stroke="#354856"/>
<g font-family="-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, PingFang SC, Microsoft YaHei, sans-serif">
<text x="{padding}" y="38" font-size="{title_size}" font-weight="650" letter-spacing="-0.5" fill="#F2F5F7">{escape(name)}</text>
{icon("arrow-up-right", right - 15, 19, "#9FB6CB", 19)}
{body}
<circle cx="{padding + 4}" cy="{footer - 4}" r="4" fill="#439CF6"/>
<text x="{padding + 21}" y="{footer}" font-size="12" font-family="SF Mono, Menlo, Consolas, monospace" fill="#ADC5DC">{escape(meta)}</text>
{icon("star", right - len(count) * 8 - 22, footer - 13, "#EBCB82", 16)}
<text x="{right}" y="{footer}" text-anchor="end" font-size="14" fill="#EBCB82">{count}</text>
</g>
</svg>'''
    ET.fromstring(svg)
    return svg


def main():
    owner = os.environ.get("GITHUB_USERNAME", "j-tide")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "profile-project-cards", "X-GitHub-Api-Version": "2022-11-28"}
    if os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = "Bearer " + os.environ["GITHUB_TOKEN"]
    rendered, counts = {}, {}
    # Fetch everything before writing: an API failure must not publish fake zeros.
    for index, (name, description, mobile_lines, meta) in enumerate(PROJECTS):
        req = Request(f"https://api.github.com/repos/{owner}/{name}", headers=headers)
        with urlopen(req, timeout=30) as response:
            repo = json.load(response)
        stars = repo["stargazers_count"]
        if type(stars) is not int or stars < 0:
            raise ValueError(f"Invalid star count for {name}")
        counts[name] = stars
        for mobile in (False, True):
            filename = f'{name}{"-mobile" if mobile else ""}.svg'
            rendered[filename] = card(name, description, mobile_lines, meta, stars, mobile, index % 2)
    output = Path(sys.argv[1] if len(sys.argv) > 1 else "dist/project-cards")
    output.mkdir(parents=True, exist_ok=True)
    for filename, svg in rendered.items():
        (output / filename).write_text(svg, encoding="utf-8")
    (output / "stars.json").write_text(json.dumps(counts, indent=2) + "\n", encoding="utf-8")
    print(f"Generated {len(rendered)} cards: {json.dumps(counts)}")


if __name__ == "__main__":
    main()
