# <Button-1>, <B1-Motion>, <ButtonRelease-1>
import tkinter as tk

win = tk.Tk()

Width = 500
Height = 500
canvas = tk.Canvas(win, height=Height, width=Width)
canvas.pack()


def clicker(e):
    # ak som klikol na nasom objekte zapamatam si suradnice
    global x, y
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if ob1 in zoz:
        x = e.x
        y = e.y


def mover(e):
    global x, y
    x2 = e.x
    y2 = e.y
    if x!=0 and y!=0:
        vector = (x2-x,y2-y)
        canvas.move(ob1, vector[0], vector[1])
        x, y = e.x, e.y


def releaser(e):
    global x, y
    x, y = 0, 0


ob1 = canvas.create_polygon(10, 10, 50, 80, 140, 82, fill='green')
canvas.bind('<Button-1>', clicker)
canvas.bind('<B1-Motion>',mover)
canvas.bind('<ButtonRelease-1>', releaser)

win.mainloop()