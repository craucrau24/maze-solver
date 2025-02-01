from gui.point import Point
from gui.line import Line

class Cell:
    def __init__(self, win, topleft, botright):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__topleft = topleft
        self.__botright = botright
        self.__win = win
    
    def draw(self):
        lines = []
        topright = Point(self.__botright.x, self.__topleft.y)
        botleft = Point(self.__topleft.x, self.__botright.y)

        if self.has_left_wall:
            lines.append(Line(botleft, self.__topleft))
        if self.has_right_wall:
            lines.append(Line(self.__botright, topright))
        if self.has_top_wall:
            lines.append(Line(self.__topleft, topright))
        if self.has_bottom_wall:
            lines.append(Line(self.__botright, botleft))
        
        for line in lines:
            self.__win.draw_line(line, "black")
        
    def center(self):
        return Point((self.__topleft.x + self.__botright.x) / 2, (self.__topleft.y + self.__botright.y) / 2)
    
    def draw_move(self, to_cell, undo=False):
        self.__win.draw_line(Line(self.center(), to_cell.center()), "blue" if undo else "red" )