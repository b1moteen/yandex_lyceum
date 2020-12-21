import pygame

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
        print(cell)
        if cell != None:
            self.on_click(cell)

    def on_click(self, cell):
        coor_x, coor_y = cell[0], cell[1]
        cell_mine = self.open_cell(coor_x, coor_y)
        self.board[coor_y][coor_x] = cell_mine
