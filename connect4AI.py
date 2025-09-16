# ai_player.py - Contains AI player implementation using minimax algorithm

import numpy as np
import random
from utils.constants import EMPTY, PLAYER_1, PLAYER_2, COLUMN_COUNT, ROW_COUNT


class AIPlayer:
    def __init__(self, player_piece=PLAYER_2, difficulty=2):
        """
        Initialize the AI player.

        Args:
            player_piece: The piece representing the AI (default: PLAYER_2)
            difficulty: The difficulty level (1-3)
                1 = Easy (depth 1, with randomness)
                2 = Medium (depth 3)
                3 = Hard (depth 5)
        """
        self.player_piece = player_piece
        self.opponent_piece = PLAYER_1 if player_piece == PLAYER_2 else PLAYER_2
        self.difficulty = difficulty

        # Set the search depth based on difficulty
        if difficulty == 1:  # Easy
            self.depth = 1
            self.randomness = 0.3  # 30% chance to make a random move

        elif difficulty == 2:  # Medium
            self.depth = 3
            self.randomness = 0.0

        else:  # Hard
            self.depth = 5
            self.randomness = 0.0

    def get_move(self, board):
        """
        Get the best move for the AI player.
        Args:
            board: The game board instance
        Returns:
            The column to place the piece
        """
        # Sometimes make a random move (for easier difficulties)
        if random.random() < self.randomness:
            valid_columns = [col for col in range(COLUMN_COUNT) if board.is_valid_location(col)]
            if valid_columns:
                return random.choice(valid_columns)

        # Get the best move using minimax
        board_copy = np.copy(board.grid)
        valid_locations = [col for col in range(COLUMN_COUNT) if board.is_valid_location(col)]

        if not valid_locations:
            return None

        best_score = -float('inf')
        best_col = random.choice(valid_locations)

        # Try each valid column and choose the best one
        for col in valid_locations:
            row = board.get_next_open_row(col)
            temp_board = np.copy(board_copy)
            self._drop_piece(temp_board, row, col, self.player_piece)

            score = self._minimax(temp_board, self.depth, -float('inf'), float('inf'), False)

            if score > best_score:
                best_score = score
                best_col = col

        return best_col

    def _drop_piece(self, board, row, col, piece):
        """Helper to drop a piece in the board array."""
        board[row][col] = piece

    def _is_winning_move(self, board, piece):
        """Check if the current board state has a win for the given piece."""
        # Check horizontal locations
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT):
                if (board[r][c] == piece and
                        board[r][c + 1] == piece and
                        board[r][c + 2] == piece and
                        board[r][c + 3] == piece):
                    return True

        # Check vertical locations
        for c in range(COLUMN_COUNT):
            for r in range(ROW_COUNT - 3):
                if (board[r][c] == piece and
                        board[r + 1][c] == piece and
                        board[r + 2][c] == piece and
                        board[r + 3][c] == piece):
                    return True

        # Check positively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(ROW_COUNT - 3):
                if (board[r][c] == piece and
                        board[r + 1][c + 1] == piece and
                        board[r + 2][c + 2] == piece and
                        board[r + 3][c + 3] == piece):
                    return True

        # Check negatively sloped diagonals
        for c in range(COLUMN_COUNT - 3):
            for r in range(3, ROW_COUNT):
                if (board[r][c] == piece and
                        board[r - 1][c + 1] == piece and
                        board[r - 2][c + 2] == piece and
                        board[r - 3][c + 3] == piece):
                    return True

        return False

    def _get_next_open_row(self, board, col):
        """Get the next open row in a column for the temporary board."""
        for r in range(ROW_COUNT):
            if board[r][col] == EMPTY:
                return r
        return None

    def _evaluate_window(self, window, piece):
        """
        Score a window of 4 pieces.

        Args:
            window: Array of 4 board positions
            piece: The piece to evaluate for

        Returns:
            Score for the window
        """
        opponent_piece = self.opponent_piece if piece == self.player_piece else self.player_piece

        # Count pieces
        score = 0
        piece_count = np.count_nonzero(window == piece)
        empty_count = np.count_nonzero(window == EMPTY)
        opponent_count = np.count_nonzero(window == opponent_piece)

        # Score the window based on its contents
        if piece_count == 4:
            score += 100  # Win
        elif piece_count == 3 and empty_count == 1:
            score += 5  # 3 in a row
        elif piece_count == 2 and empty_count == 2:
            score += 2  # 2 in a row

        # Penalize opponent's potential wins
        if opponent_count == 3 and empty_count == 1:
            score -= 4  # Block opponent's 3 in a row

        return score

    def _score_position(self, board, piece):
        """
        Score the entire board position for the given piece.
        Args:
            board: The board to evaluate
            piece: The piece to evaluate for
        Returns:
            The score for the position
        """
        score = 0

        # Score center column (preferable to control the center)
        center_array = [board[r][COLUMN_COUNT // 2] for r in range(ROW_COUNT)]
        center_count = np.count_nonzero(np.array(center_array) == piece)
        score += center_count * 3

        # Score horizontal windows
        for r in range(ROW_COUNT):
            row_array = board[r]
            for c in range(COLUMN_COUNT - 3):
                window = row_array[c:c + 4]
                score += self._evaluate_window(window, piece)

        # Score vertical windows
        for c in range(COLUMN_COUNT):
            col_array = [board[r][c] for r in range(ROW_COUNT)]
            for r in range(ROW_COUNT - 3):
                window = col_array[r:r + 4]
                score += self._evaluate_window(window, piece)

        # Score positively sloped diagonal windows
        for r in range(ROW_COUNT - 3):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self._evaluate_window(window, piece)

        # Score negatively sloped diagonal windows
        for r in range(3, ROW_COUNT):
            for c in range(COLUMN_COUNT - 3):
                window = [board[r - i][c + i] for i in range(4)]
                score += self._evaluate_window(window, piece)

        return score

    def _is_terminal_node(self, board):
        """Check if the board is in a terminal state (win or full)."""
        return (self._is_winning_move(board, self.player_piece) or
                self._is_winning_move(board, self.opponent_piece) or
                len([c for c in range(COLUMN_COUNT) if board[ROW_COUNT - 1][c] == EMPTY]) == 0)

    def _minimax(self, board, depth, alpha, beta, maximizing_player):
        """
        Minimax algorithm with alpha-beta pruning.
        Args:
            board: The current board state
            depth: How many moves to look ahead
            alpha: Alpha value for pruning
            beta: Beta value for pruning
            maximizing_player: Whether it's the maximizing player's turn
        Returns:
            The best score for the current position
        """
        # Terminal node or max depth reached
        if depth == 0 or self._is_terminal_node(board):
            if self._is_winning_move(board, self.player_piece):
                return 1000000  # AI wins
            elif self._is_winning_move(board, self.opponent_piece):
                return -1000000  # Opponent wins
            elif len([c for c in range(COLUMN_COUNT) if board[ROW_COUNT - 1][c] == EMPTY]) == 0:
                return 0  # Draw
            else:
                # Evaluate the board for the AI player
                return self._score_position(board, self.player_piece)

        valid_locations = [c for c in range(COLUMN_COUNT) if board[ROW_COUNT - 1][c] == EMPTY]

        if maximizing_player:
            value = -float('inf')
            for col in valid_locations:
                row = self._get_next_open_row(board, col)
                if row is not None:
                    board_copy = np.copy(board)
                    self._drop_piece(board_copy, row, col, self.player_piece)
                    new_score = self._minimax(board_copy, depth - 1, alpha, beta, False)
                    value = max(value, new_score)
                    alpha = max(alpha, value)
                    if alpha >= beta:
                        break  # Beta cutoff
            return value

        else:  # Minimizing player
            value = float('inf')
            for col in valid_locations:
                row = self._get_next_open_row(board, col)
                if row is not None:
                    board_copy = np.copy(board)
                    self._drop_piece(board_copy, row, col, self.opponent_piece)
                    new_score = self._minimax(board_copy, depth - 1, alpha, beta, True)
                    value = min(value, new_score)
                    beta = min(beta, value)
                    if alpha >= beta:
                        break  # Alpha cutoff
            return value