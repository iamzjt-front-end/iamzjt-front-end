"""Place the generated animation inside a dark, padded SVG card."""

import sys
from pathlib import Path
import xml.etree.ElementTree as ET


def main():
    source_path, output_path = map(Path, sys.argv[1:])
    snake = ET.parse(source_path).getroot()
    namespace = "http://www.w3.org/2000/svg"
    ET.register_namespace("", namespace)

    if snake.tag != f"{{{namespace}}}svg":
        raise ValueError("Expected a generated SVG animation")

    width = float(snake.attrib["width"])
    height = float(snake.attrib["height"])
    canvas_width, canvas_height = width + 80, height + 80
    tag = lambda name: f"{{{namespace}}}{name}"
    card = ET.Element(tag("svg"), {
        "width": f"{canvas_width:g}",
        "height": f"{canvas_height:g}",
        "viewBox": f"0 0 {canvas_width:g} {canvas_height:g}",
        "role": "img",
    })
    ET.SubElement(card, tag("title")).text = "GitHub contribution snake"
    ET.SubElement(card, tag("rect"), {
        "width": "100%", "height": "100%", "rx": "10", "fill": "#080b0f",
    })
    ET.SubElement(card, tag("rect"), {
        "x": "20", "y": "20", "width": f"{width + 40:g}",
        "height": f"{height + 40:g}", "rx": "5", "fill": "#0d1117",
    })
    snake.set("x", "40")
    snake.set("y", "40")
    card.append(snake)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(card).write(output_path, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    main()
