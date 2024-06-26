"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/15/2024
PURPOSE: Snake game part 1
"""

import pygame

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

# Set up game window dimensions
screen_height = 400
screen_width = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

# Set game window title
pygame.display.set_caption("Snakes Kristal")

# Game variables
exit_game = False
game_over = False

# Main game loop
while not exit_game:
    for event in pygame.event.get():
        # Event handling
        if event.type == pygame.QUIT:
            exit_game = True
    
    # Fill the game window with white color
    game_window.fill(white)
    pygame.display.update()

# Quit Pygame
pygame.quit()
quit()
