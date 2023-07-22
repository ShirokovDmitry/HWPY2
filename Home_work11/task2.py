# Создайте класс Матрица. Добавьте методы для:
# ○ вывода на печать,
# ○ сравнения,
# ○ сложения,
# ○ *умножения матриц


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(str(element) for element in row) + "\n"
        return matrix_str

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.data == other.data
        return False

    def __add__(self, other):
        if isinstance(other, Matrix) and self.rows == other.rows and self.columns == other.columns:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        else:
            raise ValueError("Матрицы должны иметь одинаковые размеры")

    def __mul__(self, other):
        if isinstance(other, Matrix) and self.columns == other.rows:
            result = Matrix(self.rows, other.columns)
            for i in range(self.rows):
                for j in range(other.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * other.data[k][j]
            return result
        else:
            raise ValueError("Матрицы должны иметь одинаковые размеры")


if __name__ == '__main__':
    matrix1 = Matrix(2, 3)
    matrix1.data = [[1, 2, 3], [4, 5, 6]]

    matrix2 = Matrix(2, 3)
    matrix2.data = [[7, 8, 9], [10, 11, 12]]

    matrix3 = Matrix(3, 2)
    matrix3.data = [[2, 3], [4, 5], [6, 7]]

    print(f'Матрица 1\n{matrix1}')
    print(f'Матрица 2\n{matrix2}')
    print(f'Матрица 3\n{matrix3}')

    print(f'Сравнение matrix1 и matrix2: {matrix1 == matrix2}\n')

    matrix_sum = matrix1 + matrix2
    print(f'Сложение matrix1 и matrix2:\n{matrix_sum}')

    matrix_product = matrix1 * matrix3
    print(f'Умножение matrix1 и matrix3:\n{matrix_product}')
