#!/usr/bin/env python
# coding: utf-8


__CALC = {
    "u+": lambda x: x,
    "u-": lambda x: -x,
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y
}


def is_delim(c):
    return c in " \t"


def is_unary_candidate(op):
    return op in "+-"


def to_unary(op):
    return "u" + op


def is_unary(op):
    return op[0] == "u" and is_unary_candidate(op[1:])


def is_operation(op):
    return op in "*/+-" or is_unary(op)


def priority(op):
    if is_unary(op):
        return 2
    if op in "+-":
        return 0
    if op in "*/":
        return 1
    return -1


def run_operation(op, nums):
    try:
        if not is_unary(op):
            rhs = nums.pop()
            lhs = nums.pop()
            nums.append(__CALC[op](float(lhs), float(rhs)))
        else:
            nums.append(__CALC[op](float(nums.pop())))
    except:
        return False

    return True


def advanced_calculator(input_string):
    '''
    Калькулятор на основе обратной польской записи.
    Разрешенные операции: открытая скобка, закрытая скобка,
     плюс, минус, умножить, делить
    :param input_string: строка, содержащая выражение
    :return: результат выполнение операции, если строка валидная - иначе None
    '''

    nums = []
    stack = []

    num = ""
    can_unary = True
    for c in input_string + " ":
        if c.isdigit() or c == ".":
            num += c
            can_unary = False
            continue

        if num:
            nums.append(float(num))
            num = ""

        if c == "(":
            stack.append(c)
            can_unary = True
        elif c == ")":
            if stack and stack[-1] == "(":
                return None
            while stack and stack[-1] != "(":
                if not run_operation(stack.pop(), nums):
                    return None
            if not stack:
                return None
            stack.pop()
            can_unary = False
        elif is_operation(c):
            if can_unary and is_unary_candidate(c):
                c = to_unary(c)
            while stack and (
                is_unary(stack[-1]) and priority(stack[-1]) > priority(c) or
                not is_unary(stack[-1]) and priority(stack[-1]) >= priority(c)
            ):
                if not run_operation(stack.pop(), nums):
                    return None
            stack.append(c)
            can_unary = True
        elif not is_delim(c):
            return None

    for c in reversed(stack):
        if not is_operation(c) or not run_operation(c, nums):
            return None

    return nums[0] if nums and len(nums) == 1 else None
