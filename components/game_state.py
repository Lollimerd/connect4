# game_state.py - Contains the GameState class to manage game logic

from utils.constants import PLAYING, PLAYER_1_WIN, PLAYER_2_WIN, TIE, PLAYER_1, PLAYER_2
from .board import Board
from connect4AI import AIPlayer


class GameState:
    def __init__(self, game_mode="pvp", ai_difficulty=2):
        """
        Initialize the game state.

        Args:
            game_mode: "pvp" for player vs player, "pvc" for player vs computer
            ai_difficulty: The AI difficulty level (1-3)
        """
        self.board = Board()
        self.current_player = PLAYER_1
        self.status = PLAYING
        self.game_over = False
        self.game_mode = game_mode

        # Initialize AI if in PvC mode
        self.ai_player = None
        if game_mode == "pvc":
            self.ai_player = AIPlayer(player_piece=PLAYER_2, difficulty=ai_difficulty)

    def switch_player(self):
        """Switch the current player."""
        self.current_player = PLAYER_2 if self.current_player == PLAYER_1 else PLAYER_1

    def make_move(self, col):
        """Process a player's move."""
        if self.game_over:
            return False

        if self.board.is_valid_location(col):
            row = self.board.get_next_open_row(col)
            if row is not None:
                self.board.drop_piece(row, col, self.current_player)

                # Check for win
                if self.board.is_winning_move(self.current_player):
                    self.status = PLAYER_1_WIN if self.current_player == PLAYER_1 else PLAYER_2_WIN
                    self.game_over = True
                # Check for tie
                elif self.board.is_full():
                    self.status = TIE
                    self.game_over = True
                else:
                    self.switch_player()

                return True
        return False

    def make_ai_move(self):
        """Make a move as the AI player."""
        if self.game_mode == "pvc" and self.current_player == PLAYER_2 and not self.game_over:
            col = self.ai_player.get_move(self.board)
            if col is not None:
                return self.make_move(col)
        return False

    def restart_game(self, game_mode=None, ai_difficulty=None):
        """
        Reset the game to start a new round.

        Args:
            game_mode: Optional new game mode
            ai_difficulty: Optional new AI difficulty level
        """
        self.board.reset()
        self.current_player = PLAYER_1
        self.status = PLAYING
        self.game_over = False

        # Update game mode and AI if specified
        if game_mode is not None:
            self.game_mode = game_mode

        if self.game_mode == "pvc":
            difficulty = ai_difficulty if ai_difficulty is not None else (
                self.ai_player.difficulty if self.ai_player else 2
            )
            self.ai_player = AIPlayer(player_piece=PLAYER_2, difficulty=difficulty)
        else:
            self.ai_player = None

    def get_board_grid(self):
        """Return the current board grid."""
        return self.board.grid