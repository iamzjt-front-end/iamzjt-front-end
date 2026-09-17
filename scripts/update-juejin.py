"""Render a linked profile badge from the public follower count, keeping the last good result on failure."""

import base64
import json
from datetime import datetime, timezone
from pathlib import Path
import shutil
import subprocess
import sys


USER_ID = "958429872532632"
FILES = ("juejin-profile.svg", "juejin-profile.json")


def render(count, updated_at):
    number = f"{count:,}"
    width = max(180, 124 + len(number) * 8)
    mark = Path(__file__).resolve().parent.parent / "assets/juejin-mark.svg"
    logo = base64.b64encode(mark.read_bytes()).decode()
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="28" viewBox="0 0 {width} 28" role="img" aria-labelledby="title desc">
  <title id="title">掘金主页 · {number} 粉丝 ↗</title>
  <desc id="desc">Public follower count updated at {updated_at}. Click to visit J.Tide on Juejin.</desc>
  <rect width="{width}" height="28" rx="5" fill="#080b0f"/>
  <image x="9" y="6" width="16" height="16" href="data:image/svg+xml;base64,{logo}"/>
  <g font-family="-apple-system,BlinkMacSystemFont,'Segoe UI',Arial,sans-serif">
    <text x="33" y="19" fill="#f0f6fc" font-size="12">掘金</text>
    <path d="M70 7V21" stroke="#303c43"/>
    <text x="83" y="19" fill="#9fc8b4" font-size="12">{number} 粉丝</text>
    <text x="{width - 22}" y="19" fill="#f0f6fc" font-size="15">↗</text>
  </g>
</svg>
'''


def main():
    output, previous = map(Path, sys.argv[1:])
    output.mkdir(parents=True, exist_ok=True)
    try:
        raw = subprocess.check_output([
            "curl", "--fail", "--silent", "--show-error", "--location",
            "--retry", "2", "--retry-max-time", "30", "--max-time", "10",
            f"https://api.juejin.cn/user_api/v1/user/get?user_id={USER_ID}",
        ])
        response = json.loads(raw)
        data = response.get("data") or {}
        count = data.get("follower_count")
        if response.get("err_no") != 0 or type(count) is not int or count < 0:
            raise ValueError("Juejin did not return a valid follower count")
        if str(data.get("user_id")) != USER_ID:
            raise ValueError("Juejin returned a different user")
    except (subprocess.CalledProcessError, ValueError, TypeError) as error:
        if not all((previous / name).is_file() for name in FILES):
            raise RuntimeError("No previous Juejin badge is available") from error
        metadata = json.loads((previous / FILES[1]).read_text())
        if metadata.get("userId") != USER_ID or type(metadata.get("followers")) is not int:
            raise ValueError("The previous Juejin badge has invalid metadata") from error
        for name in FILES:
            shutil.copyfile(previous / name, output / name)
        print(f"Keeping the previous Juejin badge: {error}", file=sys.stderr)
        return

    updated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (output / FILES[0]).write_text(render(count, updated_at))
    metadata = {"userId": USER_ID, "followers": count, "updatedAt": updated_at}
    (output / FILES[1]).write_text(json.dumps(metadata, indent=2) + "\n")
    print(json.dumps(metadata))


if __name__ == "__main__":
    main()
