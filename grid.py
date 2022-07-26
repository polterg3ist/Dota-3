import random
import pygame
from cell import Cell


class Grid:
    def __init__(self, screen):
        self.screen = screen
        self.grid = []
        self.opened_cell = None
        self.identical_cells = []
        self.opened_cell = None

    def create_table(self):
        items = ["aegis", "agh", "crystal", "dagon", "desolator", "heart",
                 "manta", "midas", "rapier", "sak", "dragonlance", "satanic"] * 4
        random.shuffle(items)
        print(items)
        for line in range(8):
            for row in range(6):
                y = 100 * line + (5 * line) + 5
                x = 135 * row + (5 * row) + 5
                item = random.choice(items)
                print(f"LINE-{line} ROW-{row} ITEM-{item} X-{x} Y-{y}")
                cell = Cell(self.screen, items.pop(items.index(item)), x, y)
                self.grid.append(cell)
        self.close_grid()

    def update(self):
        for cell in self.grid:
            if cell.curtain_open and cell.curtain_pos > -130:
                cell.curtain_pos -= 1.5
            elif not cell.curtain_open and cell.curtain_pos < 0:
                cell.curtain_pos += 1.5
            cell.output()

        for cell in self.identical_cells:
            cell.output()

    def close_grid(self):
        for cell in self.grid:
            cell.curtain_open = False

    def click_on_grid(self, pos):
        print(f"event click on grid POS-{pos}")
        for ind, cell in enumerate(self.grid):
            rect = pygame.Rect(cell.x, cell.y, 130, 100)
            print(cell.rect)
            if rect.collidepoint(pos):
                if not cell.curtain_open:
                    if self.opened_cell:
                        cell.curtain_open = True
                        while cell.curtain_pos > -130:
                            self.update()
                            pygame.display.flip()
                        if self.opened_cell.item_name == cell.item_name:
                            self.grid.remove(cell)
                            self.grid.remove(self.opened_cell)
                            self.opened_cell = None
                        else:
                            cell.curtain_open = False
                            self.opened_cell.curtain_open = False
                            self.opened_cell = None
                    else:
                        cell.curtain_open = True
                        self.opened_cell = cell
                        while cell.curtain_pos > -130:
                            self.update()
                            pygame.display.flip()
                return

