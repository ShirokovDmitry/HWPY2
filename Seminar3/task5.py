# Задание №5
# ✔ Создайте вручную список с повторяющимися целыми числами.
# ✔ Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# ✔ Нумерация начинается с единицы.

TWO = 2
array = [1, 1, 2, 1, 3, 5, 6, 7, 8, 2, 3, 4, 6, 6, 5, 4]
array2 = []
# for i in range(len(array)):
#     if array[i] % TWO == 1:
#         array2.append(i + 1)
for i, item in enumerate(array, start=1):
    if item % TWO == 1:
        array2.append(i)

print(array2)


