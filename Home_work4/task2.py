# Напишите функцию для транспонирования матрицы

def matrix_t(*a_list: list[[int]]) -> list[()] | str:
    trans_m = True
    list_m = len(a_list[0])
    for a in list(a_list):
        if len(a) != list_m:
            trans_m = False
    if trans_m:
        return list(zip(*a_list))

if __name__ == '__main__':
    print(matrix_t([1, 1, 1], [2, 2, 2], [3, 3, 3]))

