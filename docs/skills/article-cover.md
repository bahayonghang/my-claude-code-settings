# article-cover

Generate professional article cover images as SVG files.

## Use Cases

- Blog post cover images
- Technical article banners
- Documentation headers
- Social media preview images

## Features

- **Standard ViewBox**: 1200×630 (1.91:1 ratio, social media friendly)
- **Dark Tech Theme**: GitHub-style dark gradients
- **Multiple Layouts**: Comparison, flow, and single-concept patterns
- **Tag Support**: Bottom tag pills for keywords

## Design Patterns

### Comparison Layout
Best for performance comparisons, version upgrades, before/after scenarios.

```
┌─────────────────────────────────────────────────┐
│  [Logo]                           [Badge: 100x+]│
│                                                 │
│  ┌─────────┐    VS    ┌─────────┐    ┌────────┐│
│  │ Before  │  ────►   │ Middle  │ ►  │ After  ││
│  └─────────┘          └─────────┘    └────────┘│
│                                                 │
│         Main Title (Large, Gradient)            │
│           Subtitle (Medium, White)              │
│    [Tag1]  [Tag2]  [Tag3]  [Tag4]  [Tag5]      │
└─────────────────────────────────────────────────┘
```

### Flow Layout
Best for process explanations, architecture overviews.

```
┌─────────────────────────────────────────────────┐
│  [Logo]                                         │
│                                                 │
│  [Input] ──► [Process Box] ──► [Output]         │
│                                                 │
│         Main Title (Large, Gradient)            │
│           Subtitle (Medium, White)              │
│    [Tag1]  [Tag2]  [Tag3]  [Tag4]              │
└─────────────────────────────────────────────────┘
```

## Color System

| Purpose | Background | Stroke |
|---------|------------|--------|
| Negative/Before | `#1c2128` | `#dc3545` |
| Warning/Transition | `#1c2128` | `#ffcc02` |
| Positive/After | `#1c2128` | `#00f2fe` |
| Accent (titles) | gradient | `#ff6b35` → `#ffcc02` |

## Text Guidelines

| Element | Size | Style |
|---------|------|-------|
| Main title | 44-48px | Bold, gradient fill |
| Subtitle | 28-32px | White |
| Labels | 14-16px | Color-coded |
| Minimum | 11px | Never smaller |

## Output

- **Format**: SVG
- **Filename**: `{article-slug}-cover.svg`
- **Usage**: Open in browser, convert to PNG via Inkscape or screenshot
