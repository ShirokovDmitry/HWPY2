# Задание №7
# ✔ Пользователь вводит строку текста.
# ✔ Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# ✔ Результат сохраните в словаре, где ключ —
# символ, а значение — частота встречи
# символа в строке.
# ✔ Обратите внимание на порядок ключей.
# Объясните почему они совпадают
# или не совпадают в ваших решениях.


letters = 'gdhgdhgdhgdhgdhhhg'

new_let = {}
for letter in letters:
    new_let[letter] = new_let.get(letter, 0) + 1
print(new_let)

a = 'gdhgdhgdhgdhgdhhhg'

b = dict((letter, a.count(letter)) for letter in set(a))
print(b)