#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Выполнить индивидуальное задание 1 лабораторной работы 4.1, максимально задействовав
имеющиеся в Python средства перегрузки операторов.
"""


class Payment:

    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
        if self.first == 0:
            raise ValueError()

    def __add__(self, other):
        a = self.first / self.second * self.third
        b = other.first / other.second * other.third
        return a + b

    def __lt__(self, other):
        a = self.first / self.second * self.third
        b = other.first / other.second * other.third
        return a < b

    def __gt__(self, other):
        a = self.first / self.second * self.third
        b = other.first / other.second * other.third
        return a > b

if __name__ == "__main__":
    num1 = Payment(28500.5, 29, 30)
    num2 = Payment(27505.13, 26, 31)
    print(f"Начисленная сумма за 2 месяца: {num1 + num2}")
    print(f"Сумма за первый месяц меньше, чем за второй: {num1 < num2}")
    print(f"Сумма за первый месяц больше, чем за второй: {num1 > num2}")
