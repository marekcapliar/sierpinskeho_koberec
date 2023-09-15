# gulicka cez create_oval treba ju posuvat o dany vektor
# move(vector) posun o dany vektor
# vector(1,1) -> vector(-1,1) -> vector(-1,-1) -> vector(1,-1) -> vector(1,1)
import tkinter as tk
import random

def ball_move():
    global ball, movement, desk
    canvas.move(ball, movement[0], movement[1])
    destroy_brick()
    pos = canvas.coords(ball)
    desk_pos = canvas.coords(desk)
    overlap = canvas.find_overlapping(desk_pos[0], desk_pos[1], desk_pos[2], desk_pos[3])
    if pos[2] >= width:     # prava hranica
        movement = [movement[0] * -1, movement[1]]
    elif pos[3] >= height:  # spodna hranica
        canvas.delete('all')
        canvas.create_image(0, 0, image= lose_img, anchor= tk.NW)
        text = canvas.create_text(width//2, height//2, text='YOU LOST')
    elif pos[0] <= 0:       # lava hranica
        movement = [movement[0] * -1, movement[1]]
    elif pos[1] <= 0:       # vrchna hranica
        movement = [movement[0], movement[1] * -1]
    elif ball in overlap:   # hitne desk
        movement = bounce(pos, desk_pos)
    if len(bricks) == 0:    # vyhra
        canvas.create_text(width//2, height//2 - 50, text='YOU WON')
        canvas.delete(ball)
    canvas.after(2, ball_move)


def update_rect():
    canvas.move(desk, dx, dy)
    root.after(30, update_rect)


def move_left(e):
    global dx
    dx = -10


def move_right(e):
    global dx
    dx = 10


def stop_move(e):
    global dx, dy
    dx = 0
    dy = 0


def mover(e):
    global x
    x2 = e.x
    if x != 0:
        mouse = x2-x
        canvas.move(desk, mouse, 0)
        x= e.x


def bounce(ball_pos, rec_pos):
    ball_pos = (ball_pos[0] + ball_pos[2])//2
    rec_middle = (rec_pos[0] + rec_pos[2])//2
    ball_to_rec = ball_pos - rec_middle
    return [ball_to_rec//(rec_w//3), -1]    # rec_w//3 => vector x je 0-3


def starter(e):
    global x, y
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if desk in zoz:
        x = e.x
        y = e.y
        ball_move()
        canvas.delete(start_text)


def prepare_bricks():
    global special
    for y in range(brick_count_y):
        for x in range(brick_count_x):
            bricks.append(canvas.create_rectangle(x * brick_w, y * brick_h, (x+1) * brick_w, (y+1) * brick_h, fill= 'magenta', width= 5, outline = 'black'))
    special = random.choice(bricks)
    canvas.itemconfig(special, fill='gold')


def destroy_brick():
    global movement, temp
    coord_ball = canvas.coords(ball)
    items_list = canvas.find_overlapping(coord_ball[0], coord_ball[1], coord_ball[2], coord_ball[3])
    for i in items_list:
        if i in bricks:
            rec_coords = canvas.coords(i)
            bricks.remove(i)
            canvas.delete(i)
            if i == special:
                temp = False
                counter()
            if temp:
                if coord_ball[0] >= rec_coords[2]:     # prava hranica
                    movement = [movement[0] * -1, movement[1]]
                elif coord_ball[1] >= rec_coords[3]:  # spodna hranica
                    movement = [movement[0], movement[1] * -1]
                elif coord_ball[2] <= rec_coords[0]:       # lava hranica
                    movement = [movement[0] * -1, movement[1]]
                elif coord_ball[3] <= rec_coords[1]:       # vrchna hranica
                    movement = [movement[0], movement[1] * -1]
            break
                        

def winner(e):
    for i in bricks[:]:
        canvas.delete(i)
        bricks.remove(i)
    canvas.create_image(0, 0, image= cheater_img, anchor= tk.NW)
    canvas.create_text(width//2,height//2, text='bad ending')


def counter():
    global ftime, temp
    canvas.itemconfig(spec_ball, text=ftime)
    ftime -= 1
    if ftime < 0:
        temp = True
        canvas.itemconfig(spec_ball, text='')
    canvas.after(1000,counter)


root = tk.Tk()
width = 500
height = 500
ws = 10
rec_w = 25
brick_count_y = 4
brick_count_x = 10
brick_w = width//brick_count_x
brick_h = 20
bricks = []
bg = 'white'
canvas = tk.Canvas(root, width= width, height= height, bg= bg)
canvas.pack()
movement = [0,1]

win_img = tk.PhotoImage(file='arkanoid/treat.png')
new_img = win_img.subsample(win_img.width()//(brick_w * brick_count_x), round(win_img.height()/(brick_h * brick_count_y)))
canvas.create_image(0, 0, image= new_img, anchor= tk.NW)

lose = tk.PhotoImage(file='arkanoid/win.png')
lose_img = lose.subsample(lose.width()//width, round(lose.height()/height))

cheater = tk.PhotoImage(file='arkanoid/chet.png')
cheater_img = cheater.subsample(cheater.width()//width, round(cheater.height()/height))

ftime = 15
spec_ball = canvas.create_text(width//2, height//2, text='')
temp = True

ball = canvas.create_oval(width//2 - ws, height//2 - ws, width//2 + ws, height//2 + ws, fill = 'red')
desk = canvas.create_rectangle(width//2 - rec_w, height - 30, width//2 + rec_w, height - 20, fill= 'yellow')
dx = 0
dy = 0

# toto jest na pohyb myskou
# start_text = canvas.create_text(width//2, height//2 - 50, text='KLICK ON RECTANGLE TO START\nplay on fullscreen\nuse mouse to move')
# canvas.bind('<Button-1>', starter)
# canvas.bind('<Motion>',mover)

# prvy sposob ako nabindovat klavesy
# root.bind('<Key>', check_key)
prepare_bricks()
root.bind('<Right>',move_right)
root.bind('<Left>', move_left)
root.bind('<KeyRelease>', stop_move)
root.bind('d', winner)
ball_move()
update_rect()

# druhy sposob ako nabindovat klavesy
# canvas.focus_set()
# canvas.bind('d', move_right)
# canvas.bind('a', move_left)

root.mainloop()