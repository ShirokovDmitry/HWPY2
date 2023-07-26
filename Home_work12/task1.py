# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.

import csv


class NameDescriptor:
    def __get__(self, instance, owner):
        return instance._name

    def __set__(self, instance, value):
        if not all(part.isalpha() for part in value.split()):
            raise ValueError("Имя должно содержать только буквы")
        instance._name = value.title()


class Student:
    name = NameDescriptor()

    def __init__(self, subjects_file):
        self.subjects = self.load_subjects(subjects_file)
        self.grades = {subject: {'scores': [], 'tests': []} for subject in self.subjects}

    def load_subjects(self, subjects_file):
        with open(subjects_file, 'r') as file:
            reader = csv.reader(file)
            subjects = next(reader)
        return subjects

    def add_grade(self, subject, score, test_result):
        if subject not in self.subjects:
            raise ValueError(f"Недопустимое название'{subject}'")
        if score < 2 or score > 5:
            raise ValueError("Оценка может быть от 2 до 5")
        if test_result < 0 or test_result > 100:
            raise ValueError("Результат теста может быть от 0 до 100")

        self.grades[subject]['scores'].append(score)
        self.grades[subject]['tests'].append(test_result)

    def average_test_score(self, subject):
        scores = self.grades[subject]['scores']
        if not scores:
            return None
        return sum(scores) / len(scores)

    def overall_average_score(self):
        all_scores = []
        for subject in self.subjects:
            all_scores.extend(self.grades[subject]['scores'])

        if not all_scores:
            return None
        return sum(all_scores) / len(all_scores)


if __name__ == '__main__':
    student = Student('subjects.csv')
    print(student.subjects)

    student.name = 'John Smith Silverstone'
    print(student.name)

    student.add_grade('Math', 4, 90)
    student.add_grade('History', 5, 95)
    student.add_grade('Physics', 4, 84)

    print(student.average_test_score('Math'))
    print(student.average_test_score('History'))
    print(student.average_test_score('Physics'))
    print(student.overall_average_score())

