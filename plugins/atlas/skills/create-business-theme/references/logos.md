# Logo preparation

## Find and view the source

Prefer an official logo from the business’s website or owned social profiles. Look for the highest resolution actual logo: SVG, an image’s largest `srcset` candidate, CSS background, or brand asset. Inspect rendered pages when assets are loaded by JavaScript.

If no official logo can be found, use the profile picture from the business’s official Facebook or Instagram account. Verify that the account belongs to the correct business/location using its name, website, address or other matching details. Prefer the highest resolution profile picture available. Do not use an unrelated account’s, directory’s or stock site’s image.

Open and visually inspect candidate images before choosing one. A filename, image URL or dimension check alone is not enough. Check that the image identifies the business, has readable lettering and a complete mark, and will work against the theme background. A suitable official social profile picture is a valid fallback even if it is not a standalone logo. Preserve the downloaded original in a task-specific directory.

## Adjust with imagegen

If any visual changes are needed, load the agent’s built-in imagegen skill and follow its editing workflow. This includes background removal, cleanup, repairing distracting artifacts, cropping, resizing, adding padding, or adapting the source to the required canvases. Supply the actual source image as the editing reference; do not ask imagegen to invent a replacement logo from a description.

Keep the business’s lettering, spelling, colors and identifying mark intact unless the user requests a brand change. Ask for the specific adjustment needed, such as removing an opaque background while preserving all lettering, or centering the intact mark on a transparent canvas with padding. Do not use Cloudflare foreground segmentation, ImageMagick or another shell image editor to perform these visual adjustments.

View every edited result and compare it with the original. Background removal can erase letters or damage a mark; reject those results and revise the edit. If a transparent treatment cannot preserve the source, retain its intact background when suitable. If imagegen is unavailable, use an already suitable asset unchanged or report that cleanup is blocked rather than silently switching editing methods.

## Prepare and inspect three variants

Preserve aspect ratio and center the mark with visible padding. Required canvases:

- `logo_image`: 1000×500.
- `square_logo_image`: 800×800.
- `wallet_image`: 1032×336.

Use imagegen for any visual adaptation to these canvases. Prefer transparent backgrounds when they preserve the mark and remain legible. Export 8-bit lossless WebP for terminal compatibility. Shell tools may inspect dimensions or perform format/bit-depth conversion without changing the composition or pixels’ appearance; they must not perform cleanup, background removal or other visual edits. If the available imagegen output cannot meet a required canvas size, report the limitation instead of uploading a mismatched variant.

Open and view all three final files against the selected theme background before upload. Check legibility, intact lettering, aspect ratio, padding, clipping and unwanted artifacts. This visual inspection also applies to existing image IDs being reused: view their delivery images before deciding they are suitable.

Upload each approved variant through a separate `create_theme_image_upload` URL using the shell procedure in `SKILL.md`. Store its matching image ID. Only use an empty `logo_image` and omit the optional image fields after neither an official logo nor an official Facebook/Instagram profile picture is usable; explain the limitation to the user.
