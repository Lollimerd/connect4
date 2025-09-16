# board.py - Contains the Board class to manage the game board

import numpy as np
from utils.constants import ROW_COUNT, COLUMN_COUNT, EMPTY


class Board:
    def __init__(self):
        """Initialize a new Connect 4 board 6x7"""
        self.grid = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)

    def is_valid_location(self, col):
        """Check if a column is valid for dropping a piece."""
        return 0 <= col < COLUMN_COUNT and self.grid[ROW_COUNT - 1][col] == EMPTY

    def get_next_open_row(self, col):
        """Get the next open row in a column."""
        for r in range(ROW_COUNT):
            if self.grid[r][col] == EMPTY:
                return r
        return None

    def drop_piece(self, row, col, piece):
        """Drop a piece in the selected column."""
        self.grid[row][col] = piece

    def is_winning_move(self, piece):
        """Check if the current player has won."""
        # Check horizontal locations
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if (self.grid[r][c] == piece and
                        self.grid[r][c + 1] == piece and
                        self.grid[r][c + 2] == piece and
                        self.grid[r][c + 3] == piece):
                    return True

        # Check vertical locations
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if (self.grid[r][c] == piece and
                        self.grid[r + 1][c] == piece and
                        self.grid[r + 2][c] == piece and
                        self.grid[r + 3][c] == piece):
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (self.grid[r][c] == piece and
                        self.grid[r + 1][c + 1] == piece and
                        self.grid[r + 2][c + 2] == piece and
                        self.grid[r + 3][c + 3] == piece):
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (self.grid[r][c] == piece and
                        self.grid[r - 1][c + 1] == piece and
                        self.grid[r - 2][c + 2] == piece and
                        self.grid[r - 3][c + 3] == piece):
                    return True

        return False

    def is_full(self):
        """Check if the board is full (tie game)."""
        return not any(EMPTY in row for row in self.grid)

    def reset(self):
        """Reset the board to an empty state."""
        self.grid = np.zeros((ROW_COUNT, COLUMN_COUNT), dtype=int)