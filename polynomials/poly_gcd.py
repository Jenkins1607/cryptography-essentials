"""
Модуль проверки неприводимости по критерию Баттлера
"""
import numpy as np

# КРИТЕРИЙ БАТТЛЕРА О НЕПРИВОДИМОСТИ
# 1) Проверка на кратные корни
def polyGCD(f: list[int], f_derivative: list[int], p: int) -> list[int]:
    """
    Возвращает НОД многочленов (проверка неприводимости).
    Критерий: if GCD(f, f', mod=p) > 1 => многочлен неприводим.

    f: list[int] - кандидат на неприводимый многочлен;
    f_derivative: list[int] - производная от f
    p: int - модуль.
    """

    while f_derivative:
        f, f_derivative = f_derivative, polyMod(a=f, b=f_derivative, p=p)

    coeffs: list[int] = polyMonic(f, p)

    return coeffs

def polyMonic(a: list[int], p: int) -> list[int]:
    """Делит многочлен на старший коэффициент -> старший коэффициент = 1.
    Обратный элемент: c^(-1) = c^(p-2) (mod p) (малая теорема Ферма, быстрая степень)."""
    if not a:
        return a
    inv = pow(a[-1], p - 2, p)
    return [c * inv % p for c in a]

def polyTrim(f: list[int]) -> list[int]:
    """
    Убирает нули из конца массива (многочлена f).
    f: list[int] - многочлен степени n
    """
    n = len(f)
    while n and f[n - 1] == 0:
        n -= 1
    return f[:n]

def polyMod(a: list[int], b: list[int], p: int) -> list[int]:
    """
    Возвращает остаток от деления многочленов (a делить на b).
    Ограничения: a_length > b_length else return a.

    a: list[int] - многочлен;
    b: list[int] - многочлен.
    """

    a_length = len(a)
    b_length = len(b)

    if a_length < b_length:
        return a

    r = a[:] # безопасно копируем а
    inv_elem = pow(b[-1], p - 2, p)

    while len(r) >= len(b):
        coef = (r[-1] * inv_elem) % p # на что домножить f, чтобы убить старший член r
        shift = len(r) - len(b) # сдвиг (умножение на x^shift)

        for i, f_i in enumerate(b):
            r[shift + i] = (r[shift + i] - coef * f_i) % p

        r = polyTrim(r)

    return r


def polyMul(f1: list[int], f2: list[int], p: int) -> list[int]:
    """
    Возвращает произведение многочленов.
    f1: list[int] - многочлен;
    f2: list[int] - многочлен.
    p: int - модуль.
    """

    LEN_F1 = len(f1)
    LEN_F2 = len(f2)
    RESULT_LENGTH = (LEN_F1 + LEN_F2) - 1

    product = [0] * RESULT_LENGTH

    for i in range(LEN_F1):
        for j in range(LEN_F2):
            product[i + j] += (f1[i] * f2[j]) % p

    product = polyTrim(product)

    return product 

# f1 = []
# f2 = [] # модуль (многочлен)
# p = ... # характеристика поля 

# res: list[int] = polyMod(a=f1,,b=f2,p=7)