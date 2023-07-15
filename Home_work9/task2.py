# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке.
# 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
import csv
import json
import random


def quadratic_equation_solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None


def csv_to_json_decorator(func):
    def wrapper(file_name):
        data = []
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                numbers = [float(num) for num in row]
                roots = func(*numbers)
                data.append({
                    'input': numbers,
                    'roots': roots
                })
        with open('data.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    return wrapper


@csv_to_json_decorator
def process_equations(a, b, c):
    return quadratic_equation_solver(a, b, c)


def generate_csv_file(file_name, num_rows):
    with open(file_name, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        for _ in range(num_rows):
            row = [random.randint(1, 10) for _ in range(3)]
            csv_writer.writerow(row)


if __name__ == '__main__':
    generate_csv_file('input.csv', random.randint(100, 1000))
    process_equations('input.csv')
