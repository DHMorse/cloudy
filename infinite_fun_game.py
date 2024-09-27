import pygame
import sys

from vars import *
from snake import draw_snake_game, handle_snake_game

# Initialize Pygame
pygame.init()

# Changed to from abitrary int's to strings so that when we use the switch statement, 
# the code is more readable and easier to understand.

# change this to be local later
pointer_pos = 0

game_state = MAIN_MENU

# Functions for the different menus
def draw_main_menu():
    global pointer_pos
    screen.fill(WHITE)
    title = font.render("Infinite Fun", True, BLACK)
    start = font.render("1. Start", True, BLACK)
    settings = font.render("2. Settings", True, BLACK)
    exit_game = font.render("3. Exit", True, BLACK)
    
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))
    screen.blit(start, (WIDTH // 2 - start.get_width() // 2, 200))
    screen.blit(settings, (WIDTH // 2 - settings.get_width() // 2, 300))
    screen.blit(exit_game, (WIDTH // 2 - exit_game.get_width() // 2, 400))

    match pointer_pos:
        case 0:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - start.get_width() // 2 - 20, 220), 5)
        case 1:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - settings.get_width() // 2 - 20, 320), 5)
        case 2:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - exit_game.get_width() // 2 - 20, 420), 5)

    pygame.display.flip()

def draw_settings_menu():
    global pointer_pos
    screen.fill(WHITE)
    speed_text = font.render(f"Game Speed: {game_speed:.1f}", True, BLACK)
    increase_speed = font.render("1. Increase Speed", True, BLACK)
    decrease_speed = font.render("2. Decrease Speed", True, BLACK)
    back = font.render("3. Back", True, BLACK)

    screen.blit(speed_text, (WIDTH // 2 - speed_text.get_width() // 2, 100))
    screen.blit(increase_speed, (WIDTH // 2 - increase_speed.get_width() // 2, 200))
    screen.blit(decrease_speed, (WIDTH // 2 - decrease_speed.get_width() // 2, 300))
    screen.blit(back, (WIDTH // 2 - back.get_width() // 2, 400))
    
    match pointer_pos:
        case 0:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - speed_text.get_width() // 2 - 20, 220), 5)
        case 1:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - increase_speed.get_width() // 2 - 20, 320), 5)
        case 2:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - decrease_speed.get_width() // 2 - 20, 420), 5)
        case 3:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - back.get_width() // 2 - 20, 520), 5)

    pygame.display.flip()

def draw_game_select_screen():
    global game_state, pointer_pos
    # Placeholder for actual game logic

    screen.fill(WHITE)
    target_shooter_text = font.render(f"1. Target Shooter", True, BLACK)
    snake_game_text = font.render("2. Snake Game", True, BLACK)
    cookie_clicker_text = font.render("3. Cookie Clicker", True, BLACK)
    chess_text = font.render("4. Chess Mini-Game", True, BLACK)
    apple_catcher_text = font.render("5. Apple Catcher", True, BLACK)
    tetris_text = font.render("6. Tetris", True, BLACK)
    minesweeper_text = font.render("7. Minesweeper", True, BLACK)
    back = font.render("8. Back", True, BLACK)

    screen.blit(target_shooter_text, (WIDTH // 2 - target_shooter_text.get_width() // 2, 100))
    screen.blit(snake_game_text, (WIDTH // 2 - snake_game_text.get_width() // 2, 150))
    screen.blit(cookie_clicker_text, (WIDTH // 2 - cookie_clicker_text.get_width() // 2, 200))
    screen.blit(chess_text, (WIDTH // 2 - chess_text.get_width() // 2, 250))
    screen.blit(apple_catcher_text, (WIDTH // 2 - apple_catcher_text.get_width() // 2, 300))
    screen.blit(tetris_text, (WIDTH // 2 - tetris_text.get_width() // 2, 350))
    screen.blit(minesweeper_text, (WIDTH // 2 - minesweeper_text.get_width() // 2, 400))
    screen.blit(back, (WIDTH // 2 - back.get_width() // 2, 450))

    match pointer_pos:
        case 0:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - target_shooter_text.get_width() // 2 - 20, 120), 5)
        case 1:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - snake_game_text.get_width() // 2 - 20, 170), 5)
        case 2:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - cookie_clicker_text.get_width() // 2 - 20, 220), 5)
        case 3:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - chess_text.get_width() // 2 - 20, 270), 5)
        case 4:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - apple_catcher_text.get_width() // 2 - 20, 320), 5)
        case 5:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - tetris_text.get_width() // 2 - 20, 370), 5)
        case 6:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - minesweeper_text.get_width() // 2 - 20, 420), 5)
        case 7:
            pygame.draw.circle(screen, BLACK, (WIDTH // 2 - back.get_width() // 2 - 20, 470), 5)

    pygame.display.flip()

    # Here you would rotate between the mini-games like:
    # 1. Target shooter
    # 2. Snake game
    # 3. Cookie clicker
    # 4. Chess mini-game
    # 5. Apple catcher, Tetris, Minesweeper, etc.
    
    # Temporary back to menu
    #game_state = MAIN_MENU

def handle_game_select_screen(event):
    global game_state, pointer_pos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            # Start target shooter
            pass
        elif event.key == pygame.K_2:
            # Start snake game
            game_state = SNAKE_GAME
        elif event.key == pygame.K_3:
            # Start cookie clicker
            pass
        elif event.key == pygame.K_4:
            # Start chess mini-game
            pass
        elif event.key == pygame.K_5:
            # Start apple catcher
            pass
        elif event.key == pygame.K_6:
            # Start tetris
            pass
        elif event.key == pygame.K_7:
            # Start minesweeper
            pass
        elif event.key == pygame.K_8:
            game_state = MAIN_MENU
        
        elif event.key == pygame.K_DOWN:
            pointer_pos = (pointer_pos + 1) % 8
        elif event.key == pygame.K_UP:
            pointer_pos = (pointer_pos - 1) % 8

        # This is pretty terrible and should be refactored
        elif event.key == pygame.K_RETURN:
            match pointer_pos:
                case 0:
                    # Start target shooter
                    pass
                case 1:
                    # Start snake game
                    game_state = SNAKE_GAME
                case 2:
                    # Start cookie clicker
                    pass
                case 3:
                    # Start chess mini-game
                    pass
                case 4:
                    # Start apple catcher
                    pass
                case 5:
                    # Start tetris
                    pass
                case 6:
                    # Start minesweeper
                    pass
                case 7:
                    game_state = MAIN_MENU

        # This is pretty terrible and should be refactored

def handle_main_menu_events(event):
    global game_state, pointer_pos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            game_state = START_GAME
        elif event.key == pygame.K_2:
            game_state = SETTINGS
        elif event.key == pygame.K_3:
            game_state = EXIT_GAME
        elif event.key == pygame.K_DOWN:
            pointer_pos = (pointer_pos + 1) % 3
        elif event.key == pygame.K_UP:
            pointer_pos = (pointer_pos - 1) % 3
        
        # This is pretty terrible and should be refactored
        elif event.key == pygame.K_RETURN:
            if pointer_pos == 0:
                game_state = START_GAME
            elif pointer_pos == 1:
                game_state = SETTINGS
            elif pointer_pos == 2:
                game_state = EXIT_GAME
        # This is pretty terrible and should be refactored

def handle_settings_menu_events(event):
    global game_speed, game_state, pointer_pos
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            game_speed += 0.1
        elif event.key == pygame.K_2:
            game_speed = max(0.1, game_speed - 0.1)
        elif event.key == pygame.K_3:
            game_state = MAIN_MENU

        elif event.key == pygame.K_DOWN:
            pointer_pos = (pointer_pos + 1) % 3
        elif event.key == pygame.K_UP:
            pointer_pos = (pointer_pos - 1) % 3

        # This is pretty terrible and should be refactored
        elif event.key == pygame.K_RETURN:
            if pointer_pos == 0:
                game_speed += 0.1
            elif pointer_pos == 1:
                game_speed = max(0.1, game_speed - 0.1)
            elif pointer_pos == 2:
                game_state = MAIN_MENU
        # This is pretty terrible and should be refactored

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # New code
        match game_state:
            case 'MAIN_MENU':
                handle_main_menu_events(event)
            case 'SETTINGS':
                handle_settings_menu_events(event)
            case 'START_GAME':
                handle_game_select_screen(event)
            case 'EXIT_GAME':
                pygame.quit()
                sys.exit()
            case 'SHOOTER_GAME':
                pass
            case 'SNAKE_GAME':
                handle_snake_game(event)
        # New code

        # Old code
        '''if game_state == MAIN_MENU:
            handle_main_menu_events(event)
        elif game_state == SETTINGS:
            handle_settings_menu_events(event)
        elif game_state == START_GAME:
            start_game_sequence()
        elif game_state == EXIT_GAME:
            pygame.quit()
            sys.exit()'''
        # Old code

    match game_state:
        case 'MAIN_MENU':
            draw_main_menu()
        case 'SETTINGS':
            draw_settings_menu()
        case 'START_GAME':
            draw_game_select_screen()
        case 'SHOOTER_GAME':
            pass
        case 'SNAKE_GAME':
            draw_snake_game()

pygame.quit()