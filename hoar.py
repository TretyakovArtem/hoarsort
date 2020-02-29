from tkinter import *

root = Tk()

# слева разместим холст, на котором и будет визуализация
c = Canvas(width=900, height=700, bg='white')
c.grid(row=0, column=0, rowspan=5)

# 6 однострочных полей
# значения этих полей записываются в map

class Input:
    def __init__(self, master, row, column):
        self.i = Entry(width=5)
        self.i.grid(row=row, column=column)

class ManageButton:
    def __init__(self, master, text, row, column, cspan, sticky):
        self.b = Button(text=text)
        self.b.grid(row=row, column=column, columnspan=cspan, sticky=sticky, padx=5)

for i in range(6):
    Input(root, 0, i+1)
 
loadb = ManageButton(root, "Загрузить", row=1, column=1, cspan=3, sticky=W)
randomb = ManageButton(root, "Сгенерировать", row=1, column=4, cspan=3, sticky=E)

startb = ManageButton(root, "Старт", row=2, column=1, cspan=3, sticky=W)
stopb = ManageButton(root, "Сброс", row=2, column=4, cspan=3, sticky=W)

forwardb = ManageButton(root, "Вперед", row=3, column=5, cspan=2, sticky=E)
reversb = ManageButton(root, "Назад", row=3, column=1, cspan=2, sticky=W)
pauseb = ManageButton(root, "Пауза", row=3, column=3, cspan=2, sticky=None)

# опорный элемент выбираем всегда первый
class OperationalArray:
    def __init__(self, arr, bx, by, ex, ey):
        self.build(arr, bx, by, ex, ey)
        self.divide(arr, bx, by, ex, ey)
    
    def build(self, arr, bx, by, ex, ey):
        pivot = 'orange'
        for i in arr:
            c.create_rectangle(bx, by, ex, ey, outline=pivot)
            c.create_text(bx+15, by+15, text=i, font="Verdana 14")
            pivot = None
            bx += 30
            ex += 30

    # метод ля отрисовки возвращаемого значения
    def returnArrow(self, returnArr, bx, by, ex, ey):
        c.create_line(bx, by, ex, ey, arrow=LAST)

        bx = ex + 5
        by = ey - 15

        ex = bx + 30
        ey = by + 30
        for i in returnArr:
            c.create_rectangle(bx, by, ex, ey)
            c.create_text(bx+15, by+15, text=i, font="Verdana 14")
            pivot = None
            bx += 30
            ex += 30

    def divide(self, arr, bx, by, ex, ey):
        # отрисовать опорный элемент
        if len(arr) < 1:
            return
        c.create_text(bx+90, by+60, text=arr[0], font="Verdana 14")

        less = [i for i in arr[1:] if i <= arr[0]]
        greater = [i for i in arr[1:] if i > arr[0]]

        bx_l = bx - 30
        by_l = by + 45
        ex_l = bx_l + 30
        ey_l = by_l + 30

        for i in less:
            c.create_rectangle(bx_l, by_l, ex_l, ey_l)
            c.create_text(bx_l+15, by_l+15, text=i, font="Verdana 14")
            pivot = None
            bx_l += 30
            ex_l += 30

        bx = bx + 90 + 30
        by = by + 45

        ex = bx + 30
        ey = by + 30

        for i in greater:
            c.create_rectangle(bx, by, ex, ey)
            c.create_text(bx+15, by+15, text=i, font="Verdana 14")
            bx += 30
            ex += 30

        OperationalArray(less, bx-300, by+60, ex-300, ey+60)
        OperationalArray(greater, bx+50, by+60, ex+50, ey+60)
        




# теперь на холсте нужно нарисовать массив с данными
# после этого нужно показать на первый (опорный элемент)
# и то как массив делится на два


bx = 360
by = 10
ex = 390
ey = 40

sortArray = [4, 1, 6, 3, 5, 2]

first = OperationalArray(sortArray, bx, by, ex, ey)
first.returnArrow([1, 2, 3, 4, 5, 6], 550, 25, 580, 25)

# теперь нужно сделать отступ вниз и отобразить там опорный элемент
# слева от него отобразить массив с меньшими значениями а справа - с большими

root.mainloop()
