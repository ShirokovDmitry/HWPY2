# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

# Напишите функцию для транспонирования матрицы

import logging
import argparse


def matrix_t(*a_list: list[[int]]) -> list[()] | str:
    trans_m = True
    list_m = len(a_list[0])
    for a in list(a_list):
        if len(a) != list_m:
            trans_m = False
    if trans_m:
        return list(zip(*a_list))
    else:
        raise ValueError("Error: Матрица не прямоугольная!")


if __name__ == '__main__':
    logging.basicConfig(filename='matrix_t.log', level=logging.ERROR, encoding='utf-8',
                        format='%(asctime)s %(levelname)s %(message)s')
    logger = logging.getLogger()

    parser = argparse.ArgumentParser(description='Matrix Transpose')
    parser.add_argument('matrix', metavar='N', type=int, nargs='+',
                        help='Элементы матрицы разделены пробелами: 1 1 1 2 2 2 3 3 3')

    try:
        args = parser.parse_args()
        a_lists = [args.matrix[i:i + 3] for i in range(0, len(args.matrix), 3)]
        result = matrix_t(*a_lists)
        print(result)
    except:
        logger.exception("An error occurred:")
