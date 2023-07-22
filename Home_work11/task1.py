# Добавьте ко всем задачам с семинара строки документации и методы вывода
# информации на печать.
from time import time


class My_string(str):
    """
    Класс Моя Строка, где:
    будут доступны все возможности str дополнительно хранятся имя
    автора строки и время создания (time.time)
    """

    def __new__(cls, value: str, author_name: str):
        instance = super().__new__(cls, value)
        instance.author_name = author_name
        instance.time_created = time()
        return instance

    def print_info(self):
        """
        Print information about the My_string instance.
        """
        print(f"Value: {self}")
        print(f"Author: {self.author_name}")
        print(f"Time Created: {self.time_created}")


if __name__ == '__main__':
    new_str = My_string('Hello', 'John')
    new_str.print_info()
