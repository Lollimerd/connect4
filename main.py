# main.py - Main entry point for the Connect 4 game

import pygame
import sys
from utils.constants import *
from components.game_state import GameState
from components.renderer import Renderer


def show_menu(screen, menu_font, button_font):
    """
    Show a menu to select game mode and difficulty.

    Returns:
        Tuple of (game_mode, ai_difficulty)
    """
    screen.fill(BLACK)

    # Draw title
    title = menu_font.render("Connect 4", True, BLUE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))

    # Draw game mode options
    mode_text = menu_font.render("Select Game Mode:", True, (255, 255, 255))
    screen.blit(mode_text, (WIDTH // 2 - mode_text.get_width() // 2, 150))

    # PvP Button
    pvp_rect = pygame.Rect(WIDTH // 2 - 150, 220, 300, 50)
    pygame.draw.rect(screen, BLUE, pvp_rect)
    pvp_text = button_font.render("Player vs Player", True, (255, 255, 255))
    screen.blit(pvp_text, (WIDTH // 2 - pvp_text.get_width() // 2, 235))

    # PvC Button
    pvc_rect = pygame.Rect(WIDTH // 2 - 150, 290, 300, 50)
    pygame.draw.rect(screen, BLUE, pvc_rect)
    pvc_text = button_font.render("Player vs Computer", True, (255, 255, 255))
    screen.blit(pvc_text, (WIDTH // 2 - pvc_text.get_width() // 2, 305))

    # Prepare difficulty options (initially hidden)
    difficulty_text = menu_font.render("Select Difficulty:", True, (255, 255, 255))

    # Better spacing for difficulty buttons - more horizontal space between them
    easy_rect = pygame.Rect(WIDTH // 2 - 275, 450, 150, 50)
    medium_rect = pygame.Rect(WIDTH // 2 - 75, 450, 150, 50)
    hard_rect = pygame.Rect(WIDTH // 2 + 125, 450, 150, 50)

    difficulty_visible = False

    pygame.display.update()

    # Menu loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Check if a game mode was selected
                if pvp_rect.collidepoint(mouse_pos):
                    return "pvp", None

                elif pvc_rect.collidepoint(mouse_pos):
                    # Show difficulty options
                    difficulty_visible = True

                    # Clear the area below the buttons to avoid overlapping text
                    pygame.draw.rect(screen, BLACK, (0, 360, WIDTH, HEIGHT - 360))

                    # Display the difficulty text with more vertical space
                    screen.blit(difficulty_text, (WIDTH // 2 - difficulty_text.get_width() // 2, 380))

                    # Draw difficulty buttons
                    pygame.draw.rect(screen, RED, easy_rect)
                    easy_text = button_font.render("Easy", True, (255, 255, 255))
                    screen.blit(easy_text, (easy_rect.centerx - easy_text.get_width() // 2,
                                            easy_rect.centery - easy_text.get_height() // 2))

                    pygame.draw.rect(screen, YELLOW, medium_rect)
                    medium_text = button_font.render("Medium", True, (255, 255, 255))
                    screen.blit(medium_text, (medium_rect.centerx - medium_text.get_width() // 2,
                                              medium_rect.centery - medium_text.get_height() // 2))

                    pygame.draw.rect(screen, RED, hard_rect)
                    hard_text = button_font.render("Hard", True, (255, 255, 255))
                    screen.blit(hard_text, (hard_rect.centerx - hard_text.get_width() // 2,
                                            hard_rect.centery - hard_text.get_height() // 2))

                    pygame.display.update()

                # Check if a difficulty was selected
                elif difficulty_visible:
                    if easy_rect.collidepoint(mouse_pos):
                        return "pvc", 1
                    elif medium_rect.collidepoint(mouse_pos):
                        return "pvc", 2
                    elif hard_rect.collidepoint(mouse_pos):
                        return "pvc", 3


def main():
    # Initialize pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Connect 4')

    # Initialize fonts
    menu_font = pygame.font.SysFont("Arial", 36)
    button_font = pygame.font.SysFont("Arial", 24)

    # Initialize renderer
    renderer = Renderer(screen)

    # Show menu
    game_mode, ai_difficulty = show_menu(screen, menu_font, button_font)

    # Initialize game state with selected mode
    gamestate = GameState(game_mode=game_mode, ai_difficulty=ai_difficulty)

    # Draw initial board
    renderer.draw_board(gamestate.get_board_grid())
    renderer.draw_player_turn_indicator(gamestate.current_player,
                                        is_ai=(gamestate.game_mode == "pvc" and gamestate.current_player == PLAYER_2))
    if gamestate.game_mode == "pvc":
        renderer.draw_difficulty_indicator(ai_difficulty)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Show piece preview during mouse movement (only for human players)
            if event.type == pygame.MOUSEMOTION and (gamestate.current_player == PLAYER_1 or gamestate.game_mode == "pvp"):
                x_pos = event.pos[0]
                renderer.draw_piece_preview(x_pos, gamestate.current_player)
                renderer.draw_player_turn_indicator(gamestate.current_player,
                                                    is_ai=(gamestate.game_mode == "pvc" and gamestate.current_player == PLAYER_2))

            # Process player moves (only for human players)
            if event.type == pygame.MOUSEBUTTONDOWN and (gamestate.current_player == PLAYER_1 or gamestate.game_mode == "pvp"):
                # Clear the top row
                renderer.clear_top_row()

                # Get the column from mouse position
                x_pos = event.pos[0]
                col = int(x_pos // SQUARE_SIZE)

                # Make the move
                if gamestate.make_move(col):
                    renderer.draw_board(gamestate.get_board_grid())

                    # Check for game over
                    if gamestate.status != PLAYING:
                        renderer.draw_game_over_message(gamestate.status)
                        pygame.time.wait(3000)

                        # Show menu again
                        game_mode, ai_difficulty = show_menu(screen, menu_font, button_font)
                        gamestate.restart_game(game_mode=game_mode, ai_difficulty=ai_difficulty)
                        renderer.draw_board(gamestate.get_board_grid())
                        if gamestate.game_mode == "pvc":
                            renderer.draw_difficulty_indicator(ai_difficulty)

                    # If it's the AI's turn
                    if gamestate.game_mode == "pvc" and gamestate.current_player == PLAYER_2:
                        renderer.draw_player_turn_indicator(gamestate.current_player, is_ai=True)
                        pygame.display.update()
                        pygame.time.wait(500)  # Small delay to make AI move visible

                        gamestate.make_ai_move()
                        renderer.draw_board(gamestate.get_board_grid())

                        # Check for game over after AI move
                        if gamestate.status != PLAYING:
                            renderer.draw_game_over_message(gamestate.status)
                            pygame.time.wait(3000)
                            # Show menu again
                            game_mode, ai_difficulty = show_menu(screen, menu_font, button_font)
                            gamestate.restart_game(game_mode=game_mode, ai_difficulty=ai_difficulty)
                            renderer.draw_board(gamestate.get_board_grid())
                            if gamestate.game_mode == "pvc":
                                renderer.draw_difficulty_indicator(ai_difficulty)

                    renderer.draw_player_turn_indicator(gamestate.current_player,
                                                        is_ai=(gamestate.game_mode == "pvc" and
                                                               gamestate.current_player == PLAYER_2))

            # Allow pressing 'r' to restart the game or ESC to show menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r or event.key == pygame.K_ESCAPE:
                    # Show menu again
                    game_mode, ai_difficulty = show_menu(screen, menu_font, button_font)
                    gamestate.restart_game(game_mode=game_mode, ai_difficulty=ai_difficulty)
                    renderer.draw_board(gamestate.get_board_grid())
                    renderer.draw_player_turn_indicator(gamestate.current_player,
                                                        is_ai=(gamestate.game_mode == "pvc" and
                                                               gamestate.current_player == PLAYER_2))
                    if gamestate.game_mode == "pvc":
                        renderer.draw_difficulty_indicator(ai_difficulty)


if __name__ == "__main__":
    main()