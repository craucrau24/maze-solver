from .cell import Cell
from gui.point import Point
from .iterators.random_passthrough import RandomPassThroughMazeIterator

class Maze:
    def __init__(self, origin, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.origin = origin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.__win = win

        self._create_cells()

    def _draw_cells(self):
        for row in self._cells:
            for cell in row:
                cell.draw()

    def _create_cells(self):
        self._cells = [
            [self._create_cell(i, j) for j in range(self.num_cols)] for i in range(self.num_rows)
        ]
        
        self._draw_cells()

    def _create_cell(self, i, j):
        x = self.origin.x + j * self.cell_size_x
        y = self.origin.y + i * self.cell_size_y
        cell = Cell(self.__win, Point(x, y), Point(x + self.cell_size_x, y + self.cell_size_y))
        return cell

    def _animate(self):
        pass

    def redraw(self):
        self.__win.clear()
        self._draw_cells()

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1].has_right_wall = False

    def neighbour_cells(self, row, column):
        neighbours = []
        if row < 0 or row >= self.num_rows:
            raise ValueError("Row index out of bound")
        if column < 0 or column >= self.num_cols:
            raise ValueError("Column index out of bound")

        if row != 0:
            neighbours.append(((row - 1, column), "up"))
        if column != 0:
            neighbours.append(((row, column - 1), "left"))
        if row != self.num_rows - 1:
            neighbours.append(((row + 1, column), "down"))
        if column != self.num_cols - 1:
            neighbours.append(((row, column + 1), "right"))
        
        return neighbours

    def _break_wall(self, orig, next, dir):
        o_cell = self._cells[orig[0]][orig[1]]
        n_cell = self._cells[next[0]][next[1]]
        match dir:
            case "up":
                o_cell.has_top_wall = False
                n_cell.has_bottom_wall = False
            case "down":
                o_cell.has_bottom_wall = False
                n_cell.has_top_wall = False
            case "left":
                o_cell.has_left_wall = False
                n_cell.has_right_wall = False
            case "right":
                o_cell.has_right_wall = False
                n_cell.has_left_wall = False
            case _:
                raise ValueError(f"Unknown direction {dir}")

    def _break_walls(self):
        iter = RandomPassThroughMazeIterator(self)
        for orig, next, dir in iter:
            self._break_wall(orig, next, dir)
