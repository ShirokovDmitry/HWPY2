# Задание №7
# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.
import csv
import pickle
import os


def read_csv(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data


def convert_to_pickle_string(data):
    pickled_data = pickle.dumps(data)
    pickle_string = pickled_data.decode('latin1')
    return pickle_string


csv_file_path = os.getcwd()
file_name = 'data.csv'
file_path = os.path.join(csv_file_path, file_name)
csv_data = read_csv(file_path)
pickle_string = convert_to_pickle_string(csv_data)

if __name__ == '__main__':
    print(pickle_string)