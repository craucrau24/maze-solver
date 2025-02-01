import unittest
import unittest.mock
from maze.maze import Maze
from gui.point import Point

class TestMaze(unittest.TestCase):
    def test_maze_cells_dimension(self):
        win = unittest.mock.MagicMock()
        maze = Maze(Point(0,0), 10, 15, 10, 10, win)
        self.assertEqual(len(maze._cells), 10)
        self.assertEqual(len(maze._cells[0]), 15)

        maze = Maze(Point(0,0), 8, 25, 10, 10, win)
        self.assertEqual(len(maze._cells), 8)
        self.assertEqual(len(maze._cells[0]), 25)

        maze = Maze(Point(0,0), 15, 40, 10, 10, win)
        self.assertEqual(len(maze._cells), 15)
        self.assertEqual(len(maze._cells[0]), 40)