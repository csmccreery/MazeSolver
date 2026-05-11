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

    def draw(self, x1, x2, y1, y2, color) -> None:
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

        pt1, pt2 = Point(x1, y1), Point(x2, y1)
        pt3, pt4 = Point(x1, y2), Point(x2, y2)
        walls = []

        if self.has_left_wall:
            walls.append(Line(pt1, pt3))
        if self.has_right_wall:
            walls.append(Line(pt2, pt4))
        if self.has_top_wall:
            walls.append(Line(pt3, pt4))
        if self.has_bottom_wall:
            walls.append(Line(pt1, pt2))

        if self.__win:
            for wall in walls:
                wall.draw(self.__win.canvas, color)

    def find_center(self) -> Point:
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
