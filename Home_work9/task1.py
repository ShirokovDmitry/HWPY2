# Задание №6
# Доработайте прошлую задачу добавив декоратор wraps в
# каждый из декораторов.

import os
import json
from typing import Callable
from random import randint
from functools import wraps


def count_f(num: int = 1):
    def deco(func):
        results = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                results.append(func(*args, **kwargs))
            return results

        return wrapper

    return deco


def logger(func):
    file_name = f'{func.__name__}.json'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
    else:
        data = []

    @wraps(func)
    def wrapper(*args, **kwargs):
        json_dict = {'args': args, **kwargs}
        result = func(*args, **kwargs)
        json_dict['result'] = result
        data.append(json_dict)

        with open(file_name, 'w', encoding='utf-8') as f1:
            json.dump(data, f1)

        return result

    return wrapper


def check_parametr(func):
    MIN_NUM = 1
    MAX_NUM = 100
    MIN_COUNT = 1
    MAX_COUNT = 10

    @wraps(func)
    def wrapper(number: int, count: int, *args, **kwargs):
        if number > MAX_NUM or number < MIN_NUM:
            number = randint(MAX_NUM, MAX_NUM)
        if count > MIN_COUNT or count < MIN_COUNT:
            count = randint(MIN_COUNT, MAX_COUNT)
        result = func(number, count, *args, **kwargs)
        return result

    return wrapper


@count_f(3)
@check_parametr
@logger
def gess_number(number: int, count: int) -> Callable[[], None]:
    for i in range(1, count + 1):
        print(f'Порытка № {count}')
        num_input = int(input('Введите число: '))
        if num_input == number:
            return 'Вы угадали!'
        elif num_input < number:
            print('Число больше')
        else:
            print('Число меньше')
    return 'Вы не угадали'


if __name__ == '__main__':
    game = gess_number(25, 5)
    print(game)
