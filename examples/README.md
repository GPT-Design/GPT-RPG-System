# Example Configurations 

## How to Use These Configurations
Copy the configuration you want into a file called config.json
Place it inside your game directory
Run the game with the config:

python3 main.py --config config.json
Now you’re ready to experience GPT-RPG System in the mode that best suits your playstyle!

## Quick-Start Configurations
These example configurations allow you to **jump straight into different RPG playstyles** without needing deep customization.

---

## **Classic Turn-Based RPG (D&D-Style)**
```json
{
    "game_mode": "turn_based",
    "world_size": "medium",
    "npc_behavior": "memory_retaining",
    "combat_style": "initiative_order",
    "economy": "player_influenced",
    "magic_system": "mana_based",
    "difficulty": "balanced"
}

## **Action RPG (Like Diablo)**
```json
{
    "game_mode": "real_time",
    "world_size": "large",
    "npc_behavior": "reactionary",
    "combat_style": "hack_and_slash",
    "economy": "fixed",
    "magic_system": "cooldown_based",
    "difficulty": "challenging"
}

## **Narrative-Heavy RPG (Visual Novel / TTRPG Hybrid)**
```json
{
    "game_mode": "narrative_driven",
    "world_size": "small",
    "npc_behavior": "deep_memory",
    "combat_style": "story_focused",
    "economy": "irrelevant",
    "magic_system": "soft_magic",
    "difficulty": "roleplay_focused"
}

## **Grand Strategy RPG (Like Crusader Kings)**
```json
{
    "game_mode": "kingdom_management",
    "world_size": "huge",
    "npc_behavior": "faction_diplomacy",
    "combat_style": "auto_resolved",
    "economy": "dynamic",
    "magic_system": "restricted",
    "difficulty": "political_depth"
}

## **Tabletop Emulation (For DMs & Homebrew RPGs)**
```json
{
    "game_mode": "tabletop_assist",
    "world_size": "modular",
    "npc_behavior": "dm_controlled",
    "combat_style": "manual_resolution",
    "economy": "none",
    "magic_system": "fully_customizable",
    "difficulty": "dm_defined"
}

