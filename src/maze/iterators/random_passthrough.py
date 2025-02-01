import random

class RandomPassThroughMazeIterator:
    def __init__(self, maze, seed=None):
        if seed is not None:
            random.seed(seed)

        self.__maze = maze
        self.__visited = set()
        self.__stack = []

        self.push_next((0, 0))

    def __iter__(self):
        return self

    def __next__(self):
        while 1:
            orig, next, dir = self.pop()
            if next not in self.__visited:
                break
        self.__visited.add(next)
        self.push_next(next)
        return orig, next, dir
    
    def pop(self):
        while 1:
            try:
                orig, neigh = self.__stack[-1]
            except IndexError:
                raise StopIteration

            try:
                ret = neigh.pop()
            except IndexError:
                self.__stack.pop()
                continue

            return (orig,) + ret


            


    def push_next(self, pos):
        row, col = pos
        neigh = self.__maze.neighbour_cells(row, col)
        random.shuffle(neigh)
        self.__stack.append((pos, neigh))