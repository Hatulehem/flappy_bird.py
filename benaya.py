import pygame
import random

def draw_floor():
    screen.blit(floor, (floor_x,floor_y))
    screen.blit(floor, (floor_x+ 448,floor_y))

pygame.init()

#screen size
WINDOW_W = 420
WINDOW_H = 420
WINDOW_SIZE = (WINDOW_W,WINDOW_H)

screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Flappy Bird")

#images/variables
clock = pygame.time.Clock()

bk = pygame.image.load("background.png")

#floor
floor = pygame.image.load("floor.png")
floor_x = 0
floor_y = 368

#bird
white = (255,255,255)
bird = pygame.image.load("bird.png")
# bird.set_colorkey(white)
# bird(white).convert_alpha()
bird_rect = bird.get_rect(center=(50,WINDOW_H//2))


# bird = 
#loop
play = True

while play:
    clock.tick(130)

     #images that will appeer
    screen.blit(bk , (0,0))
    screen.blit(floor, (floor_x,floor_y))
    screen.blit(bird, bird_rect)
    floor_x -=1
    draw_floor()
    if floor_x < -448:
        floor_x = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False   


    pygame.display.update()

pygame.quit()