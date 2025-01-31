from gui.window import Window
from gui.point import Point
from gui.line import Line

def main():
    win = Window(800, 600)
    win.draw_line(Line(Point(10, 50), Point(200,150)), "blue")
    win.draw_line(Line(Point(410, 350), Point(100,250)), "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()