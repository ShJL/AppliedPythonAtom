#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''

    calc = {
        "plus":   lambda x, y: x + y,
        "minus":  lambda x, y: x - y,
        "mult":   lambda x, y: x * y,
        "divide": lambda x, y: x / y
    }

    try:
        return calc[operator](float(x), float(y))
    except:
        return None