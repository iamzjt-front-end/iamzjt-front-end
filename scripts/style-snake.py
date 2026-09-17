"""Frame the rolling 90-day animation with its actual dates and contribution totals."""

import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET


def main():
    source_path, metadata_path, output_path = map(Path, sys.argv[1:])
    metadata = json.loads(metadata_path.read_text())
    if metadata["days"] != 90:
        raise ValueError("The recent contribution card requires 90 calendar days")
    snake = ET.parse(source_path).getroot()
    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)

    if snake.tag != f"{{{namespace}}}svg":
        raise ValueError("Expected a generated SVG animation")

    width = float(snake.attrib["width"])
    height = float(snake.attrib["height"])
    tag = lambda name: f"{{{namespace}}}{name}"
    card = ET.Element(tag("svg"), {
        "width": "960", "height": "320", "viewBox": "0 0 960 320",
        "role": "img", "aria-labelledby": "title description",
    })
    ET.SubElement(card, tag("title"), {"id": "title"}).text = "J.Tide 最近 90 天的 GitHub 贡献"
    ET.SubElement(card, tag("desc"), {"id": "description"}).text = (
        f"{metadata['start']} 至 {metadata['end']}，{metadata['contributions']} 次贡献，"
        f"{metadata['activeDays']} 个活跃日。按真实贡献日期生成，每日更新。"
    )
    ET.SubElement(card, tag("rect"), {
        "width": "960", "height": "320", "rx": "14", "fill": "#080b0f",
    })
    ET.SubElement(card, tag("rect"), {
        "x": "420", "y": "20", "width": "520", "height": "280",
        "rx": "9", "fill": "#0d1117",
    })
    text_group = ET.SubElement(card, tag("g"), {
        "font-family": "-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif",
    })

    def text(x, y, value, size, color, weight="400", **extra):
        element = ET.SubElement(text_group, tag("text"), {
            "x": str(x), "y": str(y), "font-size": str(size),
            "fill": color, "font-weight": weight, **extra,
        })
        element.text = value
        return element

    text(40, 56, "J.TIDE / GITHUB", 12, "#7c8b9a", "600", **{"letter-spacing": "2"})
    text(40, 105, "最近 90 天", 28, "#edf3f8", "600")
    count = text(40, 184, str(metadata["contributions"]), 64, "#f0f6fc", "600")
    ET.SubElement(count, tag("tspan"), {
        "dx": "12", "font-size": "15", "fill": "#99a8b6", "font-weight": "400",
    }).text = "次贡献"
    text(41, 222, f"{metadata['activeDays']} 个活跃日", 16, "#9fc8b4")
    text(41, 280, f"{metadata['start'].replace('-', '.')} — {metadata['end'].replace('-', '.')}", 12, "#748392")

    scale = min(480 / width, 240 / height)
    snake.set("x", f"{420 + (520 - width * scale) / 2:g}")
    snake.set("y", f"{20 + (280 - height * scale) / 2:g}")
    snake.set("width", f"{width * scale:g}")
    snake.set("height", f"{height * scale:g}")
    card.append(snake)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(card).write(output_path, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
