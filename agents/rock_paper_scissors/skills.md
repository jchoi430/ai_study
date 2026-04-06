---
name: rock_paper_scissors
description: >-
  Play rock, paper, scissors with the user.
  The user will provide their choice (rock, paper, or scissors) and the agent will respond with its choice.
  The user will provide 1, 2, or 3 to represent rock, paper, or scissors respectively.
  The agent will determine the winner based on the rules of rock, paper, scissors.
  The agent will keep track of the score and the winner.
  The agent will respond with the winner and the score.
---


# Game Development Starter Skill

## Goal
Help the AI generate a clean, efficient architecture for the Rock, Paper, Scissors game.

### Architecture Requirements
- **Models (`models.py`):** Use a polymorphic design pattern for the shape objects to determine win conditions. Include a `Score` class to retain history and round results.
- **Graphics (`board.py`):** Abstract display rendering, window dimensions, and fonts into a dedicated `Board` class.
- **Application (`main.py`):** Maintain the 60 FPS clock event loop to process integer-based keyboard inputs and delegate rendering execution to the `Board`.

## Rules & Conventions
- The game is played between the user and the computer.
- **Language:** Python.
- **Engine:** Use `pygame-ce` (Community Edition fork) for UI rendering.
- **Input:** Use event listeners for numeric keyboard inputs. `1`, `2`, `3` for Rock, Paper, Scissors respectively, and `0` for quit.
