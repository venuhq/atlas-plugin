# Atlas plugin

Atlas CRM tools and a skill for creating Venu business themes. The public package contains instructions, a contrast-checking helper, and a connection to Atlas's hosted MCP server. It does not include CRM data or credentials. An authorized Atlas account is required to use the tools.

## Install

Use Codex CLI or a supported desktop client with shell access. No GitHub account is required to download this public repository.

```sh
codex plugin marketplace add https://github.com/venuhq/atlas-plugin.git
```

Open the plugin browser (`/plugins` in Codex CLI), select the added marketplace, and install **Atlas**. The generated marketplace's identifier is `personal`; identify this source by its repository URL if you have other marketplace sources. Authenticate to Atlas through the client's MCP OAuth flow when prompted. Start a new task/session after installing so the skill and tools become available.

Example requests:

- “Create a theme for [business] in Atlas.”
- “Update that business's theme to use its new logo.”
- “Apply the saved theme to my configured demo merchant.”

Choose your demo merchant in Atlas Settings before applying a theme. Each coworker authenticates with their own Atlas account; installation does not grant access to Atlas. This repository is for local/desktop plugin distribution, not a public ChatGPT web directory listing.

## Updates

```sh
codex plugin marketplace upgrade
```

Refresh the Atlas plugin in the plugin browser as needed and start a new session. MCP server behavior is hosted by Atlas; skill changes are delivered through this repository.

## Theme workflow

The skill researches the business's own branding, checks text contrast, prepares three logo variants, obtains one-time upload URLs through MCP, uploads local files from the shell, and saves a complete theme draft. Applying a theme is a separate action that changes the configured demo merchant's public name and theme.

Local theme creation needs Python 3 for the bundled contrast helper, `curl` for uploads, a browser, and an image-processing tool such as ImageMagick. SVG rasterization may use `rsvg-convert` or another available renderer. Atlas can alternatively run its hosted theme generator through `request_business_theme_generation`.

## Repository layout

- `.agents/plugins/marketplace.json`: installable marketplace catalog.
- `plugins/atlas/.codex-plugin/plugin.json`: plugin manifest.
- `plugins/atlas/.mcp.json`: remote MCP connection; no embedded credentials.
- `plugins/atlas/skills/create-business-theme/`: skill, references and contrast helper.

Maintain the supported fonts, field names and image dimensions alongside the Atlas MCP schemas. This skill was adapted from Atlas's hosted theme-agent workflow; it uses MCP-issued upload URLs instead of Cloudflare API credentials.
