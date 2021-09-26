import tkinter
from tkinter import messagebox
import random

field = []
score = 0

def is_end():
    global field

    for i in range(15):
        if field[i]["text"] != str(i + 1):
            return
    
    tkinter.messagebox.showinfo("Поздравляем!", "Победа!")
    tkinter.messagebox.showinfo("Ваш счет", score)
    exit()

def find_empty_cell():
    global field
    for i in range(16):
        if field[i]["text"] == "":
            return i

def key_press(event):
    global score
    em_pos = find_empty_cell()

    if event.keycode == 37:
        if (em_pos + 1) % 4 != 0:
            field[em_pos]["text"], field[em_pos + 1]["text"] = field[em_pos + 1]["text"], field[em_pos]["text"]
            score = score + 1
    if event.keycode == 38:
        if em_pos < 12:
            field[em_pos]["text"], field[em_pos + 4]["text"] = field[em_pos + 4]["text"], field[em_pos]["text"]
            score = score + 1
    if event.keycode == 39:
        if em_pos % 4 != 0:
            field[em_pos]["text"], field[em_pos - 1]["text"] = field[em_pos - 1]["text"], field[em_pos]["text"]
            score = score + 1
    if event.keycode == 40:
        if em_pos > 3:
            field[em_pos]["text"], field[em_pos - 4]["text"] = field[em_pos - 4]["text"], field[em_pos]["text"]
            score = score + 1
    print(score)
    is_end()
    
def start_game():
    n = 0

    for i in range(4):
        for j in range(4):
            color = give_me_color()
            field.append(tkinter.Label(root_window, width=6, height=3, font="Arial 20 bold", borderwidth=2, relief="solid", bg = color))
            field[n].grid(row=i, column=j)
            n = n + 1

    k = 1
    while k < 16:
        button_index = random.randint(0, 15)
        if field[button_index]["text"] == "":
            field[button_index]["text"] = str(k)
            k = k + 1

def give_me_color():
    r = int(random.random() * 256)
    g = int(random.random() * 256)
    b = int(random.random() * 256)

    random_color = "#%02x%02x%02x" % (r, g, b)
    return(random_color)
root_window = tkinter.Tk()
root_window.title("Пятнашки")
root_window.resizable(False, False)
root_window.bind("<Key>", key_press)

start_game()
give_me_color()
root_window.mainloop()