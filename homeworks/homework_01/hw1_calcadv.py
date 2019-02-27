#!/usr/bin/env python
# coding: utf-8


def is_operation(c):
    return c in "*/+-"


def priority(c):
    if c in "+-":
        return 0
    if c in "*/":
        return 1
    return -1


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    calc = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y
    }

    rpn = []
    stack = []

    num = ""
    for c in input_string:
        if c.isdigit():
            num += c
        else:
            if num:
                rpn.append(int(num))
                num = ""

            if c == "(":
                stack.append(c)
            elif c == ")":
                while not stack and stack[-1] != "(":
                    rpn.append(stack.pop())
                if not stack:
                    return None
                stack.pop()
            elif is_operation(c):
                while not stack and priority(stack[-1]) >= priority(c):
                    rpn.append(stack.pop())
                stack.append(c)
            elif c != " ":
                return None

    for c in reversed(stack):
        if not is_operation(c):
            return None
        rpn.append(c)

    try:
        while len(rpn) > 1:
            op = rpn.pop()
            rhs = rpn.pop()
            lhs = rpn.pop()
            rpn.append(calc[op](lhs, rhs))
    except:
        return None

    return rpn[0]