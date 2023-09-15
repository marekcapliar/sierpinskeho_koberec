# metoda kde funkcia vola seba samu

# pomocou coho sa najlepsie vysvetli rekurzia? pomocou rekurzie. hahahahahahahahhahahahahaha

# teoreticky moze byt nekonecny loop, prakticky je limit na pocet rekurzii
# pri volani funkcie rekurziou sa vytvara v pamati kopie funkcie => zaplna sa RAM
from string import ascii_lowercase
import tkinter as tk
import math

def faktorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * faktorial(n-1)


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def one_list(l: list):
    global new_list
    for i in l:
        if type(i) == int:
            new_list.append(i)
        else:
            one_list(i)
    return new_list


def generator_hesla(n):
    global vysledok
    if n == 0:
        print(vysledok)
    else:
        for pis in ascii_lowercase:
            vysledok[n*-1] = pis
            generator_hesla(n-1)


def reksucin(a, b,):
    global result
    if a == 0:
        return result
    else:
        a -= 1
        result += b
        reksucin(a, b)


def sierp(x, y, d, count = 0):
    if count < 9:
        count += 1
        height = ((-1)*d*math.sin(math.radians(60)))
        canvas.create_polygon(x, y, x + d, y, x + d//2, y + height, fill='white', outline='black')
        # canvas.create_line(x, y, x+d, y)
        # canvas.create_line(x+d, y, x+d//2, y+height)
        # canvas.create_line(x, y, x+d//2, y+height)
        sierp(x, y, d/2, count)
        sierp(x+d/2, y, d/2, count)
        sierp(x+d/4, y+ height//2, d//2, count)
        


print(faktorial(4))
print(fibonacci(5))
flat_list = [1, [2, 2, 2], 4, [[[3]]]]
new_list = []
print(one_list(flat_list))
print(new_list)

hlbka = 5
vysledok = ['a' for i in range(hlbka)]
print(vysledok)
# generator_hesla(hlbka)

result = 0
print(reksucin(5, 6))
print(result)

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=800, bg='white')
canvas.pack()
sierp(10, 600, 500)


root.mainloop()

# cisla na stredu: 7, 11, 12