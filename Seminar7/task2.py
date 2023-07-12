# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.
from random import choice, randint

LET_VOV = 'euoayi'
LET_CO = 'qwrtpsdfghjklzxcvbnm'


def pse_gen(num_nam: int, file_name: str) -> None:
    with open(file_name, 'a', encoding='utf-8') as f:
        for _ in range(num_nam):
            name = ''.join(choice(LET_VOV) if i in (1, 4, 6) else choice(LET_CO)
                           for i in range(randint(4, 7)))
            f.write(name.capitalize() + '\n')


if __name__ == '__main__':
    pse_gen(10, 'task2.txt')
