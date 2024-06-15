"""
AUTHOR:KRISTAL SHRESTHA
DATE:6/15/2024
PURPOSE:Pygame starting basics
"""

import pygame

# Initialize pygame modules
pygame.init()

# Create the game window
game_window = pygame.display.set_mode((1200, 500))

# Set the game window title
pygame.display.set_caption("KRISTAL'S GAME")

# Game-specific variables
exit_game = False  # Flag to keep track if the game should exit
game_over = False  # Flag to indicate if the game is over (currently unused)

# Main game loop
while not exit_game:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True  # Exit the game if the user closes the window

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have pressed the right arrow key")  # Example action for right arrow key

# Quit pygame properly
pygame.quit()
quit()  # Exit the Python interpreter
