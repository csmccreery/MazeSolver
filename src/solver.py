from .maze import Maze
from .cell import Cell


class Solver:
    def __init__(self, maze: Maze) -> None:
        self.__maze: Maze = maze

    def __valid_cell(self, direction, next_y, next_x) -> bool:
        valid_cell_position = (
                next_y >= self.__maze.y1 and next_y <= self.__maze.num_rows and
                next_x >= self.__maze.x1 and next_x <= self.__maze.num_cols
            )

        if not valid_cell_position:
            print(f"Position {next_y} outside bounds [{self.__maze.y1}, {self.__maze.num_rows}]")
            print(f"Position {next_x} outside bounds [{self.__maze.x1}, {self.__maze.num_cols}]")
            return False

        if direction == "up" and self.__maze.cells[next_y][next_x].has_top_wall:
            print(f"cell at position [{next_y}, {next_x}] has top wall")
            return False

        if direction == "down" and self.__maze.cells[next_y][next_x].has_bottom_wall:
            print(f"cell at position [{next_y}, {next_x}] has bottom wall")
            return False

        if direction == "left" and self.__maze.cells[next_y][next_x].has_left_wall:
            print(f"cell at position [{next_y}, {next_x}] has left wall")
            return False

        if direction == "right" and self.__maze.cells[next_y][next_x].has_right_wall:
            print(f"cell at position [{next_y}, {next_x}] has right wall")
            return False

        if self.__maze.cells[next_y][next_x].visited:
            print(f"cell at position [{next_y}, {next_x}] has been visited")
            return False

        return True

    def solve_dfs(self, current_cell=None) -> bool:
        self.__maze.animate(0.05)
        if not current_cell:
            current_cell = self.__maze.cells[self.__maze.x1][self.__maze.y1]

        pos_y, pos_x = current_cell.location

        if current_cell.target:
            return True

        directions = [
                    ("down", pos_y + 1, pos_x),
                    ("up", pos_y - 1, pos_x),
                    ("right", pos_y, pos_x + 1),
                    ("left", pos_y, pos_x - 1),
                ]

        print(f"Directions: {directions}")
        for direction, next_y, next_x in directions:
            print(f"Testing [{direction}] at position [{next_y}, {next_x}]")
            if self.__valid_cell(direction, next_y, next_x):
                print(f"Cell at position [{next_y}, {next_x}] valid.")
                next_cell = self.__maze.cells[next_y][next_x]
                current_cell.draw_move(next_cell)
                next_move = self.solve_dfs(next_cell)

                if next_move:
                    return True
                    break
                else:
                    current_cell.draw_move(next_cell, True)
        return False

    def solve_djikstra(self) -> bool:
        pass

    def solve_a_star(self) -> bool:
        pass

    def solve_bellman_ford(self) -> bool:
        pass
