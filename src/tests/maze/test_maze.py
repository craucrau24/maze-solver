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

    def test_maze_break_entrance_and_exit(self):
        win = unittest.mock.MagicMock()
        
        mazes = [
            Maze(Point(0,0), 10, 15, 10, 10, win),
            Maze(Point(0,0), 8, 25, 10, 10, win),
            Maze(Point(0,0), 15, 40, 10, 10, win),
        ]

        for maze in mazes:
            self.assertTrue(maze._cells[0][0].has_left_wall)
            self.assertTrue(maze._cells[-1][-1].has_right_wall)
            maze._break_entrance_and_exit()
            self.assertFalse(maze._cells[0][0].has_left_wall)
            self.assertFalse(maze._cells[-1][-1].has_right_wall)