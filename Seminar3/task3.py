# Задание №3
# Погружение в Python | Коллекции
# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (1, 2.56, 'dufvsfjsv', 3.987, 9, 'ufygrufyg', False)
words = {}
for item in data:
    types1 = type(item)
    if types1 in words:
        words[types1].append(item)
    else:
        words[types1] = [item]
print(words)