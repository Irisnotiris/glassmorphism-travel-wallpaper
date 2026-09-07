# Glassmorphism Travel Wallpaper

An AI Agent Skill that transforms any uploaded photo into a premium glassmorphism travel info card phone lock screen wallpaper — with intelligent location detection and context-aware copywriting.

![License](https://img.shields.io/badge/license-MIT-blue)
![Ratio](https://img.shields.io/badge/ratio-9%3A19.5-lightgrey)
![Style](https://img.shields.io/badge/style-frosted%20glass-9cf)

[简体中文](./README.zh-CN.md) | English

## Features

- **9:19.5 ultra-vertical format** (1080×2340) — optimized for modern phone lock screens
- **Frosted glass UI card** — realistic frosted glass texture with subtle highlights, refraction, and light reflections, inspired by Apple Vision Pro / iOS Glass UI
- **Smart location detection** — analyzes the image and searches the web to identify the most likely real-world location
- **Context-aware copywriting** — generates matching English location title, subtitle, distance, and weather text based on the detected place and image mood
- **Image pre-cropping** — automatically center-crops input images to 9:19.5 to prevent stretching
- **Lock screen aware composition** — card sits in the lower portion, leaving clean space for the lock screen clock (described via iOS lock screen scenario, not hard percentages)
- **Text uniqueness** — every text element appears exactly once, no duplicates

## How It Works — Five-Stage Workflow

```
1. Image Analysis  →  2. Web Location Search  →  3. Copywriting  →  4. Generate  →  5. QA & Delivery
```

1. **Image Analysis** — Identifies scene type, geographic features, architectural style, landmarks, and color palette
2. **Web Location Search** — Extracts keywords from the analysis and searches the web to pinpoint the most similar real-world location (with confidence level)
3. **Copywriting** — Generates 2 candidate sets of English copy (place title, subtitle, distance, weather lines) based on the confirmed location, auto-selects the best one
4. **Generate** — Crops the image, fills in the copy, and calls the image generation tool with the master prompt template
5. **QA & Delivery** — Verifies composition, glass texture, text accuracy/uniqueness, and background fidelity

## Card Structure

1. **Search bar** — "Search place..." with magnifier icon and circular "+" button
2. **Photo preview** — rounded-corner image cropped from the uploaded photo
3. **Distance label** — e.g., "1.2 km" overlaid on the preview's bottom-left
4. **Location info** — place title + subtitle below the preview
5. **Directions button** — semi-transparent button on the preview's bottom-right
6. **Weather info** — two lines of fine text at the card's bottom

## Installation

Simply share this repository URL with your AI agent and ask it to install and use this skill. The agent will clone or download the repository, read `SKILL.md` for the workflow, and apply it to your image generation tasks.

Example: *"Install this skill and use it: https://github.com/Irisnotiris/glassmorphism-travel-wallpaper"*

## Usage

1. Upload any travel photo to your AI agent
2. Ask: *"Make this into a glassmorphism travel wallpaper"*
3. The skill will run the five-stage workflow automatically

## Example

| Input | Output |
|---|---|
| ![Input](./examples/input.jpg) | ![Output](./examples/output.jpg) |

Input: Amalfi Coast cliff village photo → Output: 9:19.5 lock screen wallpaper with frosted glass card, detected location "Ravello Village / Amalfi Coast", and context-aware weather details.

## File Structure

```
glassmorphism-travel-wallpaper/
├── SKILL.md                          # Main skill file (five-stage workflow)
├── README.md                         # English documentation
├── README.zh-CN.md                   # Chinese documentation
├── examples/
│   ├── input.jpg                     # Example input photo
│   └── output.jpg                    # Example output wallpaper
├── references/
│   ├── prompt-template.md            # Core generation prompt with placeholders
│   ├── image-analysis.md             # Image analysis guide
│   ├── location-search.md            # Web location search strategy
│   └── copywriting.md                # Copy generation guide
└── scripts/
    └── crop_to_ratio.py              # Image center-cropping utility
```

## Prompt Template Placeholders

All placeholders are determined by the workflow stages before image generation — not inferred by the image model itself.

| Placeholder | Source | Example |
|---|---|---|
| `{{IMAGE_DESCRIPTION}}` | Stage 1 (Image Analysis) | "Forbidden City palace, golden roof, red pillars, sunset glow" |
| `{{DISTANCE}}` | Stage 3 (Copywriting) | "1.2 km" |
| `{{PLACE_TITLE}}` | Stage 2+3 (Location + Copy) | "Forbidden City" |
| `{{SUBTITLE}}` | Stage 2+3 (Location + Copy) | "Beijing, China" |
| `{{WEATHER_LINE1}}` | Stage 3 (Copywriting) | "Evening breeze · calm" |
| `{{WEATHER_LINE2}}` | Stage 3 (Copywriting) | "Golden Hour now" |

## Related

- [glassmorphism-travel-card](https://github.com/Irisnotiris/glassmorphism-travel-card) — 3:4 poster version

## License

MIT
