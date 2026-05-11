import unittest
from src.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(x1=0, y1=0, x2=500, y2=500, num_rows=num_rows, num_cols=num_cols, cell_size_x=5, cell_size_y=5)
        self.assertEqual(
                    len(m1._Maze__cells),
                    num_rows,
                )
        self.assertEqual(
                    len(m1._Maze__cells[0]),
                    num_cols,
                )


if __name__ == "__main__":
    unittest.main()
