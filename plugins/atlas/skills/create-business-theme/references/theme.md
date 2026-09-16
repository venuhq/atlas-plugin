# Theme fields

Use the MCP tool's current input schema as the authority. `set_business_theme` accepts:

```json
{
  "businessId": "ID returned by Atlas",
  "name": "Public business name",
  "theme": {
    "font": "Inter",
    "colors": {
      "primary": "#112233",
      "primary_foreground": "#ffffff",
      "foreground": "#112233",
      "background": "#ffffff",
      "accent": "#112233"
    },
    "logo_image": ""
  }
}
```

The name is 1–120 characters. Colors are six-digit hex; use lowercase.

- `primary`: main brand color for buttons and headline surfaces.
- `primary_foreground`: text and icons on primary; contrast at least 4.5:1.
- `foreground`: default text; contrast at least 4.5:1 against background.
- `background`: screen/page background.
- `accent`: reward highlight; match primary.
- `logo_image`: uploaded 1000×500 logo ID, or empty when no usable logo exists.
- `square_logo_image`: optional uploaded 800×800 logo ID.
- `wallet_image`: optional uploaded 1032×336 logo ID.

Supported fonts: Baloo 2, DM Sans, DM Serif Display, Fields, Inter, Lora,
Merriweather, Montserrat, Nunito, Oswald, Playfair Display, Poppins, Roboto Slab.

Omitting optional images clears them from the replacement draft. Preserve their IDs for unrelated edits. Write results use `{success, result, submitted, url}`; a saved draft's `result` is its new generation ID. Read results are not wrapped this way.
