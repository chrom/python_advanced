# Создайте класс ПЕРСОНА с абстрактным методом,
# позволяющим вывести  на экран информацию о персоне,
# а также реализовать обычный метод определения возраста (в текущем году).
# Создайте дочерние классы:
# АБИТУРИЕНТ (фамилия, дата рождения, факультет),
# СТУДЕНТ (фамилия, дата рождения, факультет, курс),
# ПРЕПОДАВАТЕЛЬ (фамилия, дата рождения, факультет, должность, стаж), со своими методами возврата информации.
# Создайте список из объектов персон, вывести информацию о
# каждом объекте, а также организуйте поиск персон, чей возраст попадает в
# заданный с клавиатуры диапазон.

from abc import ABC, abstractmethod
import datetime


class Person(ABC):

    def __init__(self, name: str, db: datetime):
        self._name = name
        self._db = db

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def db(self) -> datetime:
        return self._db

    @db.setter
    def db(self, value: datetime):
        self._db = value

    @abstractmethod
    def get_person_data(self, object) -> str:
        pass

    def get_age(self) -> int:
        today = datetime.date.today()
        return today.year - self._db.year - ((today.month, today.day) < (self._db.month, self._db.day))


class Entrance(Person):
    def __init__(self, name: str, db: datetime, faculty: str):
        super().__init__(name, db)
        self._faculty_name = faculty

    @property
    def faculty_name(self) -> str:
        return self._faculty_name

    @faculty_name.setter
    def faculty_name(self, value: str):
        self._faculty_name = value

    # Обращение к подобъекту Person
    #     return f'Entrance personal data: Name {Person.name}, full years: {self.get_age()}, faculty: {self.faculty}'
    def get_person_data(self) -> str:
        return f'Entrance personal data: \n\t Name: \t\t {self.name}\n\t Full years: \t {self.get_age()}\n\t Faculty: \t {self.faculty_name}'


dob = datetime.date(1982, 12, 10)

object1 = Entrance('John Smite', dob, 'CS')
print(object1.get_person_data())


class Student(Entrance):
    def __init__(self, name: str, db: datetime, faculty: str, course: int):
        super().__init__(name, db, faculty)
        self._course_number = course

    @property
    def course_number(self) -> int:
        return self._course_number

    @course_number.setter
    def course_number(self, value: int):
        self._course_number = value

    def get_person_data(self) -> str:
        return f'Student personal data: \n\t' \
               f'Name: \t\t {self.name}\n\t' \
               f'Full years: \t {self.get_age()}\n\t' \
               f'Faculty: \t {self.faculty_name}\n\t' \
               f'Course number: \t {self.course_number}'


dob = datetime.date(1980, 10, 10)
object2 = Student('John Doe', dob, 'CS', 2)
print(object2.get_person_data())


# //(фамилия, дата рождения, факультет, должность, стаж)
class Teacher(Person):
    def __init__(self, name: str, db: datetime, faculty: str, position: str, experience: int):
        super().__init__(name, db)
        self._faculty_name = faculty
        self._position = position
        self._experience = experience

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str):
        self._position = value

    @property
    def experience(self) -> int:
        return self._experience

    @experience.setter
    def experience(self, value: int):
        self._experience = value

    @property
    def faculty_name(self) -> str:
        return self._faculty_name

    @faculty_name.setter
    def faculty_name(self, value: str):
        self._faculty_name = value

    def get_person_data(self) -> str:
        return f'Teacher personal data: \n\t' \
               f'Name: \t\t {self.name}\n\t' \
               f'Full years: \t {self.get_age()}\n\t' \
               f'Faculty: \t {self.faculty_name}\n\t' \
               f'Position: \t {self.position}\n\t' \
               f'Experience: \t {self.experience}\n\t'


dob = datetime.date(1970, 10, 1)
object3 = Teacher('Wiesmann', dob, 'CS', 'Professor', 20)
print(object3.get_age())

dob = datetime.date(1972, 2, 1)
object4 = Teacher('Ismann', dob, 'CS', 'Professor', 18)
print(object4.get_age())

dob = datetime.date(1974, 5, 23)
object5 = Teacher('Coufmann', dob, 'CS', 'Professor', 16)
print(object5.get_age())

dob = datetime.date(1977, 8, 11)
object6 = Teacher('Normann', dob, 'CS', 'Professor', 13)
print(object6.get_age())

teacher_list = [object3, object4, object5, object6]


# TODO: know how set args in filter
# low = int(input("Low limit: "))
# high = int(input("High limit: "))


def filter_teacher(first: Teacher, low: int = 0, high: int = 0) -> bool:
    return 44 < first.get_age() < 49


for_printing = filter(filter_teacher, teacher_list)
for i in for_printing:
    print(i.get_person_data())
