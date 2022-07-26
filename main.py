import pygame
import controls
from grid import Grid
from random import randint


def main():
    pygame.init()
    FPS = 60
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((843, 847))
    pygame.display.set_caption("Dota 3")
    program_icon = pygame.image.load("img/icon/icon_1.jpg")
    pygame.display.set_icon(program_icon)
    backNo = randint(0, 3)
    background = pygame.image.load(f"img/back/back_{backNo}.jpg").convert()
    background = pygame.transform.smoothscale(background, screen.get_size())
    grid = Grid(screen)
    grid.create_table()

    while True:
        controls.events(grid)
        if grid.grid:
            clock.tick(FPS)
            controls.update(screen, grid, background)
        else:
            controls.win_game(screen, background)


if __name__ == "__main__":
    main()
