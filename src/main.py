from gui.window import Window
from gui.point import Point
from maze.cell import Cell

def create_cells(data, win):
    cells = []
    for coords, walls in data:
        x1, y1, x2, y2 = coords
        cell = Cell(win, Point(x1, y1), Point(x2, y2))
        if "left" not in walls:
            cell.has_left_wall = False
        if "right" not in walls:
            cell.has_right_wall = False
        if "top" not in walls:
            cell.has_top_wall = False
        if "bottom" not in walls:
            cell.has_bottom_wall = False
        cells.append(cell)
    return cells

def main():
    win = Window(800, 600)
    cell_data = [
        ((20, 20, 40, 40), set(["left", "right", "top", "bottom"])),
        ((60, 40, 80, 60), set(["left", "right"])),
        ((100, 60, 120, 80), set(["top", "bottom"])),
        ((140, 80, 160, 100), set(["left", "top"])),
        ((180, 100, 200, 120), set(["right", "bottom"])),

    ]
    cells = create_cells(cell_data, win)
    for cell in cells:
        cell.draw()
    
    cells[0].draw_move(cells[1], True)
    cells[2].draw_move(cells[3])
    
    win.wait_for_close()


if __name__ == "__main__":
    main()