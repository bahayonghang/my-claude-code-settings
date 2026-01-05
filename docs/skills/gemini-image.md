# gemini-image

Generate images using Gemini API for text-to-image and image-to-image generation.

## Use Cases

- Create pictures and artwork
- Generate illustrations
- Image style transfer
- Multi-image composition

## Modes

### Text-to-Image
Generate images from text descriptions.

```
Prompt: "a cute orange cat"
```

### Image-to-Image
Transform or reference existing images.

```
Prompt: "https://example.com/image.jpg draw similar style"
```

### Multi-Image Reference
Combine multiple images.

```
Prompt: "https://a.jpg https://b.jpg merge these two"
```

## Setup

1. Configure API key in `config/secrets.md`
2. For local images, upload first (see tips)

## API Call

```bash
curl -s -X POST "https://api.apicore.ai/v1/images/generations" \
  -H "Authorization: Bearer API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "model_name",
    "prompt": "prompt_text",
    "size": "aspect_ratio",
    "n": 1
  }'
```

## Tips

### Chinese Text
See `tips/chinese-text.md` for handling Chinese text in prompts.

### Image Upload
See `tips/image-upload.md` for uploading local images.

## Output

Returns image URL from `data[0].url` in API response.
