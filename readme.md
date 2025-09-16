# Connect 4 Game Documentation

## Table of Contents {#toc}
1. [Project Overview](#project-overview)
2. [Project Structure](#project-structure)
3. [Game Features](#game-features)
4. [Installation and Setup](#installation-and-setup)
5. [Game Controls](#game-controls)
6. [Game Modes](#game-modes)
7. [AI Implementation](#ai-implementation)
8. [Technical Details](#technical-details)
9. [Future Enhancements](#future-enhancements)

## Project Overview [↑](#toc)

This is a Python implementation of the classic Connect 4 game using the Pygame library. The game allows players to play against each other or against an AI with varying difficulty levels. The project follows object-oriented design principles, separating game logic, rendering, and AI components.

## Project Structure [↑](#toc)

The project consists of several Python files, each handling different aspects of the game:

- **main.py**: The entry point of the application that initializes the game and contains the main game loop.
- **constants.py**: Defines all game constants such as board dimensions, colors, and game states.
- **board.py**: Contains the `Board` class which manages the game board and its state.
- **game_state.py**: Contains the `GameState` class which manages the overall game logic.
- **connect4AI.py**: Contains the `AIPlayer` class which implements the minimax algorithm for the AI opponent.
- **renderer.py**: Contains the `Renderer` class which handles all UI rendering and display aspects.

## Game Features [↑](#toc)

- Player vs Player mode
- Player vs Computer mode with three different AI difficulty levels
- Clean and intuitive user interface
- Real-time piece placement preview
- Game state indicators (current player, AI difficulty)
- Menu system for selecting game modes and difficulty

## Installation and Setup [↑](#toc)

### Prerequisites
- Python 3.x
- Pygame library
- NumPy library

### Installation Steps

1. **Install Python 3.x** from [python.org](https://www.python.org/downloads/)

2. **Install required libraries**:
   ```
   pip install pygame numpy
   ```

3. **Clone/download the project files** and ensure all files are in the same directory

4. **Run the game**:
   ```
   python main.py
   ```

## Game Controls [↑](#toc)

- **Mouse Movement**: Move the piece preview across the top of the board
- **Left Mouse Click**: Drop a piece in the selected column
- **R Key**: Restart the game and return to the menu
- **ESC Key**: Return to the main menu at any time

## Game Modes [↑](#toc)

### Player vs Player
Two players take turns dropping pieces. Red pieces belong to Player 1, and yellow pieces belong to Player 2.

### Player vs Computer
Play against an AI opponent with three difficulty settings:

1. **Easy**: The AI uses minimax with depth 1 and has a 30% chance to make a random move.
2. **Medium**: The AI uses minimax with depth 3 and no randomness.
3. **Hard**: The AI uses minimax with depth 5 and no randomness.

## AI Implementation [↑](#toc)

The AI uses the minimax algorithm with alpha-beta pruning to determine the best move:

- **Evaluation Function**: The AI evaluates board positions by scoring windows of 4 adjacent spots. It prioritizes:
  - Center column control
  - Connecting three or four pieces in a row
  - Blocking the opponent's potential winning moves

- **Alpha-Beta Pruning**: This optimization technique reduces the number of nodes evaluated in the minimax algorithm, allowing for deeper searches.

- **Difficulty Levels**: The difficulty of the AI is controlled by adjusting the search depth and adding randomness to easier levels.

## Technical Details [↑](#toc)

### Board Representation
- The game board is represented as a 6x7 NumPy array.
- Empty spaces are represented by 0, Player 1's pieces by 1, and Player 2's pieces by 2.
- The board is indexed with (0,0) at the bottom-left.

### Win Detection
The game checks for four consecutive pieces in four directions:
- Horizontal rows
- Vertical columns
- Positive-sloping diagonals (↗)
- Negative-sloping diagonals (↘)

### UI Rendering
The UI rendering is handled by the Pygame library:
- The board is drawn as blue rectangles with circular holes.
- Pieces are drawn as red (Player 1) or yellow (Player 2) circles.
- The top row shows a preview of where the piece will be placed.

## Future Enhancements [↑](#toc)

Potential future improvements for the game could include:

1. Adding sound effects and background music
2. Implementing a scoring/stats system
3. Adding animation for dropping pieces
4. Creating a networked multiplayer mode
5. Developing a more sophisticated AI using techniques beyond the minimax algorithm
6. Adding different board sizes or game variations
7. Creating a level-based campaign mode
8. Adding undo/redo functionality
9. Implementing save/load game features

---

This documentation was created on April 26, 2025.

---

[Back to Top](#toc)