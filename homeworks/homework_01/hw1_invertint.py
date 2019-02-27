#!/usr/bin/env python
# coding: utf-8


def reverse(number):
    '''
    Метод, принимающий на вход int и
    возвращающий инвертированный int
    :param number: исходное число
    :return: инвертированное число
    '''

    res = str(number)[::-1].lstrip("0")
    return int(res if number > 0 else "-" + res[:-1]) if res else 0
