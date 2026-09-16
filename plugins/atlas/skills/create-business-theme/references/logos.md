# Logo preparation

## Find the original

Use the business's website or owned social profiles. Prefer the highest resolution actual logo: SVG, an image's largest `srcset` candidate, CSS background, or brand asset. Inspect rendered pages when assets are loaded by JavaScript. Icons, manifests and social preview images are fallbacks when there is no better original. Do not take an unrelated directory's or stock site's logo.

Download assets into a task-specific directory. Available image tools vary: use ImageMagick 7 (`magick`), ImageMagick 6 (`convert`/`identify`), or an equivalent installed raster tool. SVG sources should be rasterized before uploading, for consistent terminal rendering. With librsvg and ImageMagick 6:

```sh
rsvg-convert logo.svg --width 1200 --keep-aspect-ratio --format png --output logo-raw.png
convert logo-raw.png -depth 8 -strip PNG32:logo.png
```

Prefer 8-bit RGB/RGBA, sRGB, non-interlaced intermediates. Some terminals do not reliably render 16-bit PNG. Preserve the original download and use different output filenames.

## Opaque backgrounds

Prefer genuine transparent assets. If only an opaque original is available, upload it using `create_theme_image_upload` and the shell procedure in `SKILL.md`, then optionally request Cloudflare's foreground segmentation:

```sh
curl --fail --silent --show-error --location \
  "https://imagedelivery.net/k3593Y7l0NN1Ho1blv02Gw/$ORIGINAL_IMAGE_ID/segment=foreground,format=png" \
  --output logo-transparent.png
```

The account hash above is a public image-delivery identifier, not a credential. Inspect the downloaded format and pixels. If the transform is unavailable, retry at most twice; otherwise keep the original. Segmentation can erase letters or damage a mark. A padded intact original on a compatible background is better than a damaged transparent logo.

## Prepare three variants

Preserve aspect ratio and center the mark with visible padding. Trim only verified empty margins. Export 8-bit lossless WebP. These commands leave a 10% margin around the mark:

```sh
convert logo.png -trim +repage -resize 900x450 -background none \
  -gravity center -extent 1000x500 -colorspace sRGB -depth 8 -strip \
  -define webp:lossless=true logo.webp
convert logo.png -trim +repage -resize 720x720 -background none \
  -gravity center -extent 800x800 -colorspace sRGB -depth 8 -strip \
  -define webp:lossless=true square-logo.webp
convert logo.png -trim +repage -resize 928x302 -background none \
  -gravity center -extent 1032x336 -colorspace sRGB -depth 8 -strip \
  -define webp:lossless=true wallet-logo.webp
identify logo.webp square-logo.webp wallet-logo.webp
```

Use `magick` instead of `convert` for ImageMagick 7. Inspect each output against the theme background. Adjust padding for the actual mark if needed. Upload each variant separately through its own MCP-issued upload URL and store the matching image ID. Original-image and segmentation uploads are intermediates, not the final variant IDs.
