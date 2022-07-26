import pygame


class Cell:
    def __init__(self, screen, item, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.cell = pygame.Surface((130, 100))
        self.curtain = pygame.Surface((130, 100))
        self.curtain_pos = -130
        self.curtain_open = True
        self.item = pygame.image.load(f"img/item/item_{item}.jpg").convert()
        self.item = pygame.transform.smoothscale(self.item, (135, 100))
        self.item_name = item
        self.rect = self.cell.get_rect()

    def output(self):
        self.screen.blit(self.cell, (self.x, self.y))
        self.cell.blit(self.item, (0, 0))
        self.cell.blit(self.curtain, (self.curtain_pos, 0))
