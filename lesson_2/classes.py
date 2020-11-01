# 1) Создать класс автомобиля. Создать классы легкового автомобиля
# и грузового. Описать в основном классе базовые атрибуты и методы
# для автомобилей. Будет плюсом если в классах наследниках
# переопределите методы базового класса.

class Car:
    __year_model: int
    __max_speed: int
    __brand: str
    __model: str

    def __init__(self, brand: str, model: str, year: int, max_speed: int):
        self.__brand = brand
        self.__model = model
        self.__max_speed = max_speed
        self.__year_model = year

    @property
    def brand(self) -> str:
        return self.__brand

    @brand.setter
    def brand(self, value: str):
        self.__brand = value

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, value: str):
        self.__model = value

    @property
    def year(self) -> int:
        return self.__year_model

    @year.setter
    def year(self, value: int):
        self.__year_model = value

    @property
    def max_speed(self) -> int:
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value: int):
        self.__max_speed = value

    def print_description(self):
        return "Current car: \nBrand: {}\nModel: {}\nYear of production: {} \nMax speed: {}".format(self.brand,
                                                                                                    self.model,
                                                                                                    self.year,
                                                                                                    self.max_speed)


class Sedan(Car):
    __car_body_type = 'Sedan'

    def print_description(self):
        return "Current car type is {}: \nBrand: {}\nModel: {}\nYear of production: {} \nMax speed: {}" \
            .format(self.__car_body_type, self.brand, self.model, self.year, self.max_speed)


class SUV(Sedan):
    __car_body_type = 'SUV'


gs350 = Car('Lexus', 'GS 350', 2020, 260)
is500 = Sedan('Lexus', 'IS 500', 2019, 270)
rx450 = SUV('Lexus', 'RX 450h', 2020, 220)

print(gs350.print_description())
print(is500.print_description())
print(rx450.print_description())
print('*'*30)


# 2) Создать класс магазина. Конструктор должен инициализировать
# значения: «Название магазина» и «Количество проданных
# товаров». Реализовать методы объекта, которые будут увеличивать
# кол-во проданных товаров, и реализовать вывод значения
# переменной класса, которая будет хранить общее количество
# товаров проданных всеми магазинами.



# 3 Создать класс точки, реализовать конструктор который
# инициализирует 3 координаты (Class): Определенный программистом тип данных.x, y, z).
# Реалзиовать методы для ). Реалзиовать методы для получения и изменения каждой из координат.
# Перегрузить для этого класса методы сложения, вычитания, деления умножения.
# Перегрузить один любой унарный метод.
# Ожидаемый результат: умножаю точку с координатами 1,2,3 на
# другую точку с такими же координатами, получаю результат 1, 4, 9.

class Dot:
    def __init__(self, x: int = 1, y: int = 1, z: int = 1):
        self._z = z
        self._y = y
        self._x = x

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        self._y = value

    @property
    def z(self) -> int:
        return self._z

    @z.setter
    def z(self, value: int):
        self._z = value

    def __add__(self, other):
        self._z += other.z
        self._y += other.y
        self._x += other.x
        return self

    def __iadd__(self, other):
        self._z += other.z
        self._y += other.y
        self._x += other.x
        return self

    def __isub__(self, other):
        self._z -= other.z
        self._y -= other.y
        self._x -= other.x
        return self

    def __sub__(self, other):
        self._z -= other.z
        self._y -= other.y
        self._x -= other.x
        return self

    def __imul__(self, other):
        try:
            self._z *= other.z
            self._y *= other.y
            self._x *= other.x
        except Exception as e:
            return str(e)
        return self

    def __mul__(self, other):
        try:
            self._z *= other.z
            self._y *= other.y
            self._x *= other.x
        except Exception as e:
            return str(e)
        return self

    def __ifloordiv__(self, other):
        try:
            self._z *= other.z
            self._y *= other.y
            self._x *= other.x
        except ZeroDivisionError:
            return 'Zero division error. You can do that.'
        return self

    def __truediv__(self, other):
        try:
            self._z *= other.z
            self._y *= other.y
            self._x *= other.x
        except ZeroDivisionError:
            return 'Zero division error. You can do that.'
        return self

    def __str__(self):
        return 'Coordinates of point: X: {}, Y: {}, Z: {}'.format(self._x, self._y, self._z)


dot1 = Dot(2, 4, 8)
dot2 = Dot(2, 4, 8)
print(dot1)
dot1 *= dot2
print(dot1)
dot1 = dot1 + dot2
print(dot1)
dot1 = dot1 - dot2
print(dot1)