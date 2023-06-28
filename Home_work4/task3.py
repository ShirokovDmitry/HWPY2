# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.


def dict_item(**kwargs):
    stuff = dict()
    for key, values in kwargs.items():
        if isinstance(values, (list, dict, set,bytearray)):
            values = str(values)
        stuff[values] = key
    return stuff

if __name__ == '__main__':
    print(dict_item(ball='foot', stick='bit', form='circle'))