import tkinter as tk
import math


def sierpin(x, y, a, count = 0):
    if count < 5:
        count += 1
        for i in range(3):
            canvas.create_rectangle((i*a)//3 + x, 0 + y, ((i+1)*a)//3 + x, a//3 + y, fill='white', outline='black')
        canvas.create_rectangle(0 + x, a//3 + y, a//3 + x, (2*a)//3 + y, fill='white', outline='black')
        canvas.create_rectangle((2*a)//3 + x, a//3 + y, a + x, (2*a)//3 + y, fill='white', outline='black')
        for i in range(3):
            canvas.create_rectangle((i*a)//3 + x, (2*a)//3 + y, ((i+1)*a)//3 + x, a + y, fill='white', outline='black')
        for i in range(3):
            sierpin((i*a)//3 + x, 0 + y, a//3, count)
        sierpin(0 + x, a//3 + y, a//3, count)
        sierpin((2*a)//3 + x, a//3 + y, a//3, count)
        for i in range(3):
            sierpin((i*a)//3 + x, (2*a)//3 + y, a//3, count)


root = tk.Tk()

HEIGHT = 600
WIDTH = 600
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas.pack()
SPACE = 20
canvas.create_rectangle(SPACE, SPACE, WIDTH - SPACE, HEIGHT - SPACE, fill='white', outline='black')
sierpin(SPACE, SPACE, WIDTH - 2 * SPACE)

root.mainloop()