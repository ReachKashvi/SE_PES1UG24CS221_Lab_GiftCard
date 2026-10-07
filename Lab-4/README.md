# Pac-Man Repair Lab

This project is a single-file Pac-Man-lite clone using **Pygame**. It introduces students to grid movement, pellet collection, and ghost AI targeting rules using a small, readable object-oriented codebase.

---

## What's Provided

A working Pac-Man-lite game with:

- Grid-based movement with wall collision and pellet collection
- Four ghosts with distinct targeting behavior (Blinky chases directly, Pinky ambushes ahead of the player, Inky uses Blinky's position, Clyde flees when close) on a shared scatter/chase timer
- Frightened mode when a power pellet is eaten, with ghosts reversing direction once and becoming eatable
- Lives, scoring, and win/lose conditions

It has **one deliberate bug** and **three optional features** left as empty functions. You are expected to **analyze**, **interact with an AI assistant**, and **complete/fix** the game to make it fully functional and more interesting.

### **Use an LLM (e.g. ChatGPT or Claude) as your debugging and pair-programming partner for this lab.**

---

## Getting Started

### Setup

1. Make sure you have Python 3.10+ installed.
2. Install dependencies:

```bash
pip install pygame
```

3. Run the game:

```bash
python game.py
```

**Controls:** Arrow keys to move, `R` to reset.

---

## Tasks to Complete

Each task must be completed using an iterative process involving LLM suggestions and your critical code review.

### Task 1: Fix the power pellet bug

> Eating a power pellet is supposed to send every ghost into frightened mode for a few seconds, reversing their direction and making them vulnerable. In the current build, eating a power pellet does nothing beyond the usual 10 points — frightened mode never triggers. The maze layout marks power pellets with one specific character; check what character `eat()` compares a cell against, versus what the maze grid actually uses for power pellets.

### Task 2: Implement `ghost_color(name, mode)`

> Called once per ghost per frame in `draw`, as `color = ghost_color(ghost.name, mode) or color`, after the default color for that ghost/mode has already been computed. `name` is one of `"blinky"`, `"pinky"`, `"inky"`, `"clyde"`; `mode` is `"normal"`, `"frightened"`, or `"eaten"`. Return an `(r, g, b)` override, or `None` to keep the default. Idea: give each ghost a distinct frightened-mode tint instead of the shared blue/white flash.

### Task 3: Implement `on_pellet_eaten(score, pellets_left)`

> Called from `eat()` immediately after every pellet (regular or power) is removed from the board and the score updated. It receives the score after this pellet's points were added, and the number of pellets still remaining. Its return value is ignored. Idea: spawn a bonus fruit once `pellets_left` crosses a specific number, or flash the HUD on the final pellet.

### Task 4: Implement `bonus_life_threshold()`

> Called every frame in `update()`. It takes no arguments and should return an integer score value, or `None` to disable bonus lives entirely. Whenever the player's score crosses a multiple of that value for the first time, one life is awarded automatically — the surrounding bookkeeping (`self.bonus_awarded`) is already implemented, so you only need to choose or compute the threshold. Idea: return a fixed value like `10000`.

---

## Expected Behavior

- The player never passes through a wall and never re-collects an already-eaten pellet
- Pinky's target tile is 4 tiles ahead of the player, in the player's current direction of travel
- Clyde chases the player directly while far away, and retreats to his home corner once he gets close
- Eating a power pellet turns every non-eaten ghost frightened for a few seconds and reverses each ghost's direction once
- The game ends in a win when every pellet is eaten, or a loss when lives reach zero

---

## Folder Structure

```
pacman/
├── game.py
└── README.md
```

---

## Submission Checklist

Submission is only the following three things:

- [] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior
- [] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working
- [] The Chat/LLM used page link, with the complete chat history
