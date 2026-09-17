# Profile assets

`profile-banner.svg` is the current typography-only header: a 1600 x 184 charcoal strip with small rounded corners, the name above the role, and no decorative image. `profile-banner-mobile.svg` uses an 800 x 200 layout so the text remains readable on narrow screens. The README selects the mobile asset below 600 pixels through a `<picture>` source.

Both current headers are editable SVGs and do not depend on generated imagery or external fonts. The raster concepts below are retained as design references.

## Earlier compact concept

`profile-banner-compact.png` was edited with the built-in imagegen tool using the previous compact strip as the edit target and the original banner as the artwork reference.

Compact banner prompt:

> Edit Image 1, the compact rounded signature strip. Image 2 is only the reference for the silver metallic tidal wave sculpture. Preserve Image 1's compact long thin shape, dark charcoal color, rounded corners, transparent outer canvas, exact single-line typography 'J.Tide | AI Agent Engineer', identity text placement, and modest text size. The image canvas can remain 1920 x 819 exactly as Image 1; the actual visible nameplate must remain confined to the same narrow horizontal band, approximately x=13 to 1907 and y=321 to 499, with full transparency outside. Do not expand or increase the height of the strip. Add the recognizable sculptural brushed-silver tidal ribbon from Image 2 to the RIGHTMOST 25 percent of the nameplate only, gracefully scaled down to fit the strip height. Keep its silver texture and very subtle sage-green edge, but greatly subdue its highlights so it is a quiet decorative accent, lower contrast than the identity text. It should be a miniature of the reference wave integrated naturally into the dark right end of the bar, entirely clipped inside the rounded silhouette. Leave generous dark breathing space between the text and the artwork. No additional text, no extra panels, no cards, no new symbols, no giant wave, no tall hero image, no glow, no pattern. The requested final design is a calm low-profile rounded signature banner that retains the recognizable original wave as a small right-side detail.

## Original concept

`profile-banner.png` was generated using Codex's built-in imagegen tool. It is retained as the original artwork reference; the profile now uses the compact banner above.

Generation prompt:

> Use case: ads-marketing. Create one finished premium GitHub profile cover banner for a developer named J.Tide, identifying as an AI Agent Engineer. Aspect ratio exactly 3:1, ideally 1920x640. The banner is a polished editorial typographic composition, not a mockup of a website. Background: uniform very dark cool charcoal #0d1117 with barely visible fine photographic grain. Left 60 percent: exquisite crisp white sans-serif typography with strict left alignment and generous negative space. Text verbatim, ONLY two lines of text: large 'J.Tide' and below in smaller restrained muted mint-green type 'AI Agent Engineer'. Render exact spelling and case. Right 35 percent: a single refined physical sculptural tidal ribbon, folded like a flowing wave, brushed satin silver and graphite, one subtle desaturated emerald edge, photographed in a dark studio with controlled soft highlights. A restrained architectural sculpture suggesting the name Tide, with a clear silhouette, no busy detail. Premium modern personal portfolio feel, sober, confident, high craft, sharp readable typography at thumbnail scale. Keep all text well inside margins at least 80 pixels. Avoid purple, blue glow, grids, circuit lines, robots, chat bubbles, icons, fake UI, logos from other brands, gradients behind text, extra labels, slogans, microcopy, pills, watermarks, additional text. Output only the final wide banner image.

The static technology badges in `stack/` come from Shields.io and use Simple Icons. Their shared background is `#161d25` and logo color is `#a8cdbd`. They are stored locally so the profile does not depend on a badge service for each page load. Example source:

`https://img.shields.io/badge/Python-161d25?style=flat-square&logo=python&logoColor=a8cdbd`

The Juejin follower badge in the profile README reads `data.follower_count` from the public Juejin user API through Shields.io. It links to the Juejin profile and requests a one-hour badge cache.
