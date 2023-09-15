import tkinter as tk
import random as rnd


def setup():
    canvas.create_image(0, height - 40, image=nit, anchor= tk.NW)
    for i in range(40):
        x = rnd.randrange(0, width - size)
        y = rnd.randrange(0, height - size - 40)
        moveable.append(canvas.create_oval(x, y, x + size, y + size, fill = colors[i//10]))


def check(e):
    global process
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if len(zoz) != 0 and zoz[-1] in moveable and len(process) == 0 and counter < 10:
        process.append(zoz[-1])
        moveable.remove(zoz[-1])
        mover()


def mover():
    global process
    coor = canvas.coords(process[0])
    final_pos = (710, 475)
    dx = final_pos[0] - coor[0] - size//2
    dy = final_pos[1] - coor[1] - size//2
    if dx != 0 and dy != 0:
        # if dx >= dy:
        #     dx = dx//dy
        #     dy = 1
        # else:
        dx = dx//dy
        dy = dy//dy
    canvas.move(process[0], dx, dy)
    if (coor[1]+coor[3])//2 == 475:
        ball_to_nit()
    else:
        canvas.after(5, mover)


def ball_to_nit():
    global process, nit_len, counter
    a = canvas.coords(process[0])
    if a[0] > nit_len:
        canvas.move(process[0], -2, 0)
        canvas.after(5, ball_to_nit)
    else:
        counter += 1
        process = []
        nit_len += size


root = tk.Tk()
width = 750
height = 500
size = 40
canvas = tk.Canvas(root, width=width, height=height, bg = 'white')
canvas.pack()
colors = ['pink', 'yellow', 'green', 'blue']
nit = tk.PhotoImage(file= 'koralik_nit.png')
nit_len = 36    # 36, 475   710, 475 suradnice zaciatku a konca nite
moveable = []
process = []
counter = 0
setup()

canvas.bind('<Button-1>', check)

root.mainloop()