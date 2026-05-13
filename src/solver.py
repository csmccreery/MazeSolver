from .maze import Maze
from .cell import Cell


class Solver:
    def __init__(self, maze: Maze) -> None:
        self.__maze: Maze = maze
        self.__starting_position = (self.__maze.x1, self.__maze.y1)
        self.__current_cell: Cell = self.__maze.cells[
                self.__starting_position[0]][self.__starting_position[1]
            ]

    def __valid_cell(self, direction, i, j) -> bool:
        valid_cell_position = (
                i >= self.__maze.y1 and i <= self.__maze.num_rows and
                j >= self.__maze.x1 and j <= self.__maze.num_cols
            )

        if not valid_cell_position:
            return False

        if direction == "up" and self.__maze.cells[i][j].has_bottom_wall:
            return False

        if direction == "down" and self.__maze.cells[i][j].has_top_wall:
            return False

        if direction == "left" and self.__maze.cells[i][j].has_right_wall:
            return False

        if direction == "right" and self.__maze.cells[i][j].has_left_wall:
            return False

        if self.__maze.cells[i][j].visited:
            return False

        return True

    def solve_dfs(self) -> bool:
        self.__maze.animate(0.05)
        start_y, start_x = self.__starting_position
        self.__maze.cells[start_x][start_y].visited = True

        if self.__current_cell.target:
            return True

        directions = [
                    ("up",
                     self.__current_cell.location[0],
                     self.__current_cell.location[1] + 1
                     ),
                    ("down",
                     self.__current_cell.location[0],
                     self.__current_cell.location[1] - 1
                     ),
                    ("left",
                     self.__current_cell.location[0] + 1,
                     self.__current_cell.location[1]
                     ),
                    ("right",
                     self.__current_cell.location[0] - 1,
                     self.__current_cell.location[1]
                     ),
                ]

        for direction, i, j in directions:
            if self.__valid_cell(direction, i, j):
                next_cell = self.__maze.cells[i][j]
                self.__current_cell.draw_move(next_cell)
                next_move = self.solve_dfs()

                if next_move:
                    return True

                self.__current_cell.draw_move(next_cell)
                self.__current_cell = next_cell
            
    def solve_djikstra(self) -> bool:
        pass

    def solve_a_star(self) -> bool:
        pass

    def solve_bellman_ford(self) -> bool:
        pass
