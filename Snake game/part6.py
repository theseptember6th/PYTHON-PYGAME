"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/15/2024
PURPOSE: Snake game part 6 (movement solved)
"""

import pygame

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
fps=30

clock=pygame.time.Clock()


# Set up game window dimensions
screen_height = 400
screen_width = 600
game_window = pygame.display.set_mode((screen_width, screen_height))

# Set game window title
pygame.display.set_caption("Snakes Kristal")

# Game variables
exit_game = False
game_over = False
snake_x=45
snake_y=55
snake_size=10
velocity_x=0
velocity_y=0

# Main game loop
while not exit_game:
    for event in pygame.event.get():
        # Event handling
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0
               
            if event.key==pygame.K_LEFT:
                velocity_x=-10
                velocity_y=0
                
            if event.key==pygame.K_UP:
                velocity_y=-10
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=10
                velocity_x=0
                
    snake_x+=velocity_x
    snake_y+=velocity_y
    # Fill the game window with white color
    game_window.fill(white)
    pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)

# Quit Pygame
pygame.quit()
quit()
