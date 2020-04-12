from tkinter import *
from random import randrange

root = Tk()

BX_BEGIN = 360
BY_BEGIN = 10
EX_BEGIN = 390
EY_BEGIN = 40

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
    def __init__(self, master, text, row, column, cspan, sticky, command=None):
        self.b = Button(text=text, command=command)
        self.b.grid(row=row, column=column, columnspan=cspan, sticky=sticky, padx=5)

cells = []
values = []

for i in range(6):
    cells.append(Input(root, 0, i+1))


def get_values():
    values = []
    for cell in cells:
        values.append(int(cell.i.get()))
    
    c.delete("all")
    first = OperationalArray(values, BX_BEGIN, BY_BEGIN, EX_BEGIN, EY_BEGIN, 0)
    first.returnArrow(first.merged, 550, 25, 580, 25)
    print(values)


def generate():
    values = []
    for cell in cells:
        num = randrange(10)
        values.append(num)
        cell.i.delete(0)
        cell.i.insert(0,num)
    
    c.delete("all")
    first = OperationalArray(values, BX_BEGIN, BY_BEGIN, EX_BEGIN, EY_BEGIN, 0)
    first.returnArrow(first.merged, 550, 25, 580, 25)
    print(values)


loadb = ManageButton(root, "Загрузить", row=1, column=1, cspan=3, sticky=W, command=get_values)
randomb = ManageButton(root, "Сгенерировать", row=1, column=4, cspan=3, sticky=E, command=generate)

startb = ManageButton(root, "Старт", row=2, column=1, cspan=3, sticky=W)
stopb = ManageButton(root, "Сброс", row=2, column=4, cspan=3, sticky=W)

forwardb = ManageButton(root, "Вперед", row=3, column=5, cspan=2, sticky=E)
reversb = ManageButton(root, "Назад", row=3, column=1, cspan=2, sticky=W)
pauseb = ManageButton(root, "Пауза", row=3, column=3, cspan=2, sticky=None)



# опорный элемент выбираем всегда первый
class OperationalArray:
    def __init__(self, arr, bx, by, ex, ey, level):
        self.level = level
        self.build(arr, bx, by, ex, ey)
        self.merged = self.divide(arr, bx, by, ex, ey)
        
    
    def build(self, arr, bx, by, ex, ey):
        pivot = 'orange'
        if len(arr) < 2:
            return
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
        if len(arr) < 2:
            return arr
        c.create_text((bx + (len(arr) / 2) * 30), by+60, text=arr[0], font="Verdana 14")

        less = [i for i in arr[1:] if i <= arr[0]]
        greater = [i for i in arr[1:] if i > arr[0]]

        if self.level == 0:
            self.level = 2
        else:
            self.level = self.level * 2

        # сдивигаем меньший массив
        bx_l = bx - (BX_BEGIN // self.level)
        by_l = by + 45
        ex_l = bx_l + 30
        ey_l = by_l + 30

        one = None
        if len(less) == 1:
            one = "green"

        for i in less:
            c.create_rectangle(bx_l, by_l, ex_l, ey_l, outline=one)
            c.create_text(bx_l+15, by_l+15, text=i, font="Verdana 14")
            pivot = None
            bx_l += 30
            ex_l += 30

        bx_g = (bx +  (BX_BEGIN // self.level))
        by_g = by + 45

        ex_g = bx_g + 30
        ey_g = by_g + 30

        one = None
        if len(greater) == 1:
            one = "green"

        for i in greater:
            c.create_rectangle(bx_g, by_g, ex_g, ey_g, outline=one)
            c.create_text(bx_g+15, by_g+15, text=i, font="Verdana 14")
            bx_g += 30
            ex_g += 30
        
        return OperationalArray(less, (BX_BEGIN // self.level), by_l+60, (BX_BEGIN // self.level) + 30, ey_l+60, self.level).merged + [arr[0]] + OperationalArray(greater, (bx +  (bx // 2)), by_g+60, (bx +  (bx // 2)) + 30, ey_g+60, self.level).merged
        


# теперь на холсте нужно нарисовать массив с данными
# после этого нужно показать на первый (опорный элемент)
# и то как массив делится на два

sortArray = [4, 1, 2, 5, 3, 6]

first = OperationalArray(sortArray, BX_BEGIN, BY_BEGIN, EX_BEGIN, EY_BEGIN, 0)
first.returnArrow(first.merged, 550, 25, 580, 25)



# теперь нужно сделать отступ вниз и отобразить там опорный элемент
# слева от него отобразить массив с меньшими значениями а справа - с большими

root.mainloop()
