# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

items_for = {'crackers': 3, 'rabbit costume': 10, 'gum': 5, 'magic wand': 5, 'teddy bear': 8}
backpack = []
size = 30
for key, value in items_for.items():
    if value <= size:
        size -= value
        backpack.append(key)
print(backpack)
