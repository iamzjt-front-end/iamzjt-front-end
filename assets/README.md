# Profile assets

The current header uses `profile-header.svg` at 1600 x 176 and `profile-header-mobile.svg` at 800 x 196 below 600 pixels. Both have a 24-pixel corner radius, use the contribution card's `#080b0f` background and `#9fc8b4` accent, and render text with system fonts. Seven low-contrast tidal contour lines decorate the right side. The desktop name and role share one line; the mobile layout stacks them for readability. Earlier banner and intro assets are retained as design references.

## Technology badges

The local SVG badges in `stack/` are generated with Shields.io's `flat-square` style and displayed at a 24-pixel height, matching the original profile's compact rectangular badges. TypeScript, Node.js, and Git recover their original color backgrounds and white marks; Vue.js, React, and Vite recover their original dark backgrounds and colored marks. Added AI tools use the same combination of brand-color backgrounds or dark backgrounds with colored marks. Labels remain white throughout.

Icon geometry comes from Simple Icons (originally obtained through Shields.io); the OpenAI mark comes from Simple Icons v13, and the Weaviate mark comes from the logo published on its official site. Tool Calling and Embeddings are unbranded capability labels and use a neutral gray.

Palette reference: [Simple Icons data](https://github.com/simple-icons/simple-icons/blob/develop/data/simple-icons.json). Original source links are listed below. The Git mark is attributed to its designers under CC BY 3.0; Vue's artwork retains its upstream CC BY-NC-SA 4.0 license. All marks identify the technologies used in the profile.

| Badge | Background | Mark | Source |
| --- | --- | --- | --- |
| Python | `#3776AB` | `#FFFFFF` | [Source](https://www.python.org/community/logos/) |
| LangChain | `#1C3C3C` | `#7FC8FF` | [Source](https://www.langchain.com/langchain) |
| OpenAI SDK | `#000000` | `#FFFFFF` | [Source](https://openai.com/brand/) |
| DeepSeek | `#282C34` | `#5786FE` | [Source](https://www.deepseek.com) |
| Tool Calling | `#455A64` | None | Unbranded capability label |
| Embeddings | `#455A64` | None | Unbranded capability label |
| Weaviate | `#1C3C3C` | `#75FBAE` | [Source](https://weaviate.io/img/site/2026/weaviate-logo-2-colours-dark-green.svg) |
| Flask | `#000000` | `#FFFFFF` | [Source](https://github.com/pallets/flask/blob/85c5d93cbd049c4bd0679c36fd1ddcae8c37b642/docs/_static/flask-icon.svg) |
| SQLAlchemy | `#D71F00` | `#FFFFFF` | [Source](https://commons.wikimedia.org/wiki/File:SQLAlchemy.svg) |
| Pydantic | `#282C34` | `#E92063` | [Source](https://github.com/pydantic/pydantic/blob/94c748001a32992a587694b999fb1f3d2f1fc1fe/docs/logo-white.svg) |
| TypeScript | `#007ACC` | `#FFFFFF` | [Source](https://www.typescriptlang.org/branding) |
| Vue.js | `#2C3E50` | `#4FC08D` | [Source](https://github.com/vuejs/art/blob/a1c78b74569b70a25300925b4eacfefcc143b8f6/logo.svg) |
| React | `#282C34` | `#61DAFB` | [Source](https://github.com/facebook/create-react-app/blob/282c03f9525fdf8061ffa1ec50dce89296d916bd/test/fixtures/relative-paths/src/logo.svg) |
| Node.js | `#339933` | `#FFFFFF` | [Source](https://nodejs.org/en/about/branding) |
| Swift / SwiftUI | `#F05138` | `#FFFFFF` | [Source](https://developer.apple.com/swift/resources/) |
| Git | `#F05032` | `#FFFFFF` | [Source](https://git-scm.com/community/logos) |
| Vite | `#2C3A42` | `#9135FF` | [Source](https://github.com/voidzero-dev/community-design-resources/blob/55902097229cf01cf2a4ceb376f992f5cf306756/brand-assets/vite/vite-icon-color-bracketless.svg) |

## Juejin link

The dark Juejin entry combines its brand mark, label, follower count, and outbound arrow into one linked badge. `juejin-mark.svg` is the Simple Icons mark obtained through Shields.io. The existing daily contribution workflow runs `scripts/update-juejin.py`, reads `data.follower_count` from the public Juejin user API, and publishes `juejin-profile.svg` plus its timestamped metadata on the `snake` branch. If the API fails, it preserves the last successfully generated badge and its original update timestamp. The badge does not depend on the reliability of Shields.io's live Juejin proxy.

## Earlier compact concept

`profile-banner-compact.png` was edited with the built-in imagegen tool using the previous compact strip as the edit target and the original banner as the artwork reference.

Compact banner prompt:

> Edit Image 1, the compact rounded signature strip. Image 2 is only the reference for the silver metallic tidal wave sculpture. Preserve Image 1's compact long thin shape, dark charcoal color, rounded corners, transparent outer canvas, exact single-line typography 'J.Tide | AI Agent Engineer', identity text placement, and modest text size. The image canvas can remain 1920 x 819 exactly as Image 1; the actual visible nameplate must remain confined to the same narrow horizontal band, approximately x=13 to 1907 and y=321 to 499, with full transparency outside. Do not expand or increase the height of the strip. Add the recognizable sculptural brushed-silver tidal ribbon from Image 2 to the RIGHTMOST 25 percent of the nameplate only, gracefully scaled down to fit the strip height. Keep its silver texture and very subtle sage-green edge, but greatly subdue its highlights so it is a quiet decorative accent, lower contrast than the identity text. It should be a miniature of the reference wave integrated naturally into the dark right end of the bar, entirely clipped inside the rounded silhouette. Leave generous dark breathing space between the text and the artwork. No additional text, no extra panels, no cards, no new symbols, no giant wave, no tall hero image, no glow, no pattern. The requested final design is a calm low-profile rounded signature banner that retains the recognizable original wave as a small right-side detail.

## Original concept

`profile-banner.png` was generated using Codex's built-in imagegen tool. It is retained as the original artwork reference; the profile now uses the SVG signature banner above.

Generation prompt:

> Use case: ads-marketing. Create one finished premium GitHub profile cover banner for a developer named J.Tide, identifying as an AI Agent Engineer. Aspect ratio exactly 3:1, ideally 1920x640. The banner is a polished editorial typographic composition, not a mockup of a website. Background: uniform very dark cool charcoal #0d1117 with barely visible fine photographic grain. Left 60 percent: exquisite crisp white sans-serif typography with strict left alignment and generous negative space. Text verbatim, ONLY two lines of text: large 'J.Tide' and below in smaller restrained muted mint-green type 'AI Agent Engineer'. Render exact spelling and case. Right 35 percent: a single refined physical sculptural tidal ribbon, folded like a flowing wave, brushed satin silver and graphite, one subtle desaturated emerald edge, photographed in a dark studio with controlled soft highlights. A restrained architectural sculpture suggesting the name Tide, with a clear silhouette, no busy detail. Premium modern personal portfolio feel, sober, confident, high craft, sharp readable typography at thumbnail scale. Keep all text well inside margins at least 80 pixels. Avoid purple, blue glow, grids, circuit lines, robots, chat bubbles, icons, fake UI, logos from other brands, gradients behind text, extra labels, slogans, microcopy, pills, watermarks, additional text. Output only the final wide banner image.
