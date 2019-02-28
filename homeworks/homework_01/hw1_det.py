#!/usr/bin/env python
# coding: utf-8


def calculate_determinant(list_of_lists):
    '''
    Метод, считающий детерминант входной матрицы,
    если это возможно, если невозможно, то возвращается
    None
    Гарантируется, что в матрице float
    :param list_of_lists: список списков - исходная матрица
    :return: значение определителя или None
    '''

    n = len(list_of_lists)
    matr = []
    for row in list_of_lists:
        if len(row) != n:
            return None
        matr.append(row.copy())

    for i in range(n):
        for j in range(i + 1, n):
            delta = matr[j][i] / matr[i][i]
            for k in range(i, n):
                matr[j][k] -= delta * matr[i][k]

    det = 1
    for i in range(n):
        det *= matr[i][i]

    return det
