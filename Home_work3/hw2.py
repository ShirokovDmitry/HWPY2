# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

array = ([2, 5, 1, 2, 3, 3, 4, 1, 5])
array2 = set()
for index in array:
    counter = array.count(index)
    if counter > 1:
        array2.add(index)
print(array2)