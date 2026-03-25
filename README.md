# The Zack Pack (TZP) - Client Modpack

**A challenging modded Minecraft experience with an AI Dungeon Master**

- Minecraft: **1.21.1**
- NeoForge: **21.1.220**
- Mods: **172**
- Version: **1.1.0**

## Download & Install

The easiest way to install TZP is through the **TZP Launcher**:

1. Download the latest launcher release from [TZP-launcher](https://github.com/TheZackPack/TZP-launcher/releases)
2. Run the launcher -- it will automatically download and install the modpack
3. Click **Play** to launch Minecraft with all mods configured

### Manual Install

If you prefer to install manually:

1. Install [NeoForge 21.1.220](https://neoforged.net/) for Minecraft 1.21.1
2. Clone or download this repository
3. Copy the contents of `mods/` into your Minecraft `mods/` folder
4. Copy the contents of `config/` into your Minecraft `config/` folder
5. Launch Minecraft with the NeoForge 1.21.1 profile

## What's Included

This repo is the **source of truth** for the TZP modpack. It contains:

- `mods/` -- All 172 mod JARs required to play on the TZP server
- `config/` -- Pre-tuned mod configurations
- `kubejs/` -- Custom KubeJS scripts (recipes, events, tweaks)
- `manifest.json` -- Machine-readable file manifest with hashes (used by the TZP launcher for incremental updates)
- `pack.json` -- Pack metadata

## Mod Highlights

TZP includes a curated set of 172 mods spanning technology, magic, exploration, building, and quality-of-life. Some highlights:

| Category | Notable Mods |
|---|---|
| **Tech** | Mekanism, Applied Energistics 2, Refined Storage, Immersive Engineering, Flux Networks, Extreme Reactors, Compact Machines, Industrial Foregoing |
| **Magic** | Apotheosis (+ Apothic Enchanting/Spawners), Reliquary, EvilCraft |
| **Exploration** | Biomes O' Plenty, The Undergarden, Dungeons Arise, Creeper Overhaul, MowziesMobs |
| **Building** | Create, Macaw's (Doors/Furniture/Windows), Dramatic Doors, Handcrafted, Refurbished Furniture, Chisel (Athena) |
| **Farming** | Farmer's Delight, Mystical Agriculture, Aquaculture, Gobber |
| **Colony** | MineColonies, Structurize, Domum Ornamentum |
| **Storage** | Storage Drawers, Iron Chests, Sophisticated Backpacks |
| **QoL** | JEI, JourneyMap, Jade, Waystones, Embeddium, Lithium, ModernFix, Mouse Tweaks, FTB Quests |
| **AI** | MadGod Client Mod (player telemetry for the AI Dungeon Master) |

## Updating

When the modpack is updated:
- **Launcher users**: The launcher auto-detects updates on startup
- **Manual users**: Pull the latest changes and re-copy `mods/` and `config/`

## Server

The TZP server is invite-only. Contact **NightMoon_** (Zack) on Discord for access.

## Related Projects

- [TZP-launcher](https://github.com/TheZackPack/TZP-launcher) -- Desktop launcher for downloading and updating TZP
- [tzp-madgod-client](https://github.com/TheZackPack/tzp-madgod-client) -- Client-side NeoForge mod for MadGod AI integration
- [TZP-web](https://github.com/TheZackPack/TZP-web) -- TZP website and API dashboard

## License

This modpack is a curated collection of third-party mods. Each mod retains its original license. This repository exists for distribution to TZP server players.
