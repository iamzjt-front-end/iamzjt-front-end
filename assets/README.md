# Profile assets

The current header uses `profile-intro-light.svg` and `profile-intro-dark.svg` at 1600 x 152. The corresponding `profile-intro-mobile-*.svg` assets use an 800 x 190 layout below 600 pixels. The README selects the appropriate screen size and color scheme with `<picture>` sources. These are editable SVGs using system fonts; the former `profile-banner*` assets are retained as earlier concepts.

## Technology badges

The local SVG badges in `stack/` use each tool's brand palette with a consistent 24-pixel height and small rounded corners. Icon geometry comes from Simple Icons (originally obtained through Shields.io); the OpenAI mark comes from Simple Icons v13, and the Weaviate mark comes from the logo published on its official site. Black or white foregrounds are chosen to keep text contrast at least 4.5:1. Tool Calling and Embeddings are unbranded capability labels and use a neutral gray.

Palette reference: [Simple Icons data](https://github.com/simple-icons/simple-icons/blob/develop/data/simple-icons.json). Original source links are listed below. The Git mark is attributed to its designers under CC BY 3.0; Vue's artwork retains its upstream CC BY-NC-SA 4.0 license. All marks identify the technologies used in the profile.

| Badge | Background | Source |
| --- | --- | --- |
| Python | `#3776AB` | [Source](https://www.python.org/community/logos/) |
| LangChain | `#7FC8FF` | [Source](https://www.langchain.com/langchain) |
| OpenAI SDK | `#000000` | [Source](https://openai.com/brand/) |
| DeepSeek | `#5786FE` | [Source](https://www.deepseek.com) |
| Tool Calling | `#59636E` | Unbranded capability label |
| Embeddings | `#59636E` | Unbranded capability label |
| Weaviate | `#75FBAE` | [Source](https://weaviate.io/img/site/2026/weaviate-logo-2-colours-dark-green.svg) |
| Flask | `#3BABC3` | [Source](https://github.com/pallets/flask/blob/85c5d93cbd049c4bd0679c36fd1ddcae8c37b642/docs/_static/flask-icon.svg) |
| SQLAlchemy | `#D71F00` | [Source](https://commons.wikimedia.org/wiki/File:SQLAlchemy.svg) |
| Pydantic | `#E92063` | [Source](https://github.com/pydantic/pydantic/blob/94c748001a32992a587694b999fb1f3d2f1fc1fe/docs/logo-white.svg) |
| TypeScript | `#3178C6` | [Source](https://www.typescriptlang.org/branding) |
| Vue | `#4FC08D` | [Source](https://github.com/vuejs/art/blob/a1c78b74569b70a25300925b4eacfefcc143b8f6/logo.svg) |
| React | `#61DAFB` | [Source](https://github.com/facebook/create-react-app/blob/282c03f9525fdf8061ffa1ec50dce89296d916bd/test/fixtures/relative-paths/src/logo.svg) |
| Node.js | `#5FA04E` | [Source](https://nodejs.org/en/about/branding) |
| Swift / SwiftUI | `#F05138` | [Source](https://developer.apple.com/swift/resources/) |
| Git | `#F03C2E` | [Source](https://git-scm.com/community/logos) |
| Vite | `#9135FF` | [Source](https://github.com/voidzero-dev/community-design-resources/blob/55902097229cf01cf2a4ceb376f992f5cf306756/brand-assets/vite/vite-icon-color-bracketless.svg) |

## Juejin link

The blue Juejin entry combines its brand mark, profile label, live follower count, and outbound arrow into one linked badge. It reads `data.follower_count` from the public Juejin user API through Shields.io and requests a one-hour badge cache.

## Earlier compact concept

`profile-banner-compact.png` was edited with the built-in imagegen tool using the previous compact strip as the edit target and the original banner as the artwork reference.

Compact banner prompt:

> Edit Image 1, the compact rounded signature strip. Image 2 is only the reference for the silver metallic tidal wave sculpture. Preserve Image 1's compact long thin shape, dark charcoal color, rounded corners, transparent outer canvas, exact single-line typography 'J.Tide | AI Agent Engineer', identity text placement, and modest text size. The image canvas can remain 1920 x 819 exactly as Image 1; the actual visible nameplate must remain confined to the same narrow horizontal band, approximately x=13 to 1907 and y=321 to 499, with full transparency outside. Do not expand or increase the height of the strip. Add the recognizable sculptural brushed-silver tidal ribbon from Image 2 to the RIGHTMOST 25 percent of the nameplate only, gracefully scaled down to fit the strip height. Keep its silver texture and very subtle sage-green edge, but greatly subdue its highlights so it is a quiet decorative accent, lower contrast than the identity text. It should be a miniature of the reference wave integrated naturally into the dark right end of the bar, entirely clipped inside the rounded silhouette. Leave generous dark breathing space between the text and the artwork. No additional text, no extra panels, no cards, no new symbols, no giant wave, no tall hero image, no glow, no pattern. The requested final design is a calm low-profile rounded signature banner that retains the recognizable original wave as a small right-side detail.

## Original concept

`profile-banner.png` was generated using Codex's built-in imagegen tool. It is retained as the original artwork reference; the profile now uses the compact banner above.

Generation prompt:

> Use case: ads-marketing. Create one finished premium GitHub profile cover banner for a developer named J.Tide, identifying as an AI Agent Engineer. Aspect ratio exactly 3:1, ideally 1920x640. The banner is a polished editorial typographic composition, not a mockup of a website. Background: uniform very dark cool charcoal #0d1117 with barely visible fine photographic grain. Left 60 percent: exquisite crisp white sans-serif typography with strict left alignment and generous negative space. Text verbatim, ONLY two lines of text: large 'J.Tide' and below in smaller restrained muted mint-green type 'AI Agent Engineer'. Render exact spelling and case. Right 35 percent: a single refined physical sculptural tidal ribbon, folded like a flowing wave, brushed satin silver and graphite, one subtle desaturated emerald edge, photographed in a dark studio with controlled soft highlights. A restrained architectural sculpture suggesting the name Tide, with a clear silhouette, no busy detail. Premium modern personal portfolio feel, sober, confident, high craft, sharp readable typography at thumbnail scale. Keep all text well inside margins at least 80 pixels. Avoid purple, blue glow, grids, circuit lines, robots, chat bubbles, icons, fake UI, logos from other brands, gradients behind text, extra labels, slogans, microcopy, pills, watermarks, additional text. Output only the final wide banner image.
