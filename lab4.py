#Вариант 1
from itertools import combinations
import numpy as np
item_s={
    'r':(3, 25),
    'p':(2,15),
    'a':(2,15),
    'm':(2,20),
    'i':(1,5),
    'k':(1,15),
    'x':(3,20),
    't':(1,25),
    'f':(1,15),
    'd':(1,10),
    's':(2,20),
    'c':(2,20),
}
CAPACITY = 8
start_points = 15
print('Проверка доп условия - болезни нет - ингалятор и антидот не требуются')
total_points = sum(v for _, v in item_s.values())
def get_size_value(stuffdict):
    #Разбиение на два отдельных списка
    size = [stuffdict[itm][0] for itm in stuffdict]
    value = [stuffdict[itm][1] for itm in stuffdict]
    return size, value
def get_memtable(stuffdict, capacity):
    size, value = get_size_value(stuffdict)
    n = len(value)

    table = np.array([[0 for _ in range(capacity + 1)] for _ in range(n + 1)])

    for row in range(n + 1):
        for colmn in range(capacity + 1):

            if row == 0 or colmn == 0:
                table[row][colmn] = 0
            elif size[row - 1] <= colmn:
                table[row][colmn] = max(table[row - 1][colmn],
                                        value[row - 1] + table[row - 1][colmn - size[row - 1]])
    else:
                table[row][colmn] = table[row - 1][colmn]

    return table, size, value

def get_selected_item_list(stuffdict, capacity):
    table, size, value = get_memtable(stuffdict, capacity)
    n = len(value)
    colmn = capacity
    res = table[n][colmn]

    item_list_size_value = []

    for i in range(n, 0, -1):

        if res <= 0:
            break

        if res == table[i-1][colmn]:
            continue

        else:
            item_list_size_value.append((size[i-1], value[i-1]))
            res -= value[i-1]
            colmn -= size[i-1]

    key_list = []
    for search in item_list_size_value:
        for key, val in stuffdict.items():
            if search == val and key not in key_list:
                key_list.append(key)
                break

    return key_list, item_list_size_value
keys_opt, values_opt = get_selected_item_list(item_s, CAPACITY)

print(keys_opt)
print(values_opt)
def build_inventory(keys, values, rows, cols):
    #Разложение предметов
    flat = []
    for code, (size, value) in zip(keys, values):
        flat.extend([code] * size)
    while len(flat) < rows * cols:
        flat.append('-')

    grid = [flat[r * cols:(r + 1) * cols] for r in range(rows)]
    return grid
def print_inventory(grid):
    for r in grid:
        print (','.join(f'[{c}]' for c in r))
grid = build_inventory(keys_opt, values_opt, 2, 4)
print_inventory(grid)
def final_score(values, start, total):
    taken = sum(v for _, v in values)
    not_taken = total - taken
    return start + taken - not_taken
score = final_score(values_opt, start_points, total_points)
print(f'Итоговые очки выживания: {score}')

if score > 0:
    print('Условие выполнено: ура, всё получилось!')
else:
    print('Условие не выполнено, провал')
#Доп задание
print('Инвентарь в 7 ячеек')
keys_7, values_7 = get_selected_item_list(item_s, 7)
print(keys_7)
print(values_7)
score_7 = final_score(values_7, start_points, total_points)
print(f'Итоговые очки выживания(7 ячеек): {score_7}')

if score_7 > 0:
    print('Решение с положительным итогом есть')
elif score_7 == 0:
    print('Строгого положительного итога не достичь, максимум равен нулю')
else:
    print('Решения с положительным итогом нет')
def find_all_positive(stuffdict, capacity, start, total):
    keys = list(stuffdict.keys())
    n = len(keys)
    results = []

    for r in range(n + 1):
        for combo in combinations(keys, r):
            weight = sum(stuffdict[c][0] for c in combo)
            if weight > capacity:
                continue
            taken_values = [(stuffdict[c][0], stuffdict[c][1]) for c in combo]
            score = final_score(taken_values, start, total)
            if score > 0:
                results.append((combo, score))

    return results
print ('Все комбинации с положительным итогом')
all_positive = find_all_positive(item_s, CAPACITY, start_points, total_points)

for combo, s in sorted(all_positive, key=lambda x: -x[1]):
    print(f'{combo}: {s}')