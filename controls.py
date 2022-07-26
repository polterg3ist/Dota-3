import pygame
from sys import exit as close_game


def events(grid):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()
        if grid.grid:
            if event.type == pygame.MOUSEBUTTONUP:
                grid.click_on_grid(event.pos)
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                grid.create_table()


def win_game(screen, background):
    screen.blit(background, (0, 0))
    font_first = pygame.font.SysFont('serif', 80)
    font_second = pygame.font.SysFont('Times New roman', 40)
    text_win = font_first.render('You Won', True, (0, 100, 55))
    text_play_again = font_second.render('Press R to play again', True, (189, 218, 87))
    screen_rect = screen.get_rect()
    place_win = text_win.get_rect(center=screen_rect.center)
    place_play_again = text_play_again.get_rect(center=(421, 473))
    screen.blit(text_win, place_win)
    screen.blit(text_play_again, place_play_again)
    pygame.display.flip()


def update(screen, grid, background):
    screen.blit(background, (0, 0))
    grid.update()
    pygame.display.flip()


