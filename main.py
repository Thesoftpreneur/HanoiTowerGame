import sys
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
from button import Button

import pygame

pygame.init()
background_color = (128, 229, 175)
window_size = (900, 500)
game_font = pygame.font.Font("Freedom-10eM.ttf", 100)
button_font = pygame.font.Font("Freedom-10eM.ttf", 30)


def game(discs=4):
    pass

def mainMenu():
    pygame.display.set_caption("Hanoi Tower / Menu")
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()


    while True:
        bg = pygame.image.load("background.png")
        screen.blit(bg, (0, 0))
        menu_text = game_font.render("Main Menu", True, (255, 255, 255))
        shadow_menu_text = game_font.render("Main Menu", True, (0, 0, 0))
        screen.blit(shadow_menu_text, (window_size[0] // 2 - menu_text.get_width() // 2 - 7, 60))
        screen.blit(menu_text, (window_size[0] // 2 - menu_text.get_width() // 2, 60))

        easy_button = Button(100, 250, 200, 100, "Easy", button_font, color=(132, 233, 133), hover_color=(73, 202, 77))
        medium_button = Button(350, 250, 200, 100, "Medium", button_font, color=(209, 212, 128), hover_color=(252, 109, 0))
        hard_button = Button(600, 250, 200, 100, "Hard", button_font, color=(216, 93, 89), hover_color=(199, 14, 8))
        mouse_pos = pygame.mouse.get_pos()


        easy_button.check_collision(mouse_pos)
        medium_button.check_collision(mouse_pos)
        hard_button.check_collision(mouse_pos)

        easy_button.draw(screen)
        medium_button.draw(screen)
        hard_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()
mainMenu()

