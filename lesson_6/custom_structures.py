# 1) Создать свою структуру данных Список, которая поддерживает
# индексацию. Методы pop, append, insert, remove, clear.
# Перегрузить операцию сложения для списков, которая возвращает новый расширенный объект.

class CustomList(list):
    def __init__(self, custom_list: list):
        self.data = custom_list

    def __len__(self):
        return len(self.data)

    def append(self, item: int):
        self.data[len(self.data)] = item

    def pop(self) -> int:
        return self.data[len(self.data)]

    def remove(self, value: int):
        for index, item in enumerate(self.data):
            if item == value:
                del self.data[index]
                break

    def clear(self, ):
        self.data = []

    def insert(self, key: int, value: int):
        flag = False
        for index, item in enumerate(self.data):
            if index == key:
                self.data[index] = value
                flag = True
                break
            if flag:
                self.data[index + 1] = item
            else:
                self.data[index] = item

    def __add__(self, other):
        return CustomList(self.data + other.data)


listA = [1, 2, 34, 12]

# print(listA[1])
# print(listA.append(26))
print(listA)
listA.insert(0, 100)
# print(listA[1: 2])
# print(listA.remove(2))
print(listA)
print('*' * 30)

listB = CustomList([1, 2, 34, 5, 65, 98, 25])
listC = CustomList([3, 4, 68, 10, 120, 180, 50])
print(listB.__dict__)
listB.insert(1, 300)
print(listB.__dict__)
new = listB + listC
print(new.__dict__)
print('*' * 50)


# 2) Создать свою структуру данных Словарь, которая поддерживает методы,
# get, items, keys, values. Так же перегрузить операцию сложения для
# словарей, которая возвращает новый расширенный объект.

class CustomDict:

    def __init__(self, custom_dict: dict = {}):
        print(custom_dict)
        self._data = custom_dict

    def get(self, key: str):
        try:
            return self._data[key]
        except NameError:
            return ''

    def keys(self):
        result = []
        for index, item in enumerate(self._data):
            result.append(index)
        return result

    def values(self):
        result = []
        for index, item in enumerate(self._data):
            result.append(item)
        return result

    def items(self):
        result = []
        for index, item in enumerate(self._data):
            result.append((index, item))
        return result

    def __add__(self, other):
        return CustomDict(dict(**self._data, **other._data))



a = CustomDict()
a.foo = "bar"
a.asd = "eqw"
a.qqqqq = 'fowwwwo'
# print(a.keys())
# print(a.values())
# print(a.items())
print(a.__dict__)

o = CustomDict()
o.foos = "aaa"
o.asds = "zzzz"
print(o.__dict__)
x = o + a
print(x.__dict__)

# o.update({'a': 'b'}, c=44)
# print 'lumberjack' in o
# print o

# In [187]: run mapping.py
# True
# {'a': 'b', 'lumberjack': 'foo', 'foo': 'bar', 'c': 44}

# cd = {'1': 'asd', '3': 'adasd', '5': 'qerq', 9: 'qewrty'}
# print(cd)
# print(cd.keys())
# print(cd.values())
# print(cd.items())
