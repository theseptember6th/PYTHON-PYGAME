"""
AUTHOR: KRISTAL SHRESTHA
DATE: 6/15/2024
PURPOSE: Snake game part 9 (length increment logic)
"""

import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
fps=30

font=pygame.font.SysFont(None,30)
clock=pygame.time.Clock()

def text_screen(text,color,x,y):
    screen_text=font.render(text,True,color)
    game_window.blit(screen_text,[x,y])

def plotSnake(gameWindow,color,snake_list,snake_size):
     for x,y in snake_list:
        pygame.draw.rect(game_window,color,[x,y,snake_size,snake_size])
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
snake_size=30
velocity_x=0
velocity_y=0
food_x=random.randint(0,int(screen_width/1.2))
food_y=random.randint(0,int(screen_height/1.2))
score=0
init_velocity=5
snake_list=[]
snake_length=1

# Main game loop
while not exit_game:
    for event in pygame.event.get():
        # Event handling
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                velocity_x=init_velocity
                velocity_y=0
               
            if event.key==pygame.K_LEFT:
                velocity_x=-init_velocity
                velocity_y=0
                
            if event.key==pygame.K_UP:
                velocity_y=-init_velocity
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=init_velocity
                velocity_x=0
                
    snake_x+=velocity_x
    snake_y+=velocity_y

    if abs(snake_x-food_x)<15 and abs(snake_y-food_y)<15:
        score+=1
        # print(f"score: {score*10}")
        #text_screen(f"score: {score*10}",red,5,5) #it is meaning less to write this here,because then the game window will be  completely filled white later line82
        food_x=random.randint(0,int(screen_width/1.2))
        food_y=random.randint(0,int(screen_height/1.2))
        snake_length+=5

    # Fill the game window with white color
    game_window.fill(white)
    text_screen(f"score: {score*10}",red,5,5)
    pygame.draw.rect(game_window,red,[food_x,food_y,snake_size,snake_size])

    head=[]
    head.append(snake_x)
    head.append(snake_y)
    snake_list.append(head)

    if len(snake_list)>snake_length:
        del snake_list[0]
    # pygame.draw.rect(game_window,black,[snake_x,snake_y,snake_size,snake_size])
    plotSnake(game_window,black,snake_list,snake_size)
    pygame.display.update()
    clock.tick(fps)

# Quit Pygame
pygame.quit()
quit()
