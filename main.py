import os
from sys import exit

import pygame
from resource_loader import load_font, load_image, load_sound

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("PixelRunner")
fps = pygame.time.Clock()
test_font = load_font('font/Pixeltype.ttf', 50)

# Utiliza la función load_image en lugar de pygame.image.load
sky_surface = load_image('graphics/sky.png').convert()
ground_surface = load_image('graphics/ground.png').convert()
text_surface = test_font.render('Mi juego', False, 'Black')

snail_surface = load_image('graphics/snail/snail1.png').convert_alpha()
snail_x_pos =  600

player_surface = load_image('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface,(300, 50))
    snail_x_pos -=4
    if snail_x_pos < -100: snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos, 250))
    screen.blit(player_surface,player_rect)


    pygame.display.update()
    fps.tick(60)
