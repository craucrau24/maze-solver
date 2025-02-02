import random

class RegularMazeIterator:
    def __init__(self, maze):
        self.__maze = maze
        self.__visited = set()
        self.__stack = []

        self.push_next((0, 0))

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            orig, next, dir = self.pop()
            if not dir or next not in self.__visited:
                break
        if dir:
            self.push_next(next)
        return orig, next, dir
    
    def pop(self):
        while 1:
            try:
                orig, neigh = self.__stack[-1]
                dir = True
            except IndexError:
                raise StopIteration

            try:
                next, _ = neigh.pop()
            except IndexError:
                self.__stack.pop()
                next = self.__stack[-1][0]
                dir = False

            return (orig, next, dir)

    def push_next(self, pos):
        self.__visited.add(pos)

        row, col = pos
        neigh = self.__maze.neighbour_cells(row, col)
        random.shuffle(neigh)
        self.__stack.append((pos, neigh))
