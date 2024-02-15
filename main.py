import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame

pygame.init()
background_color = (128, 229, 175)
window_size = (900, 500)
game_font = pygame.font.Font("Freedom-10eM.ttf", 100)


def game(discs=4):
    pass

def mainMenu():
    pygame.display.set_caption("Hanoi Tower / Menu")
    screen = pygame.display.set_mode(window_size)
    bg = pygame.image.load("background.png")
    screen.blit(bg, (0, 0))
    menu_text = game_font.render("Main Menu", True, (255, 255, 255))
    shadow_menu_text = game_font.render("Main Menu", True, (0, 0, 0))
    screen.blit(shadow_menu_text, (window_size[0] // 2 - menu_text.get_width() // 2 - 7, 60))
    screen.blit(menu_text,(window_size[0] // 2 - menu_text.get_width() // 2, 60))

    pygame.display.flip()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

mainMenu()

