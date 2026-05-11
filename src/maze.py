from .cell import Cell
from time import sleep


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

    def __create_cells(self) -> None:
        # Note to self, may cause issues later
        matrix: list[list[Cell]] = [
                    [Cell(self.win) for _ in range(self.num_cols)]
                     for _ in range(self.num_rows)
                ]
        self.__cells = matrix
        if self.win:
            self.__draw_cell()

    def __draw_cell(self, frame_rate=0.05) -> None:
        for i in range(self.y1, self.num_rows):
            for j in range(self.x1, self.num_cols):
                y1 = self.y1 + (i * self.cell_size_y)
                y2 = y1 + self.cell_size_y

                x1 = self.x1 + (j * self.cell_size_x)
                x2 = x1 + self.cell_size_x

                self.__cells[i][j].draw(x1, x2, y1, y2, "black")
            self.__animate(frame_rate)

    def __animate(self, frame_rate) -> None:
        self.win.redraw()
        sleep(frame_rate)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell()
        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell()
