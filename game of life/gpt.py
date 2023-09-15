import tkinter as tk
import random

class Cell:
    def __init__(self, x, y, state):
        self.x = x
        self.y = y
        self.state = state

class GameOfLife:
    def __init__(self, master, width, height, cell_size):
        self.master = master
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cells = [[None for y in range(height)] for x in range(width)]
        self.canvas = tk.Canvas(self.master, width=width*cell_size, height=height*cell_size)
        self.canvas.pack()
        self.init_cells()
        self.draw_cells()
        self.master.after(100, self.step)

    def init_cells(self):
        for x in range(self.width):
            for y in range(self.height):
                state = random.choice([0, 1])
                self.cells[x][y] = Cell(x, y, state)

    def draw_cells(self):
        self.canvas.delete("all")
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]
                if cell.state == 1:
                    x1 = cell.x * self.cell_size
                    y1 = cell.y * self.cell_size
                    x2 = x1 + self.cell_size
                    y2 = y1 + self.cell_size
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def get_neighbors(self, x, y):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if x+i < 0 or x+i >= self.width or y+j < 0 or y+j >= self.height:
                    continue
                neighbors.append(self.cells[x+i][y+j])
        return neighbors

    def step(self):
        new_cells = [[None for y in range(self.height)] for x in range(self.width)]
        for x in range(self.width):
            for y in range(self.height):
                cell = self.cells[x][y]
                neighbors = self.get_neighbors(x, y)
                live_neighbors = sum(n.state for n in neighbors)
                if cell.state == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    new_cells[x][y] = Cell(x, y, 0)
                elif cell.state == 0 and live_neighbors == 3:
                    new_cells[x][y] = Cell(x, y, 1)
                else:
                    new_cells[x][y] = cell
        self.cells = new_cells
        self.draw_cells()
        self.master.after(100, self.step)

root = tk.Tk()
game = GameOfLife(root, 50, 50, 10)
root.mainloop()