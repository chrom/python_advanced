# 2) Создать модуль, который будет заполнять базу данных
# случайными валидными значениями (минимум 100 студентов).

import mongoengine as me
from faker import Faker
import random
from student_model import Student


def generate_student(qty: int = 100):
    fake: Faker = Faker()
    me.connect(host='mongodb://test:test@localhost:27017/test')

    faculty = ['DB', 'CS-101']
    curator = ['Antonio Lucio Vivaldi',
               'Johann Sebastian Bach',
               'Sir Arthur Ignatius Conan Doyle',
               'Sir James Paul McCartney',
               'Sir James Paul McCartney',
               ]
    Student.drop_collection()
    for i in range(qty):
        user = Student(fio=fake.name(),
                       group=str(random.randint(0, 9)),
                       rating=random.sample(range(1, 101), 10),
                       curator=random.sample(curator, 1)[0],
                       faculty=random.sample(faculty, 1)[0],
                       email=fake.email(),
                       address=fake.address()
                       )
        user.save()


if __name__ == '__main__':
    generate_student()
