# Chess in Python

A command-line 2-player chess game built with Python and Object-Oriented Programming (OOP) principles.

## Features

- **Full Chess Board Setup**: Standard starting position with White and Black pieces.
- **Piece Movements**:
  - Pawns (single step, starting 2-square step, diagonal captures, promotion to Queen)
  - Rooks, Bishops, Queens (sliding moves with collision detection)
  - Knights (L-shaped jumps)
  - King (one step in all directions)
- **Check and Checkmate**: Validates moves against check and detects checkmate/stalemate.
- **Turn-based CLI Gameplay**: Clear board display and move input in chess notation (e.g. `e2 e4`).

## How to Play

1. Make sure you have Python 3 installed.
2. Run the game from the terminal:
   ```bash
   python main.py
   ```
3. Enter your moves when prompted using starting square and destination square separated by space:
   ```text
   Player 1's turn (White): e2 e4
   Player 2's turn (Black): e7 e5
   ```
4. Type `quit` at any time to exit the game.
