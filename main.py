from src.window import Window
from src.maze import Maze


WIN_X_SIZE = 1920
WIN_Y_SIZE = 1080
NUM_COLS = 100
CELL_SIZE = WIN_X_SIZE // NUM_COLS
NUM_ROWS = WIN_Y_SIZE // CELL_SIZE

def main():
    win = Window(WIN_X_SIZE, WIN_Y_SIZE)

    maze = Maze(1, 1, WIN_X_SIZE, WIN_Y_SIZE,
                NUM_ROWS, NUM_COLS, CELL_SIZE, CELL_SIZE, win)

    win.wait_for_close()


if __name__ == "__main__":
    main()
