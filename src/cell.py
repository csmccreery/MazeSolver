from .window import Window
from .point import Point
from .line import Line


class Cell:
    def __init__(self, win=None) -> None:
        self.has_left_wall: bool = True
        self.has_right_wall: bool = True
        self.has_top_wall: bool = True
        self.has_bottom_wall: bool = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False

    def set_coords(self, x1, x2, y1, y2) -> None:
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2

    def draw(self, color) -> None:
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)

        walls = [
                (Line(top_left, bottom_left), self.has_left_wall),
                (Line(top_right, bottom_right), self.has_right_wall),
                (Line(top_left, top_right), self.has_top_wall),
                (Line(bottom_left, bottom_right), self.has_bottom_wall),
            ]

        if self.__win:
            for wall, exists in walls:
                wall_color = color if exists else "white"
                wall.draw(self.__win.canvas, wall_color)

    def __find_center(self) -> Point:
        x = self.__x1 + abs(self.__x1 - self.__x2) / 2
        y = self.__y1 + abs(self.__y1 - self.__y2) / 2

        return Point(x, y)

    def draw_move(self, to_cell, undo=False) -> None:
        color = "red" if undo else "black"
        self_center = self.find_center()

        if to_cell is not None:
            other_center = to_cell.find_center()
        else:
            raise Exception("No adjacent cell found")

        line = Line(self_center, other_center)
        line.draw(self.__win.canvas, color)
