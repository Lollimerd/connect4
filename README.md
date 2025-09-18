# Connect 4 Game

This project is a Python implementation of the classic Connect 4 game using the Pygame library. It features a clean user interface, different game modes, and an AI opponent with adjustable difficulty levels.

-----

## 🎮 Game Features

  * **Player vs Player (PvP) Mode**: Play against a friend on the same computer.
  * **Player vs Computer (PvC) Mode**: Challenge an AI opponent with three difficulty settings.
  * **Real-time Piece Preview**: See a preview of your piece before dropping it.
  * **Game State Indicators**: The UI displays the current player's turn and the AI's difficulty level.
  * **Interactive Menu**: A simple menu to select the game mode and AI difficulty.

-----

## 📂 Project Structure

The project is organized into the following files and directories:

  * `main.py`: The main entry point for the game. It handles the game loop, event processing, and menu navigation.
  * `utils/constants.py`: Defines all the constant values used in the game, such as colors, board dimensions, and game states.
  * `components/board.py`: Contains the `Board` class, which manages the game board's state, including dropping pieces and checking for wins.
  * `components/game_state.py`: The `GameState` class manages the overall game logic, including switching players, making moves, and handling the game mode.
  * `connect4AI.py`: Implements the `AIPlayer` class, which uses the minimax algorithm with alpha-beta pruning to determine the AI's moves.
  * `components/renderer.py`: The `Renderer` class is responsible for all the visual aspects of the game, such as drawing the board, pieces, and text.

-----

## ⚙️ Installation and Setup

### Prerequisites

  * Python 3.x
  * Pygame
  * NumPy

### Installation Steps

1.  **Install Python 3.x** from the [official website](https://www.python.org/downloads/).

2.  **Install the required libraries** by running the following command in your terminal:

    ```bash
    pip install pygame numpy
    ```

3.  **Download the project files** and place them in the same directory.

4.  **Run the game** with the following command:

    ```bash
    python main.py
    ```

-----

## 🕹️ Game Controls

  * **Mouse Movement**: Move the mouse to position the piece preview at the top of the board.
  * **Left Mouse Click**: Click to drop your piece into the selected column.
  * **'R' Key or 'ESC' Key**: Press either key to restart the game and return to the main menu.

-----

## 🎲 Game Modes

### Player vs Player

In this mode, two players take turns dropping their pieces into the board. Player 1 uses red pieces, and Player 2 uses yellow pieces. The first player to get four of their pieces in a row (horizontally, vertically, or diagonally) wins.

### Player vs Computer

Challenge the AI opponent in this mode. The player is Player 1 (red), and the AI is Player 2 (yellow). There are three difficulty levels:

  * **Easy**: The AI uses a minimax search with a depth of 1 and has a 30% chance of making a random move.
  * **Medium**: The AI uses a minimax search with a depth of 3 and no randomness.
  * **Hard**: The AI uses a minimax search with a depth of 5 and no randomness.

-----

## 🤖 AI Implementation

The AI opponent uses the **minimax algorithm** with **alpha-beta pruning** to find the optimal move.

  * **Evaluation Function**: The AI evaluates the board by scoring "windows" of four slots. It prioritizes creating its own winning lines, blocking the opponent's winning moves, and controlling the center of the board.
  * **Alpha-Beta Pruning**: This optimization helps to reduce the number of nodes the minimax algorithm needs to evaluate, allowing for a deeper search in a shorter amount of time.

-----

## 🛠️ Technical Details

### Board Representation

The game board is represented as a 6x7 NumPy array.

  * `0`: Represents an empty slot.
  * `1`: Represents a piece from Player 1.
  * `2`: Represents a piece from Player 2.

### Win Detection

The `is_winning_move` function in the `Board` class checks for four consecutive pieces in all four possible directions: horizontal, vertical, and both diagonal directions.

### UI Rendering

All the rendering is handled by the `Renderer` class using the Pygame library.

  * The game board is drawn as a blue grid with black circles for the empty slots.
  * Player pieces are rendered as red and yellow circles.

-----

## 🚀 Future Enhancements

  * **Animations**: Add smooth animations for pieces dropping into the board.
  * **Sound Effects**: Incorporate sound effects for piece drops and wins.
  * **Score Tracking**: Implement a scoring system to keep track of wins and losses.
  * **Networked Multiplayer**: Add the ability to play against another person over a network.