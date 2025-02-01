from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Awesome Maze Solver"
        self.__canvas = Canvas(self.__root, width=width, height=height)
        self.__canvas.pack()
        self.__running = True
        self.__width = width
        self.__height = height

        self.__root.protocol("WM_DELETE_WINDOW", self.close)
    
    def clear(self):
        self.__canvas.create_rectangle(0, 0, self.__width, self.__height, fill="white")

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)