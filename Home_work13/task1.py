# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.

import csv
import json
from pathlib import Path


class CSVConversionError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'CSV Ошибка конвертации: {self.message}'


class FileReadError(CSVConversionError):
    def __init__(self, file_path):
        self.file_path = file_path
        message = f'Ошибка чтения файла: {file_path}'
        super().__init__(message)


class FileWriteError(CSVConversionError):
    def __init__(self, file_path):
        self.file_path = file_path
        message = f'Ошибка записи файла: {file_path}'
        super().__init__(message)


def csv_to_json(file_out: Path, file_in: Path) -> None:
    try:
        json_list = []
        with open(file_out, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for i, row in enumerate(reader):
                if i == 0:
                    continue
                json_dict = {}
                level, user_id, name = row
                json_dict['level'] = int(level)
                json_dict['id'] = user_id.zfill(10)
                json_dict['name'] = name.title()
                json_dict['hash'] = hash(f'{user_id}{name}')
                json_list.append(json_dict)

        try:
            with open(file_in, 'w', encoding='utf-8') as f:
                json.dump(json_list, f, indent=2)
        except IOError:
            raise FileWriteError(file_in)

    except IOError:
        raise FileReadError(file_out)


if __name__ == '__main__':
    try:
        csv_to_json(Path('out.csv'), Path('json_in.json'))
    except CSVConversionError as e:
        print(e)