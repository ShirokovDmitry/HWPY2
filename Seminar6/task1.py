

from random import randint as rnd

def find_num(min_num: int, max_num: int, counts: int) -> bool:
    ran_num = rnd(min_num, max_num)
    count = 1
    for count in range(counts):
        find_now = int(input(f'Введите число от {min_num} до {max_num} '))
        if find_now > ran_num:
            print('Число меньше')
        elif find_now < ran_num:
            print('Число больше')
        else:
            print('Вы смогли отгадать')
            return True

    print(f'Попытоки кончились ({count + 1})\n Число: {ran_num}')
    return False

if __name__ == '__main__':
    find_num(10, 100, 10)