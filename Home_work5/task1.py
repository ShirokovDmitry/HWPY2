# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.


text_path = r'C:\Users\The\Desktop\screen\screen.jpg'

def split_text(name_path: str) -> tuple():
    solit_list = name_path.split('\\')
    ex_path = solit_list[-1].split('.')
    path = '\\'.join(solit_list[0:-1])
    name = ex_path[0]
    expansion = ex_path[1]
    return path, name, expansion

print(split_text(text_path))