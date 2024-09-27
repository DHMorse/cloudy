import pygame

from vars import screen, BLACK

def draw_snake_game():
    # Set the screen background
    screen.fill(BLACK)
    # Draw the snake
    pygame.display.flip()

def handle_snake_game(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            print("UP")
        elif event.key == pygame.K_DOWN:
            print("DOWN")
        elif event.key == pygame.K_LEFT:
            print("LEFT")
        elif event.key == pygame.K_RIGHT:
            print("RIGHT")