import pygame


class Disc:
    def __init__(self, width, height, color):
        self.color = color
        self.width = width
        self.height = height
        self.x = 300
        self.y = 200
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def is_clicked(self, event):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1


    def getAbove(self, screen):
        rect1 = pygame.Rect(450 - self.width//2, 150, self.width, self.height)
        pygame.draw.rect(screen, self.color, rect1)



class Column:
    def __init__(self, x):
        self.discs = []
        self.x = x
        self.y = 400

    def rem(self):
        disc = self.discs[-1]
        self.discs.pop(-1)
        return disc

    def add(self, disc):
        self.discs.append(disc)

    def drawDiscs(self, screen):
        for i in range(len(self.discs)):
            self.discs[i].rect = pygame.Rect(self.x-self.discs[i].width//2, 375 - (i*25), self.discs[i].width, self.discs[i].height)
            pygame.draw.rect(screen, self.discs[i].color, self.discs[i].rect)



