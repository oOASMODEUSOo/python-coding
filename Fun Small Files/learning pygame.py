import pygame

#initialising the game window
pygame.init()

screen_width, screen_height = 600,600

screen = pygame.display.set_mode((screen_width,screen_height))
running = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False