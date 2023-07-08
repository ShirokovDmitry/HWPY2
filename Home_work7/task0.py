from string import ascii_letters
from random import randint, choices, randbytes


def gen_files(data: dict):
    for key, value in data.items():
        create_file(key, amount_file=value)


def create_file(extension: str, min_len_name: int = 2, max_len_name: int = 5,
                min_size_file: int = 256, max_size_file: int = 4096, amount_file: int = 5) -> None:
    for _ in range(amount_file):
        len_name = randint(min_len_name, max_len_name)
        file_name = ''.join(choices(ascii_letters, k=len_name)) + extension
        size = randint(min_size_file, max_size_file)
        with open(file_name, 'wb') as f:
            f.write(randbytes(size))


if __name__ == '__main__':
    my_dict = {'.jpg': 2, '.png': 2, '.svg': 2, '.pdf': 2}
    gen_files(my_dict)
    create_file('.txt')