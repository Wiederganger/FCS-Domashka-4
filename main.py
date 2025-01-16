from tkinter import *

root = Tk()                                                #создаём окно
root.geometry("900x700")                                   #задаём размер окна
root.title("The Game of Life by Evgenii Milgunov")         #задаём заголовок окна
root.resizable(False, False)                               #запрещаем изменять размер окна

#функция меняющая цвет клетки на заданный
def change_to(i, j, color):
    global mark, buttons                                   #передаём матрицы mark и buttons
    if color == 0:                                         #если заданный цвет - белый (0)
        buttons[i][j].config(bg='white')                   #меняем цвет кнопки на белый (0)
        mark[i][j] = 0                                     #меняем цвет элемента матрицы на белый (0)
    elif color == 1:                                       #если заданный цвет - чёрный (1)
        buttons[i][j].config(bg='black')                   #меняем цвет кнопки на чёрный (1)
        mark[i][j] = 1                                     #меняем цвет элемента матрицы на чёрный (1)
    elif color == 2:                                       #если заданный цвет - бирюзовый (2)
        buttons[i][j].config(bg='turquoise')               #меняем цвет кнопки на бирюзовый (2)
        mark[i][j] = 2                                     #меняем цвет элемента матрицы на бирюзовый
    buttons[i][j].grid(row=i, column=j)                    #обновляем кнопку

#функция циклически меняющая цвет клетки по клику (ручной ввод)
def clickButton(i, j):
    global mark, buttons                                   #передаём матрицы mark и buttons
    change_to(i, j, (mark[i][j] + 1) % 3)                  #вызываем функцию change_to для смены цвета

#функция делающая 1 обновление поля
def refresh():
    global buttons, mark, counter                          #передаём матрицы buttons, mark и counter
    for i in range(27):                                    #идём по строкам
        for j in range(45):                                #идём по столбцам
            counter[i][j] = 0                              #обнуляем количество "немёртвых" соседей для каждой из клеток
            if i > 0 and mark[i - 1][j]:                   #если клетка сверху "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if j > 0 and mark[i][j - 1]:                   #если клетка слева "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if i < 26 and mark[i + 1][j]:                  #если клетка снизу "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if j < 44 and mark[i][j + 1]:                  #если клетка справа "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if i > 0 and j > 0 and mark[i - 1][j - 1]:     #если клетка сверху слева "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if i > 0 and j < 44 and mark[i - 1][j + 1]:    #если клетка сверху справа "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if i < 26 and j > 0 and mark[i + 1][j - 1]:    #если клетка снизу слева "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
            if i < 26 and j < 44 and mark[i + 1][j + 1]:   #если клетка снизу справа "немёртвая"
                counter[i][j] += 1                         #увеличиваем счётчик на 1
    for i in range(27):                                    #идём по строкам
        for j in range(45):                                #идём по столбцам
            if mark[i][j] == 0:                            #если текущая клетка белая (0)
                if counter[i][j] == 3:                     #если "немёртвых" соседей 3
                    change_to(i, j, 1)                     #меняем цвет на чёрный (1)
                elif counter[i][j] == 4:                   #если "немёртвых" соседей 4
                    change_to(i, j, 2)                     #меняем цвет на бирюзовый (2)
            elif mark[i][j] == 1:                          #если текущая клетка чёрная (1)
                if counter[i][j] in (2, 3):                #если количество "немёртвых" соседей равно 2 или 3
                    pass                                   #оставляем как есть
                elif counter[i][j] == 5:                   #если "немёртвых" соседей 5
                    change_to(i, j, 2)                     #меняем цвет на бирюзовый (2)
                else:                                      #иначе
                    change_to(i, j, 0)                     #меняем цвет на белый (0)
            elif mark[i][j] == 2:                          #если текущая клетка бирюзовая (2)
                if counter[i][j] == 2:                     #если "немёртвых" соседей 2
                    change_to(i, j, 1)                     #меняем цвет на чёрный (1)
                elif counter[i][j] == 4:                   #если немёртвых соседей 4
                    pass                                   #оставляем как есть
                else:                                      #иначе
                    change_to(i, j, 0)                     #меняем цвет на белый (0)

launch = Button(text='Next step', command=refresh, bg='lime')      #создаём кнопку для произведения следующего шага
launch.grid(row=1, column=60)                                      #размещаем эту кнопку сбоку
#создаём двумерный массив кнопок размера клеточного поля
buttons = [[Button()] * 45 for i in range(27)]
#создаём двумерный массив цветов размера клеточного поля
mark = [[0] * 45 for i in range(27)]
#создаём двумерный массив количества "немёртвых" соседей размера клеточного поля
counter = [[0] * 45 for i in range(27)]
for i in range(27):           #идём по строкам
    for j in range(45):       #идём по столбцам
        #создаём белую кнопку цвет 1 на 1 цвет которой можно менять по клику
        buttons[i][j] = Button(width=1, height=1, bg='white', command=lambda x=i, y=j: clickButton(x, y))
        #размещаем эту кнопку в окне
        buttons[i][j].grid(row=i, column=j)

#запускаем окно
root.mainloop()
