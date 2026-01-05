# excalidraw

Generate hand-drawn style diagrams as Excalidraw JSON files.

## Use Cases

- Architecture diagrams
- Flowcharts
- System design diagrams
- Sequence diagrams

## Critical Rules

1. **Arrow Binding**: Arrows must bind bidirectionally
   - Arrow needs `startBinding` and `endBinding`
   - Rectangle needs `boundElements` array

2. **Text Dimensions**: Text elements must have `width` and `height`

3. **Background Regions**: Must fully cover contained elements with 40px padding

4. **No Overlaps**: Arrows must not cross unrelated components

## Color System

| Purpose | Background | Stroke |
|---------|------------|--------|
| Primary / Phase 1 | `#a5d8ff` | `#1971c2` |
| Secondary / Phase 2 | `#b2f2bb` | `#2f9e44` |
| Accent / Shared | `#fff3bf` | `#e67700` |
| Storage / State | `#d0bfff` | `#7048e8` |

## Layout Rules

- Align coordinates to multiples of 20
- Component spacing: 100-150px
- Standard component size: 140×60
- Background regions: opacity 30

## Element Templates

### Rectangle
```json
{
  "type": "rectangle",
  "x": 100, "y": 100,
  "width": 140, "height": 60,
  "backgroundColor": "#a5d8ff",
  "strokeColor": "#1971c2",
  "roundness": { "type": 3 },
  "boundElements": [{"id": "arrow-id", "type": "arrow"}]
}
```

### Text
```json
{
  "type": "text",
  "x": 120, "y": 120,
  "width": 80, "height": 24,
  "text": "Label",
  "fontSize": 16,
  "fontFamily": 4
}
```

### Arrow
```json
{
  "type": "arrow",
  "x": 240, "y": 130,
  "points": [[0, 0], [100, 0]],
  "startBinding": { "elementId": "source-id", "focus": 0, "gap": 5 },
  "endBinding": { "elementId": "target-id", "focus": 0, "gap": 5 },
  "endArrowhead": "arrow"
}
```

## Avoiding Arrow Crossings

When arrows would cross components:

1. **Triangle Layout**: For 3 components with return arrow
2. **Diamond Layout**: For 4 components with return arrow
3. **Bypass Path**: Route arrows above/below components

```json
"points": [[0, 0], [0, -80], [-400, -80], [-400, 0]]
```

## Output

- **Format**: `.excalidraw.json`
- **Usage**: Drag into excalidraw.com or open with VS Code extension
