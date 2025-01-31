from gui.window import Window
from gui.point import Point
from maze.maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(Point(20, 20), 15, 20, 30, 30, win)
    
    win.wait_for_close()


if __name__ == "__main__":
    main()