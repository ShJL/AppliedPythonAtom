#!/usr/bin/env python
# coding: utf-8


def bracket_type(c):
    if c in "()":
        return 0
    if c in "[]":
        return 1
    return 2


def is_bracket_correct(input_string):
    '''
    Метод проверяющий является ли поданная скобочная
     последовательность правильной (скобки открываются и закрываются)
     не пересекаются
    :param input_string: строка, содержащая 6 типов скобок (,),[,],{,}
    :return: True or False
    '''

    stack = []
    for c in input_string:
        if c in "([{":
            stack.append(c)
        else:
            if not stack or bracket_type(c) != bracket_type(stack[-1]):
                return False
            stack.pop()

    return len(stack) == 0