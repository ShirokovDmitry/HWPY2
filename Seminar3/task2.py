# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

number = input('Введите')
if number.isdecimal() and int(number) > 0:
    print(f'{number} Это целое положительное число')
elif number.count('.') == 1 and number.count('-') < 2 and number.replace('.', '').replace('-', '').isdecimal():
    print(f'{number} Это целое вещественное число')
elif number.isupper():
    print(number.lower())
else:
    print(number.lower())