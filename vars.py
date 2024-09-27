import pygame

# Initialize Pygame
pygame.init()

# Font
font = pygame.font.SysFont('Arial', 30)

# Game speed
game_speed = 1.0

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Infinite Fun")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game states
#MAIN_MENU, SETTINGS, START_GAME, EXIT_GAME = 0, 1, 2, 3
MAIN_MENU, SETTINGS, START_GAME, EXIT_GAME = 'MAIN_MENU', 'SETTINGS', 'START_GAME', 'EXIT_GAME' 
TARGET_SHOOTER, SNAKE_GAME, COOKIE_CLICKER, CHESS, APPLE_CATCHER, TETRIS, MINESWEEPER = 'TARGET_SHOOTER', 'SNAKE_GAME', 'COOKIE_CLICKER', 'CHESS', 'APPLE_CATCHER', 'TETRIS', 'MINESWEEPER'
