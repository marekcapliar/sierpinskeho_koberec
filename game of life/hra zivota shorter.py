import tkinter as tk

fr = open('game of life/imput.txt', 'r')


def create2Dmatrix(width, height):
    matrix = []
    temp = []
    for y in range(height):
        for x in range(width):
            temp.append(0)
        matrix.append(temp)
        temp = []
    return matrix


def process_file(matrix):
    x = 0
    y = 0
    for row in fr:
        for char in row:
            if char == '1':
                matrix[y][x] = 1
            x += 1
        y += 1
        x = 0


def friends(x, y, matrix):
    # matrix[y] [x]
    count = 0
    if matrix[y-1][x-1] == 1 and x-1 >= 0 and y-1 >= 0:
        count += 1
    if matrix[y-1][x] ==1 and y-1 >= 0:
        count += 1
    if x+1 <= width-1 and y-1 >= 0 and matrix[y-1][x+1] ==1:
        count += 1
    if matrix[y][x-1] == 1 and x-1 >= 0:
        count += 1
    if x+1 <= width-1 and matrix[y][x+1] == 1:
        count += 1
    if x-1 >= 0 and y+1 <= height-1 and matrix[y+1][x-1] == 1:
        count += 1
    if y+1 <= height-1 and matrix[y+1][x] == 1:
        count += 1
    if x+1 <= width-1 and y+1 <= height-1 and matrix[y+1][x+1] == 1:
        count += 1
    return count


def rewrite(matrix):
    global oldfield
    newfield = create2Dmatrix(width, height)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            neighbours = friends(x, y, oldfield)
            if matrix[y][x] == 1:
                if neighbours == 2 or neighbours == 3:
                    newfield[y][x] = 1
                else:
                    newfield[y][x] = 0
            elif matrix[y][x] == 0 and neighbours == 3:
                newfield[y][x] = 1
            else:
                newfield[y][x] = 0
    oldfield = newfield
    return newfield


text = fr.readline()
width, height = text.split(' ')
width = int(width)
height = int(height)

# vytvori 2D zoznam plny 0
oldfield = create2Dmatrix(width, height)

# do zoznamu nahodime 1 z imput.txt
process_file(oldfield)

# naimportujes canvas, vykreslis plochu tvaru mriezky
win = tk.Tk()
size = 20
WIDTH = width * size
HEIGHT = height * size
canvas = tk.Canvas(win, width= WIDTH, height= HEIGHT, bg='white')
canvas.pack()

def draw_grid(ws = size):
    count = HEIGHT // ws
    for i in range(count):
        canvas.create_line(0, i*ws, WIDTH, i*ws)
    count = WIDTH // ws
    for x in range(count):
        canvas.create_line(x*ws, 0, x*ws, HEIGHT)


def draw_cell(oldfield, ws = size):
    canvas.delete('all')
    draw_grid()
    for y in range(height):
        for x in range(width):
            if oldfield[y][x] == 1:
                canvas.create_oval(x*ws, y*ws, (x+1)*ws, (y+1)*ws, fill='green')


def auto_gen():
    global oldfield
    draw_cell(oldfield)
    rewrite(oldfield)
    canvas.after(100, auto_gen)


def next_gen():
    global oldfield
    draw_cell(oldfield)
    rewrite(oldfield)


next_gen()
auto_button = tk.Button(win, text='Auto', command=auto_gen)
auto_button.pack()
step_button = tk.Button(win, text='Next step', command=next_gen)
step_button.pack()

win.mainloop()