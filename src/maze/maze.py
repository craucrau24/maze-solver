from .cell import Cell
from gui.point import Point

class Maze:
    def __init__(self, origin, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.origin = origin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win

        self._create_cells()

    def _create_cells(self):
        self.__cells = [
            [self._create_cell(i, j) for j in range(self.num_cols)] for i in range(self.num_rows)
        ]
        
        for row in self.__cells:
            for cell in row:
                cell.draw()

    def _create_cell(self, i, j):
        x = self.origin.x + j * self.cell_size_x
        y = self.origin.y + i * self.cell_size_y
        cell = Cell(self.__win, Point(x, y), Point(x + self.cell_size_x, y + self.cell_size_y))
        return cell

    def _animate(self):
        pass