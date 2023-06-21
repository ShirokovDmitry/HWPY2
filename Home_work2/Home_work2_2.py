# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

hex_num = int(input('Введите число: '))
Hex16 = "0x"
list_16 = []
re_16 = None
div_16 = None
list_16.append(str(hex_num % 16))
re_16 = hex_num % 16
div_16 = hex_num // 16

while div_16 != 0:
    re_16 = div_16 % 16
    div_16 //= 16
    list_16.append(str(re_16))
list_16.reverse()

for i in list_16:
    if i == "10":
        Hex16 += "a"
    elif i == "11":
        Hex16 += "b"
    elif i == "12":
        Hex16 += "c"
    elif i == "13":
        Hex16 += "d"
    elif i == "14":
        Hex16 += "e"
    elif i == "15":
        Hex16 += "f"
    else:
        Hex16 += i

print(Hex16)
print(hex(hex_num))