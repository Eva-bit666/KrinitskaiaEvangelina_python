import os, time
#Цвета для флага и узора
BLUE = '\u001b[44m'
WHITE = '\x1b[48;5;15m'
RED = '\u001b[41m'
BLACK = '\u001b[40m'
END = '\u001b[0m'
#Рисуем флаг Франции: 15 строк и три вертикальные полосы
def draw_flag():
    for i in range(15):
        print(f'{BLUE}      {WHITE}      {RED}      {END}')
#Рисуем повторяющийся узор 6 на 10 клеток
def draw_pattern():
    for row in range(6):
        line = " "
        for col in range(10):
            if (row+col) % 2 == 0:
                line = line + BLACK + "  "
            else:
                line = line + WHITE + "  "
        print(f'{line}{END}')
height = 9
width = 20

#Считаем координаты точек функции y=x^2
ys = []
for col in range(width):
    y = col ** 2
    ys.append(y)

max_y = max(ys)
#Создание пустой сетки под график
grid = []
for row in range(height):
    line = []
    for col in range(width):
        line.append(' ')
    grid.append(line)
#Расставление звёздочек по сетке согласно значениям y
for col in range(width):
    y = ys[col]
    row = height - 1 - round(y / max_y * (height - 1))
    grid[row][col] = "*"
#Печатаем готовый график по сетке
def draw_function():
    for row in grid:
        line_text = ""
        for symbol in row:
            line_text = line_text + symbol
        print(line_text)
def draw_diagram():
    #Чтение чисел из sequence.txt
    file = open("sequence.txt", "r")
    numbers=[]
    for text_line in file:
        numbers.append(float(text_line))
    file.close()

    count_neg = 0
    count_pos = 0

     #Считаем сколько чисел меньше и больше нуля
    for n in numbers:
        if n < 0:
            count_neg = count_neg + 1
        if n > 0:
            count_pos = count_pos + 1

    print(f"Меньше 0: {count_neg}")
    print(f"Больше 0: {count_pos}")
    total = len(numbers)
    percent_neg = count_neg / total * 100
    percent_pos = count_pos / total * 100
    print(f"Меньше 0: {round(percent_neg, 1)}%")
    print(f"Больше 0: {round(percent_pos, 1)}%")
    #Перевод процентов в длину полосок
    bar_neg = round(percent_neg / 100 * 50)
    bar_pos = round(percent_pos / 100 * 50)
    print(f'{RED}{" " * bar_neg}{END}')
    print(f'{BLUE}{" " * bar_pos}{END}')
#Анимация кадров с очисткой консоли
frames = [draw_flag, draw_pattern, draw_function, draw_diagram]
draw_flag()
draw_pattern()
draw_function()
draw_diagram()

for frame in frames:
    os.system('clear')
    frame()
    time.sleep(10)
