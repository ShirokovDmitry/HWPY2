# Задание №1
# ✔ Вручную создайте список с целыми числами, которые
# повторяются. Получите новый список, который содержит
# уникальные (без повтора) элементы исходного списка.
# ✔ *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.


array = [1, 1, 2, 1, 3, 5, 6, 7, 8, 2, 3, 4, 6, 6, 5, 4]
array1 = []
for item in array:
    if item not in array1:
        array1.append(item)

print(array1)
array2 = list(set(array))
print(array2)