import tkinter as tk
import random


def setup():
    global button, empty, coins
    empty = []
    for x in range(0, WIDTH - 3 * square, square):
        for y in range(0, HEIGHT, square):
            if random.randrange(0, 100) < 20:
                canvas.create_image(x, y, image=ostrov0, anchor=tk.NW)
            else:
                empty.append(canvas.create_image(x, y, image=ostrov3, anchor=tk.NW))
    coins = canvas.create_text(WIDTH - 3*square, 0, text=coin_count, font=('Helvetica', '30', 'bold'), anchor=tk.NW)
    button = canvas.create_image(WIDTH - square, 0, image=ostrov_kruh0, anchor=tk.NW)


def click(e):
    global empty
    clicked = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if button in clicked:
        change_button()
    elif clicked[0] in empty:
        canvas.itemconfig(clicked[0], image=change_island(clicked[0]))
        empty.remove(clicked[0])
    elif clicked[0] in most:
        if canvas.itemcget(clicked[0], 'image') == 'pyimage2':
            canvas.itemconfig(clicked[0], image=ostrov2)
        else:
            canvas.itemconfig(clicked[0], image=ostrov1)


def change_button():
    if canvas.itemcget(button, 'image') == 'pyimage6':      # pyimage6 doplni ostrov
        canvas.itemconfig(button, image=ostrov_kruh0)
    else:
        canvas.itemconfig(button, image=ostrov_kruh1)


def change_island(ff):
    global coin_count
    if canvas.itemcget(button, 'image') == 'pyimage6':      # pyimage6 doplni ostrov
        coin_count += 50
        canvas.itemconfig(coins, text=str(coin_count))
        return ostrov0
    else:
        coin_count += 10
        canvas.itemconfig(coins, text=str(coin_count))
        most.append(ff)
        return ostrov1


M = random.randint(4, 6)
N = random.randint(3, 9)

root = tk.Tk()
square = 50
WIDTH = square * (M + 3)
HEIGHT = square * N
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

ostrov0 = tk.PhotoImage(file='img/ostrov0.png')                 # ostrov
ostrov1 = tk.PhotoImage(file='img/ostrov1.png')                 # vodorvny most
ostrov2 = tk.PhotoImage(file='img/ostrov2.png')                 # zvisly most
ostrov3 = tk.PhotoImage(file='img/ostrov3.png')                 # prazdne
ostrov_kruh0 = tk.PhotoImage(file='img/ostrov_kruh0.png')       # dopln most
ostrov_kruh1 = tk.PhotoImage(file='img/ostrov_kruh1.png')       # dopln ostrov
coin_count = 0
most = []

setup()
canvas.bind('<Button-1>', click)


root.mainloop()
