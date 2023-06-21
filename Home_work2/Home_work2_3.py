# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

print("Напишите дроби 'a/b'")

fst_num = input("Первое число: ")
sec_num = input("Второе число: ")
count = 0
a_1 = ""
a_2 = ""
b_1 = ""
b_2 = ""

while count < len(fst_num):
    a_1 += fst_num[count]
    count += 1
    if fst_num[count] == "/":
        count += 1
        while count < len(fst_num):
            a_2 += fst_num[count]
            count += 1
count = 0

while count < len(sec_num):
    b_1 += sec_num[count]
    count += 1
    if sec_num[count] == "/":
        count += 1
        while count < len(sec_num):
            b_2 += sec_num[count]
            count += 1

print("Произведение дробей равно :", int(a_1) * int(b_2), "/", int(a_2) * int(b_1))

a1 = ""
b1 = ""
a2 = ""
b2 = ""
if a_2 != b_2:
    a1 = int(a_1) * int(b_2)
    b1 = int(b_1) * int(a_2)
    a2 = int(a_2) * int(b_2)
    b2 = int(b_2) * int(a_2)
    print("Сумма дробей равна :", a1 + b1, "/", a2)

if a_2 == b_2:
    if int(a_1) + int(b_1) == int(a_2):
        print("Cумма дробей равна единице")
    else:
        print("Cумма дробей равна :", int(a_1) + int(b_1), "/", int(a_2))