# GPT-RPG System - Testing Instructions

## Overview
This directory contains **automated and manual tests** for verifying the functionality of the GPT-RPG System.

---

## **1. Running Unit Tests (Automated)**
Before making any changes, run the automated tests to ensure everything is working correctly.

### **How to Run Tests**
1. Ensure all dependencies are installed:
   ```sh
   pip install -r requirements.txt

2. Run the full test suite using:
   ```sh
   pytest tests/

3. If you only want to run a specific test file:
   ```sh
   pytest tests/test_npc_ai.py

## 2. Manual Testing Instructions
For features that require player interaction, follow these test cases.

### NPC Memory & Interaction Test
Goal: Ensure NPCs react appropriately to past interactions.

- Start a new RPG session.  
- Speak with an NPC, insult them, then return later.  
- Expected behavior: NPC should remember the insult and react accordingly.

### Combat System Test
Goal: Verify turn-based mechanics work properly.

- Enter a battle with an enemy.  
- Use a mix of attacks, blocks, and spells.  
- Expected behavior: Damage, cooldowns, and turn orders should function correctly.

### World Event System Test
Goal: Check if the game properly handles seasonal changes and world events.

- Simulate a 1-year timeskip.  
- Observe how the economy, NPCs, and environment shift.  
- Expected behavior: Trade should be affected by weather, and factions should shift over time.

---

## 3. Debugging & Reporting Issues
If you find a bug:

1. Open an issue on GitHub:  
[GitHub Issues](https://github.com/GPT-Design/GPT-RPG-System/issues)

2. Describe:
- The steps to reproduce the bug.
- What you expected to happen.
- What actually happened.

3. Attach screenshots or logs if possible.

---

## Upcoming Test Coverage
- Core Engine Testing  
- NPC Memory & AI Behavior  
- Combat Mechanics  
- Economy & Trade Simulation  
- Future Tests: Multiplayer, UI/UX, Performance  


