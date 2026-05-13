from .cell import Cell
from time import sleep
import random


class Maze:
    def __init__(
                self,
                x1,
                y1,
                x2,
                y2,
                num_rows,
                num_cols,
                cell_size_y,
                cell_size_x,
                win=None,
                seed=None
                ) -> None:

        self.x1: int = x1
        self.y1: int = y1
        self.x2: int = x2
        self.y2: int = y2
        self.num_rows: int = num_rows
        self.num_cols: int = num_cols
        self.cell_size_y: int = cell_size_y
        self.cell_size_x: int = cell_size_x
        self.win = win
        self.__cells = []
        self.__create_cells()
        if seed:
            self.__seed = seed
            random.seed(seed)

        self.__break_walls(0, 0)
        self.__reset_cells_visited()

    def __create_cells(self) -> None:
        # Note to self, may cause issues later
        matrix: list[list[Cell]] = [
                    [Cell(self.win) for _ in range(self.num_cols)]
                     for _ in range(self.num_rows)
                ]
        self.__cells = matrix
        self.__break_entrance_and_exit()
        if self.win:
            self.__draw_cell()

    def __draw_cell(self, frame_rate=0.05) -> None:
        for i in range(self.y1, self.num_rows):
            for j in range(self.x1, self.num_cols):
                y1 = self.y1 + (i * self.cell_size_y)
                y2 = y1 + self.cell_size_y

                x1 = self.x1 + (j * self.cell_size_x)
                x2 = x1 + self.cell_size_x
                self.__cells[i][j].set_coords(x1, x2, y1, y2)

                self.__cells[i][j].draw("black")
            self.__animate(frame_rate)

    def __animate(self, frame_rate) -> None:
        self.win.redraw()
        sleep(frame_rate)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[1][1].has_top_wall = False
        self.__cells[1][1].draw("white")
        self.__cells[-1][-1].has_bottom_wall = False
        self.__cells[-1][-1].draw("white")

    def __break_walls(self, i, j) -> None:
        self.__cells[i][j].visited = True

        while True:
            options = []
            if i + 1 < self.num_rows and not self.__cells[i + 1][j].visited:
                options.append(("down", i + 1, j))
            if i - 1 >= self.y1 and not self.__cells[i - 1][j].visited:
                options.append(("up", i - 1, j))
            if j + 1 < self.num_cols and not self.__cells[i][j + 1].visited:
                options.append(("right", i, j + 1))
            if j - 1 >= self.x1 and not self.__cells[i][j - 1].visited:
                options.append(("left", i, j - 1))

            if len(options) == 0:
                self.__cells[i][j].draw("black")
                return

            direction, next_i, next_j = options[random.randrange(len(options))]

            if direction == "up":
                if next_i >= self.y1:
                    self.__cells[i][j].has_top_wall = False
                    self.__cells[next_i][next_j].has_bottom_wall = False
            elif direction == "down":
                if next_i <= self.num_rows:
                    self.__cells[i][j].has_bottom_wall = False
                    self.__cells[next_i][next_j].has_top_wall = False
            elif direction == "left":
                if next_j >= self.x1:
                    self.__cells[i][j].has_left_wall = False
                    self.__cells[next_i][next_j].has_right_wall = False
            elif direction == "right":
                if next_j <= self.num_cols:
                    self.__cells[i][j].has_right_wall = False
                    self.__cells[next_i][next_j].has_left_wall = False

            # Recursively visit the next cell
            self.__break_walls(next_i, next_j)

    def __reset_cells_visited(self) -> None:
        for row in self.__cells:
            for col in row:
                col.visited = False
