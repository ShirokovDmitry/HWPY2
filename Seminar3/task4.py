# Задание №4
# ✔ Создайте вручную список с повторяющимися элементами.
# ✔ Удалите из него все элементы, которые встречаются дважды.

array = [1, 1, 2, 1, 3, 5, 6, 7, 8, 2, 3, 4, 6, 6, 5, 4]
TWO = 2
for item in set(array):
    if array.count(item) == TWO:
        for _ in range(TWO):
            array.remove(item)
print(array)