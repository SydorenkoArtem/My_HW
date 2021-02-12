# Написать функцию которая будет простое число возводить в квардрат
from itertools import count, islice
from math import sqrt


def is_prime(number: int) -> bool:
    return number > 1 and all(number % i for i in islice(count(2), int(sqrt(number) - 1)))


def exponentiation(number):
    for i in range(2, number):
        if number % i:
            continue
        else:
            return number
    return number ** 2


number = int(input('Введите число:\n'))

print(exponentiation(number) if is_prime(number) else 'number is not prime')


# Необходимо возвести в квадрат все простые числа в списке используя функцию map
numbers = input('Введите перечень чисел через пробел:')
list_1 = numbers.split()
list_2 = list(map(int, list_1))
new_list = list(map(exponentiation, list_2))

print(new_list)
