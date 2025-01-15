from tkinter import *

root = Tk()
root.geometry("900x700")
root.title("The Game of Life by Evgenii Milgunov")
root.resizable(False, False)

def clickButton(i, j):
    global mark, buttons
    if mark[i][j] == 0:
        buttons[i][j].configure(bg='black', fg='white')
        mark[i][j] = 1
    elif mark[i][j] == 1:
        buttons[i][j].configure(bg='white', fg='black')
        mark[i][j] = 0
    buttons[i][j].grid(row=i, column=j)

def refresh():
    global buttons, mark, counter
    for i in range(27):
        for j in range(45):
            counter[i][j] = 0
            if i > 0 and mark[i - 1][j] == 1:
                counter[i][j] += 1
            if j > 0 and mark[i][j - 1] == 1:
                counter[i][j] += 1
            if i < 26 and mark[i + 1][j] == 1:
                counter[i][j] += 1
            if j < 44 and mark[i][j + 1] == 1:
                counter[i][j] += 1
            if i > 0 and j > 0 and mark[i - 1][j - 1] == 1:
                counter[i][j] += 1
            if i > 0 and j < 44 and mark[i - 1][j + 1] == 1:
                counter[i][j] += 1
            if i < 26 and j > 0 and mark[i + 1][j - 1] == 1:
                counter[i][j] += 1
            if i < 26 and j < 44 and mark[i + 1][j + 1] == 1:
                counter[i][j] += 1
    for i in range(27):
        for j in range(45):
            if mark[i][j] == 0:
                if counter[i][j] == 3:
                    clickButton(i, j)
            elif mark[i][j] == 1:
                if counter[i][j] not in (2, 3):
                    clickButton(i, j)

launch = Button(text='Next step', command=refresh, bg='lime')
launch.grid(row=1, column=60)
buttons = [[Button()] * 45 for i in range(27)]
mark = [[0] * 45 for i in range(27)]
counter = [[0] * 45 for i in range(27)]
for i in range(27):
    for j in range(45):
        buttons[i][j] = Button(width=1, height=1, bg='white', fg='black', command=lambda x=i, y=j: clickButton(x, y))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()