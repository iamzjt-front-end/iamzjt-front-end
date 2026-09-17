# Profile assets

The current header uses `profile-cover-ai.svg` (1600 x 224) and `profile-cover-ai-mobile.svg` (800 x 210). The cover has a dark blue-gray background, a 24-pixel corner radius, stacked name and motto, and an AI core connected to tools and data. Typography is native SVG for crisp rendering. The original artwork is saved as `profile-ai-art.png`, generated with the built-in imagegen tool and embedded unchanged in each header. SVG viewports and edge masks fit the artwork into the narrow responsive layouts. Earlier headers and JT marks are retained as design references and are no longer used by the README.

## Technology badges

The local SVG badges in `stack/` are generated with Shields.io's `flat-square` style and displayed at a 24-pixel height, matching the original profile's compact rectangular badges. TypeScript, Node.js, and Git recover their original color backgrounds and white marks; Vue 3, React, and Vite recover their original dark backgrounds and colored marks. Added AI tools use the same combination of brand-color backgrounds or dark backgrounds with colored marks. Labels remain white throughout.

Icon geometry comes from Simple Icons (originally obtained through Shields.io); the OpenAI mark comes from Simple Icons v13, and the Weaviate mark comes from the logo published on its official site. The stack is ordered AI & Agents, Backend, Frontend, then Native & Tooling, with all categories displayed directly. Tool Calling, RAG, and Embeddings appear as a secondary capability line rather than competing with product logos. Earlier Tool Calling and Embeddings badge files remain as design references.

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
| Vue 3 | `#2C3E50` | `#4FC08D` | [Source](https://github.com/vuejs/art/blob/a1c78b74569b70a25300925b4eacfefcc143b8f6/logo.svg) |
| React | `#282C34` | `#61DAFB` | [Source](https://github.com/facebook/create-react-app/blob/282c03f9525fdf8061ffa1ec50dce89296d916bd/test/fixtures/relative-paths/src/logo.svg) |
| Node.js | `#339933` | `#FFFFFF` | [Source](https://nodejs.org/en/about/branding) |
| Swift / SwiftUI | `#F05138` | `#FFFFFF` | [Source](https://developer.apple.com/swift/resources/) |
| Git | `#F05032` | `#FFFFFF` | [Source](https://git-scm.com/community/logos) |
| Vite | `#2C3A42` | `#9135FF` | [Source](https://github.com/voidzero-dev/community-design-resources/blob/55902097229cf01cf2a4ceb376f992f5cf306756/brand-assets/vite/vite-icon-color-bracketless.svg) |
| Tailwind CSS | `#0F172A` | `#06B6D4` | [Source](https://tailwindcss.com/brand) |
| UnoCSS | `#333333` | `#FFFFFF` | [Source](https://github.com/unocss/unocss/blob/main/playground/public/icon.svg) |
| 微信小程序 | `#07C160` | `#FFFFFF` | [WeChat brand mark](https://wechat.design/brand/main-brand) |
| uni-app | `#2B9939` | Original icon | [Official documentation icon](https://qiniu-web-assets.dcloud.net.cn/unidoc/zh/icon.png?v=1556263038788) |
| Taro | `#1978F6` | Original white mark | [Official documentation mark](https://github.com/NervJS/taro-docs/blob/master/static/img/logo-taro.png) |

The frontend row lists TypeScript, Vue 3, React, Tailwind CSS, UnoCSS, Vite, WeChat Mini Programs, uni-app, and Taro in that order. The WeChat badge uses its parent brand mark; uni-app and Taro embed the original official PNG icons in the local SVG badges.

## Juejin link

`juejin-writing.svg` is a static writing link labeled “掘金 · 技术文章 ↗”. It links directly to the author's article list, without follower counts. The follower-fetching script and its workflow steps have been removed; the contribution snake continues to update independently. `juejin-mark.svg` is the Simple Icons mark obtained through Shields.io.

## Current AI cover generation

Mode: built-in imagegen. Output: `profile-ai-art.png`. Name and motto are added separately in the SVG header.

Prompt:

> Use case: ads-marketing. Design one exceptionally polished, restrained AI-themed panoramic decorative background for a developer's narrow GitHub profile header. Brand J.Tide, AI agent engineer, audience experienced software engineers. This output is ONLY the background illustration; typesetting will be added separately in code. No text of any kind anywhere, except the exact two letters AI on the central chip. Composition: extremely wide landscape aspect ratio 6:1, ideally 2400 by 400 pixels, artwork fills the canvas to its edges, no margins, no mockup, no enclosing frame, no rounded corners because those will be applied in code. LEFT 62 percent must be nearly uniform near-black blue-gray #0b1018, calm negative space for a name and a one-line motto. RIGHT 32 percent contains a small sophisticated AI reasoning core: one compact flat square midnight-blue silicon tile with softly rounded corners and the letters AI engraved in warm-white, subtly elevated above a precision graphic surface. The chip is seen nearly front-on with only a very shallow architectural perspective, not a dramatic 3D angle. Only three very thin clean routed connections extend from the core toward three tiny square peripheral modules, evoking an agent using tools. Keep the whole motif legible and contained well inside the banner height, with large dark breathing room. Material finish: matte graphite with restrained cool silver edges, one very soft desaturated ice-blue accent. Premium industrial product photography fused with meticulous technical editorial graphics. Even controlled studio light; no dazzling highlights. The illustration subtly fades naturally into the plain background towards the center. It must feel composed, mature, and understated at a displayed size of 850 by 140 pixels. Avoid every one of these: metallic waves, ribbon sculptures, JT monograms, squiggly lettermarks, handwritten strokes, brains, robots, humanoids, faces, starbursts, purple gradients, neon cyan glow, hologram effects, busy circuit boards, random dots, floating text, charts, mock browser chrome, extra labels, watermarks. Deliver just one finished clean panoramic banner background.

## Earlier compact concept

`profile-banner-compact.png` was edited with the built-in imagegen tool using the previous compact strip as the edit target and the original banner as the artwork reference.

Compact banner prompt:

> Edit Image 1, the compact rounded signature strip. Image 2 is only the reference for the silver metallic tidal wave sculpture. Preserve Image 1's compact long thin shape, dark charcoal color, rounded corners, transparent outer canvas, exact single-line typography 'J.Tide | AI Agent Engineer', identity text placement, and modest text size. The image canvas can remain 1920 x 819 exactly as Image 1; the actual visible nameplate must remain confined to the same narrow horizontal band, approximately x=13 to 1907 and y=321 to 499, with full transparency outside. Do not expand or increase the height of the strip. Add the recognizable sculptural brushed-silver tidal ribbon from Image 2 to the RIGHTMOST 25 percent of the nameplate only, gracefully scaled down to fit the strip height. Keep its silver texture and very subtle sage-green edge, but greatly subdue its highlights so it is a quiet decorative accent, lower contrast than the identity text. It should be a miniature of the reference wave integrated naturally into the dark right end of the bar, entirely clipped inside the rounded silhouette. Leave generous dark breathing space between the text and the artwork. No additional text, no extra panels, no cards, no new symbols, no giant wave, no tall hero image, no glow, no pattern. The requested final design is a calm low-profile rounded signature banner that retains the recognizable original wave as a small right-side detail.

## Original concept

`profile-banner.png` was generated using Codex's built-in imagegen tool. It is retained as the original artwork reference; the profile now uses the SVG signature banner above.

Generation prompt:

> Use case: ads-marketing. Create one finished premium GitHub profile cover banner for a developer named J.Tide, identifying as an AI Agent Engineer. Aspect ratio exactly 3:1, ideally 1920x640. The banner is a polished editorial typographic composition, not a mockup of a website. Background: uniform very dark cool charcoal #0d1117 with barely visible fine photographic grain. Left 60 percent: exquisite crisp white sans-serif typography with strict left alignment and generous negative space. Text verbatim, ONLY two lines of text: large 'J.Tide' and below in smaller restrained muted mint-green type 'AI Agent Engineer'. Render exact spelling and case. Right 35 percent: a single refined physical sculptural tidal ribbon, folded like a flowing wave, brushed satin silver and graphite, one subtle desaturated emerald edge, photographed in a dark studio with controlled soft highlights. A restrained architectural sculpture suggesting the name Tide, with a clear silhouette, no busy detail. Premium modern personal portfolio feel, sober, confident, high craft, sharp readable typography at thumbnail scale. Keep all text well inside margins at least 80 pixels. Avoid purple, blue glow, grids, circuit lines, robots, chat bubbles, icons, fake UI, logos from other brands, gradients behind text, extra labels, slogans, microcopy, pills, watermarks, additional text. Output only the final wide banner image.
