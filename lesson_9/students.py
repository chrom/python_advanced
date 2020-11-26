# 1) Создать базу данных студентов
# (ФИО, группа, оценки, куратор студента, факультет).
# Описать метод для вывода отличников по каждому факультету.
# Описать метод для вывода всех студентов определенного куратора.
import mongoengine as me
from student_model import Student
from generate_students_db import generate_student
from functools import reduce


def average(lst: list) -> int:
    return reduce(lambda a, b: a + b, lst) / len(lst)


me.connect(host='mongodb://test:test@localhost:27017/test')


def create_users():
    generate_student(10)


def get_best_by_faculty(faculty: str) -> tuple:
    students = Student.objects.filter(faculty=faculty)
    s: Student
    best = {}
    for s in students:
        best[int(average(s.rating))] = s

    best = sorted(best.items())
    return best[-1]


def get_students_by_curator(curator: str):
    students = Student.objects.filter(curator=curator)
    s: Student
    for s in students:
        print(s._data)


if __name__ == '__main__':
    # create_users()
    # get_students_by_curator('Sir James Paul McCartney')
    print(get_best_by_faculty('CS-101'))
