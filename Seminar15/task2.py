# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

import os.path
from os import listdir
import logging
from collections import namedtuple

logging.basicConfig(filename='log6.log', level=logging.INFO, encoding='utf-8')
logger = logging.getLogger(__name__)

file = namedtuple(typename='file', field_names='file_path, ext, folder, parent_folder')


def directory_info(file_p: str):
    files_list = listdir(file_p)
    p = file_p.split(os.path.sep)
    for item in files_list:
        if os.path.isfile(os.path.join(file_p, item)):
            temp = item.split('.')
            obj = file(temp[0], temp[1], False, p[-1])
        else:
            obj = file(item, '', True, p[-1])
        logger.info(obj)


directory_info(r'E:\GitLibrary\Pycharm\Seminar15')
