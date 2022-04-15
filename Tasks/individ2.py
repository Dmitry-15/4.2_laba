#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создать класс Octal для работы с беззнаковыми целыми восьмеричными числами,
используя для представления числа список из 100 элементов типа int, каждый элемент
которого является восьмеричной цифрой. Младшая цифра имеет меньший индекс (единицы
— в нулевом элементе списка). Реальный размер списка задается как аргумент
конструктора инициализации. Реализовать арифметические операции, аналогичные
встроенным для целых и операции сравнения.
"""


class Octal:

    def __init__(self, number):
        self.storage = []
        self.number = str(number)
        self.limit = 100
        self.checking_length(self.storage)
        for k in self.number:
            self.storage.append(k)

    def __add__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        sum_str = str(num1 + num2)
        sum_lst = []
        for k in sum_str:
            sum_lst.append(k)
        self.checking_length(sum_lst)
        return "".join(sum_lst[::-1])

    def __sub__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        sum_str = str(num1 - num2)
        sum_lst = []
        for k in sum_str:
            sum_lst.append(k)
        self.checking_length(sum_lst)
        return "".join(sum_lst[::-1])

    def __mul__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        sum_str = str(num1 * num2)
        sum_lst = []
        for k in sum_str:
            sum_lst.append(k)
        self.checking_length(sum_lst)
        return "".join(sum_lst[::-1])

    def __truediv__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        sum_str = str(num1 / num2)
        sum_lst = []
        for k in sum_str:
            sum_lst.append(k)
        self.checking_length(sum_lst)
        return "".join(sum_lst[::-1])

    def __lt__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        return num1 < num2

    def __gt__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        return num1 > num2

    def __le__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        return num1 <= num2

    def __ge__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        return num1 >= num2

    def __eq__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        return num1 == num2

    def __ne__(self, other):
        num1 = self.storage[::-1]
        num2 = other.storage[::-1]
        num1 = int("".join(num1), 8)
        num2 = int("".join(num2), 8)
        return num1 != num2

    def checking_length(self, storage):
        length = len(storage)
        if length > self.limit:
            raise ValueError()


if __name__ == '__main__':
    r1 = Octal(25)
    r2 = Octal(15)
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 / r2 = {r1 / r2}")
    print(f"r1 < r2 = {r1 < r2}")
    print(f"r1 > r2 = {r1 > r2}")
    print(f"r1 <= r2 = {r1 <= r2}")
    print(f"r1 >= r2 = {r1 >= r2}")
    print(f"r1 == r2 = {r1 == r2}")
    print(f"r1 != r2 = {r1 != r2}")
