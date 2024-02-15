import pygame


class Disc:
    def __init__(self, width, height, color):
        self.color = color
        self.width = width
        self.height = height

    def drawOnFirst(self, screen, listOfDiscs):
        self.rect = pygame.Rect(200-self.width//2, 400 - ((len(listOfDiscs)+1)*25), self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
        listOfDiscs.append((self.width, self.color))


    def drawOnSecond(self, screen, listOfDiscs):
        self.rect = pygame.Rect(200-self.width//2, 400 - ((len(listOfDiscs)+1)*25), self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
        listOfDiscs.append((self.width, self.color))

    def drawOnThird(self, screen, listOfDiscs):
        self.rect = pygame.Rect(200-self.width//2, 400 - ((len(listOfDiscs)+1)*25), self.width, self.height)
        pygame.draw.rect(screen, self.color, self.rect)
        listOfDiscs.append((self.width, self.color))

    def is_clicked(self, event):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1

