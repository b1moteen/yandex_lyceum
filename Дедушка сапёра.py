import pygame
import random
from Board import Board

FPS = 30


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.plus = 1

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == -1:
                    pygame.draw.rect(screen, "white", (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                     2)
                elif self.board[y][x] == 10:
                    pygame.draw.rect(screen, "red", (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                     0)
                elif self.board[y][x] != 10 and self.board[y][x] != -1:
                    cell_mine = self.board[y][x]
                    font = pygame.font.Font(None, 50)
                    text = font.render(str(cell_mine), True, (100, 255, 100))
                    text_x = self.left + x * self.cell_size + 5
                    text_y = self.top + y * self.cell_size + 5
                    screen.blit(text, (text_x, text_y))
                    pygame.draw.rect(screen, "white", (
                        self.left + x * self.cell_size, self.top + y * self.cell_size, self.cell_size, self.cell_size),
                                     2)

    def get_cell(self, mouse_pos):
        mouse_pos_x, mouse_pos_y = mouse_pos[0], mouse_pos[1]
        cor_x = (mouse_pos_x - self.left) // self.cell_size
        cor_y = (mouse_pos_y - self.top) // self.cell_size
        if len(self.board[0]) - 1 >= cor_x >= 0 and len(self.board) - 1 >= cor_y >= 0:
            return (cor_x, cor_y)
        else:
            return None

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell != None:
            self.on_click(cell)

    def on_click(self, cell):
        coor_x, coor_y = cell[0], cell[1]
        cell_mine = self.open_cell(coor_x, coor_y)
        self.board[coor_y][coor_x] = cell_mine


class Minesweeper(Board):
    def __init__(self, gorizontal, vertical, colvo_min):
        super().__init__(gorizontal, vertical)
        self.gorizontal = gorizontal
        self.vertical = vertical
        self.colvo_min = colvo_min

    def do_mines(self):
        for i in range(colvo_min):
            mine_y = random.randint(0, self.vertical - 1)
            mine_x = random.randint(0, self.gorizontal - 1)
            self.board[mine_y][mine_x] = 10

    def open_cell(self, coor_x, coor_y):
        cell_mine = 0
        if coor_x != 0 and coor_y != 0 and coor_x != self.gorizontal - 1 and coor_y != self.vertical - 1 and \
                self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x - 1] == 10:  # gorizontal
                cell_mine += 1
            if self.board[coor_y][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x] == 10:  # vertical
                cell_mine += 1
            if self.board[coor_y + 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x - 1] == 10:  # first diagonal
                cell_mine += 1
            if self.board[coor_y + 1][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x - 1] == 10:  # вторая диагональ
                cell_mine += 1
            if self.board[coor_y - 1][coor_x + 1] == 10:
                cell_mine += 1
            return cell_mine

        elif coor_x == self.gorizontal - 1 and coor_y != self.vertical - 1 and coor_y != 0 and self.board[coor_y][
            coor_x] != 10:
            if self.board[coor_y][coor_x - 1] == 10:  # gorizontal
                cell_mine += 1
            if self.board[coor_y - 1][coor_x] == 10:  # vertical
                cell_mine += 1
            if self.board[coor_y + 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x - 1] == 10:  # first diagonal
                cell_mine += 1
            if self.board[coor_y + 1][coor_x - 1] == 10:  # вторая диагональ
                cell_mine += 1
            return cell_mine
        elif coor_x == 0 and coor_y != self.vertical - 1 and coor_y != 0 and self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x + 1] == 10:  # gorizontal
                cell_mine += 1
            if self.board[coor_y - 1][coor_x] == 10:  # vertical
                cell_mine += 1
            if self.board[coor_y + 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x + 1] == 10:  # first diagonal
                cell_mine += 1
            if self.board[coor_y + 1][coor_x + 1] == 10:  # вторая диагональ
                cell_mine += 1
            return cell_mine
        elif coor_y == 0 and coor_x != self.gorizontal - 1 and coor_x != 0 and self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x - 1] == 10:
                cell_mine += 1
            if self.board[coor_y][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x - 1] == 10:
                cell_mine += 1
            return cell_mine
        elif coor_y == self.vertical - 1 and coor_x != self.gorizontal - 1 and coor_x != 0 and self.board[coor_y][
            coor_x] != 10:
            if self.board[coor_y][coor_x - 1] == 10:
                cell_mine += 1
            if self.board[coor_y][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x - 1] == 10:  # first diagonal
                cell_mine += 1
            return cell_mine
        elif coor_x == 0 and coor_y == 0 and self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x + 1] == 10:
                cell_mine += 1
            return cell_mine
        elif coor_x == self.gorizontal - 1 and coor_y == 0 and self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x - 1] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y + 1][coor_x - 1] == 10:
                cell_mine += 1
            return cell_mine
        elif coor_x == 0 and coor_y == self.vertical - 1 and self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x + 1] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x + 1] == 10:
                cell_mine += 1
            return cell_mine
        elif coor_x == self.gorizontal - 1 and coor_y == self.vertical - 1 and self.board[coor_y][coor_x] != 10:
            if self.board[coor_y][coor_x - 1] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x] == 10:
                cell_mine += 1
            if self.board[coor_y - 1][coor_x - 1] == 10:
                cell_mine += 1
            return cell_mine
        else:
            cell_mine = 10
            return cell_mine


def main(gorizontal, vertical, colvo_min):
    pygame.init()
    pygame.display.set_caption('Поле')
    size = 800, 800
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.display.flip()
    board = Minesweeper(gorizontal, vertical, colvo_min)
    running = True
    board.do_mines()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)
        screen.fill((0, 0, 0))
        board.render(screen)
        board.set_view(100, 100, 50)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == "__main__":
    gorizontal = int(input())
    vertical = int(input())
    colvo_min = int(input())
    main(gorizontal, vertical, colvo_min)
