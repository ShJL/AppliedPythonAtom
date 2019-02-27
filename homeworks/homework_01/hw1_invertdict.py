#!/usr/bin/env python
# coding: utf-8


def uncover(obj):
    if not (isinstance(obj, list) or isinstance(obj, set) or isinstance(obj, tuple)):
        return [obj]
    res = []
    for v in obj:
        res += uncover(v)
    return res


def invert_dict(source_dict):
    '''
    Функция которая разворачивает словарь, т.е.
    каждому значению ставит в соответствие ключ.
    :param source_dict: dict
    :return: new_dict: dict
    '''

    if not isinstance(source_dict, dict):
        return source_dict

    new_dict = {}
    for k, vs in source_dict.items():
        for v in uncover(vs):
            if v not in new_dict:
                new_dict[v] = k
            elif isinstance(new_dict[v], list):
                new_dict[v].append(k)
            else:
                new_dict[v] = [new_dict[v], k]

    return new_dict
