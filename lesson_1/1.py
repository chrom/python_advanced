# 1)Создать список из N элементов (от 0 до n с шагом 1). В этом списке
# вывести все четные значения.

print([x for x in range(1, 10) if x % 2 == 0])

# 2) Создать словарь Страна:Столиц  а. Создать список стран. Не все
# страны со списка должны сходиться с названиями стран со словаря. С
# помощою оператора in проверить на вхождение элемента страны в
# словарь, и если такой ключ действительно существует вывести
# столицу.

dictionary_country_capital = {'Andorra': 'Andorra la Vella',
                              'Afghanistan': 'Kabul',
                              'Antigua and Barbuda': "St. John's",
                              'Albania': 'Tirana',
                              'Armenia': 'Yerevan'}
list_country = ['Afghanistan', 'Albania', 'Armenia']

for i in list_country:
    if i in dictionary_country_capital:
        print(dictionary_country_capital[i])

# 3)Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить
# слово Fizz, а вместо чисел, кратных пяти — слово Buzz. Если число
# кратно пятнадцати, то программа должна выводить слово FizzBuzz.
for i in range(1, 101):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(str(i))


# 4) Реализовать функцию bank, кот  орая приннимает следующие
# аргументы: сумма депозита, кол-во лет, и процент. Результатом
# выполнения должна быть сумма по истечению депозита
def bank(money: int, years: int, percent: int) -> int:
    return money * years * percent


print(bank(1000, 3, 20))
