from tkinter import Canvas
from .point import Point


class Line:
    def __init__(self, pt1: Point, pt2: Point) -> None:
        self.pt1 = pt1
        self.pt2 = pt2

    def draw(self, canvas: Canvas, color: str) -> None:
        canvas.create_line(
                    self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y,
                    fill=color, width=2
                )
