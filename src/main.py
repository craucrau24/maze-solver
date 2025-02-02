from gui.window import Window
from gui.point import Point
from maze.maze import Maze

def main():
    win = Window(1200, 900)
    maze = Maze(Point(20, 20), 28, 45, 25, 30, win)
    maze._break_entrance_and_exit()
    maze._break_walls()
    maze.redraw()
    maze.solve()
    win.add(maze)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()