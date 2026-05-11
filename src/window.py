from tkinter import Tk, Canvas, BOTH
from .line import Line


class Window:
    def __init__(self, width: int, height: int) -> None:
        self.root = Tk()
        self.root.title = "maze"
        self.canvas = Canvas(width=width, height=height, bg="white")
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line: Line, color: str) -> None:
        line.draw(self.canvas, color)

    def redraw(self) -> None:
        self.root.update()
        self.root.update_idletasks()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False
