from tkinter import *

root = Tk()
root.geometry("900x700")
root.title("The Game of Life by Evgenii Milgunov")
root.resizable(False, False)

def change_to(i, j, color):
    global mark, buttons
    if color == 0:
        buttons[i][j].config(bg='white')
        mark[i][j] = 0
    elif color == 1:
        buttons[i][j].config(bg='black')
        mark[i][j] = 1
    elif color == 2:
        buttons[i][j].config(bg='turquoise')
        mark[i][j] = 2
    buttons[i][j].grid(row=i, column=j)

def clickButton(i, j):
    global mark, buttons
    change_to(i, j, (mark[i][j] + 1) % 3)

def refresh():
    global buttons, mark, counter
    for i in range(27):
        for j in range(45):
            counter[i][j] = 0
            if i > 0 and mark[i - 1][j]:
                counter[i][j] += 1
            if j > 0 and mark[i][j - 1]:
                counter[i][j] += 1
            if i < 26 and mark[i + 1][j]:
                counter[i][j] += 1
            if j < 44 and mark[i][j + 1]:
                counter[i][j] += 1
            if i > 0 and j > 0 and mark[i - 1][j - 1]:
                counter[i][j] += 1
            if i > 0 and j < 44 and mark[i - 1][j + 1]:
                counter[i][j] += 1
            if i < 26 and j > 0 and mark[i + 1][j - 1]:
                counter[i][j] += 1
            if i < 26 and j < 44 and mark[i + 1][j + 1]:
                counter[i][j] += 1
    for i in range(27):
        for j in range(45):
            if mark[i][j] == 0:
                if counter[i][j] == 3:
                    change_to(i, j, 1)
                elif counter[i][j] == 4:
                    change_to(i, j, 2)
            elif mark[i][j] == 1:
                if counter[i][j] in (2, 3):
                    pass
                elif counter[i][j] == 5:
                    change_to(i, j, 2)
                else:
                    change_to(i, j, 0)
            elif mark[i][j] == 2:
                if counter[i][j] == 2:
                    change_to(i, j, 1)
                elif counter[i][j] == 4:
                    pass
                else:
                    change_to(i, j, 0)

launch = Button(text='Next step', command=refresh, bg='lime')
launch.grid(row=1, column=60)
buttons = [[Button()] * 45 for i in range(27)]
mark = [[0] * 45 for i in range(27)]
counter = [[0] * 45 for i in range(27)]
for i in range(27):
    for j in range(45):
        buttons[i][j] = Button(width=1, height=1, bg='white', command=lambda x=i, y=j: clickButton(x, y))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()