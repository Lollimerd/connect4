# renderer.py - Contains the Renderer class to handle all UI rendering

import pygame

from utils.constants import BLUE, BLACK, RED, YELLOW, PLAYER_1, PLAYER_2
from utils.constants import PLAYER_1_WIN, PLAYER_2_WIN, TIE
from utils.constants import WIDTH, HEIGHT, SQUARE_SIZE, RADIUS


class Renderer:
    def __init__(self, screen):
        """Initialize the renderer with the pygame screen."""
        self.screen = screen
        self.font = pygame.font.SysFont("monospace", 75)
        self.small_font = pygame.font.SysFont("monospace", 30)

    def draw_board(self, board_grid):
        """Draw the game board based on the current board state."""
        # Draw the blue board background
        for c in range(len(board_grid[0])):
            for r in range(len(board_grid)):
                pygame.draw.rect(self.screen, BLUE, (c * SQUARE_SIZE, (r + 1) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                pygame.draw.circle(self.screen, BLACK,
                                   (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                    int((r + 1) * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

        # Draw the pieces
        for c in range(len(board_grid[0])):
            for r in range(len(board_grid)):
                if board_grid[r][c] == PLAYER_1:
                    pygame.draw.circle(self.screen, RED,
                                       (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                        HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)
                elif board_grid[r][c] == PLAYER_2:
                    pygame.draw.circle(self.screen, YELLOW,
                                       (int(c * SQUARE_SIZE + SQUARE_SIZE / 2),
                                        HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

        pygame.display.update()

    def draw_piece_preview(self, x_pos, current_player):
        """Draw a preview of the piece at the top of the screen."""
        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
        color = RED if current_player == PLAYER_1 else YELLOW
        pygame.draw.circle(self.screen, color, (x_pos, int(SQUARE_SIZE / 2)), RADIUS)
        pygame.display.update()

    def clear_top_row(self):
        """Clear the top row where piece previews are shown."""
        pygame.draw.rect(self.screen, BLACK, (0, 0, WIDTH, SQUARE_SIZE))
        pygame.display.update()

    def draw_game_over_message(self, game_status):
        """Draw game over message based on the game status."""
        if game_status == PLAYER_1_WIN:
            label = self.font.render("Player 1 wins!!", 1, RED)
        elif game_status == PLAYER_2_WIN:
            label = self.font.render("Player 2 wins!!", 1, YELLOW)
        elif game_status == TIE:
            label = self.font.render("It's a tie!!", 1, BLUE)
        else:
            return

        self.screen.blit(label, (40, 10))
        pygame.display.update()

    def draw_player_turn_indicator(self, current_player, is_ai=False):
        """
        Draw an indicator showing whose turn it is.

        Args:
            current_player: The current player
            is_ai: Whether the current player is AI
        """
        color = RED if current_player == PLAYER_1 else YELLOW

        if is_ai:
            player_text = "AI's Turn"
        else:
            player_text = "Player 1" if current_player == PLAYER_1 else "Player 2"
            player_text += "'s Turn"

        # Draw at the bottom of the screen
        label = self.small_font.render(player_text, 1, color)
        pygame.draw.rect(self.screen, BLACK, (WIDTH - 200, HEIGHT - 40, 200, 40))
        self.screen.blit(label, (WIDTH - 190, HEIGHT - 35))
        pygame.display.update()

    def draw_difficulty_indicator(self, difficulty):
        """
        Draw the current AI difficulty level.

        Args:
            difficulty: The AI difficulty level (1-3)
        """
        if difficulty is None:
            return

        difficulty_text = "AI: "
        if difficulty == 1:
            difficulty_text += "Easy"
        elif difficulty == 2:
            difficulty_text += "Medium"
        else:
            difficulty_text += "Hard"

        label = self.small_font.render(difficulty_text, 1, BLUE)
        pygame.draw.rect(self.screen, BLACK, (10, HEIGHT - 40, 150, 40))
        self.screen.blit(label, (20, HEIGHT - 35))
        pygame.display.update()
