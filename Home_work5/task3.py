# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib(n: int) -> list[int]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print(*(fib(40)))