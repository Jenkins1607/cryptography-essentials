"""
Модуль поиска неприводимого многочлена
над полем Галуа GF(p), где p - модуль

2 критерий: если ранг равен степень многочлена - 1) 
"""
import numpy as np
import secrets
from poly_fast_pow import polyFastPow
from gcd import (
    polyTrim,
    polyGCD
    )

def polyIrreducibleSearch(p: int, n: int) -> list[int]:
    """
    Возвращает неприводимый многочлен
    в формате списка коэффициентов.

    Включает две проверки по критерию Баттлера:
    1) GCD(f, f') == 1
    2) Критерий Фронебиуса(?)

    p: int - модуль;
    n: int - степень многочлена
    """
    while True:
        # создаем список длины n
        f: list[int] = [secrets.randbelow(p) for _ in range(n)]
        # нормировка (гарантируем длину n + 1)
        f.append(1)  # Нормировка: старший коэффициент = 1
            
        # Убираем ведущие нули 
        f = polyTrim(f)
        if len(f) != n + 1:
            continue  # Степень не совпадает, генерируем заново

        f_derivative = polyDerivative(f, p)
        gcd = polyGCD(f, f_derivative, p)

        # ПЕРВЫЙ КРИТЕРИЙ
        if len(gcd) > 1:  # НОД != 1, есть кратные корни
            continue

        return f
        # ВТОРОЙ КРИТЕРИЙ
        # 2. Полная проверка неприводимости (тест Рабина)
        # if isIrreducible(f, p, n):
        #     print(f"Найден неприводимый многочлен: {f}")
        #     return f

def polyDerivative(f: list[int], p: int) -> list[int]:
    """
    Возвращает список коэффициентов
    производной.

    Формула: f[i] = c(x_i)^n =>
    f'[i] = n*c*(x_i)^(n-1) mod p

    f: list[int] - многочлен степени n.
    p: int - модуль.
    """
    if len(f) <= 1:
        return [0]
    # список коэффициентов производной
    f_derivative: list[int] = []
    N: int = len(f) # степень многочлена

    for i in range(1, N):
        exp = i
        f_derivative.append(exp*f[i] % p)

    f_derivative = polyTrim(f_derivative)

    return f_derivative



def getRankMatrix(f: list[int], f_mod: list[int], p: int):
    """
    f: list[int] - кандидат на неприводимый многочлен;
    f_mod: list[int] - многочлен (модуль);
    p: int - характеристика поля.
    """
    n: int = len(f) # степень многочлена
    matrix = np.zeros(shape=(n, n), dtype=int)

    for i in range(1, n):
        elem = polyFastPow(base=f, exp=i, f=f_mod, p=p)
        matrix[i - 1] = elem

    return matrix




n = 5
p = 5

f = polyIrreducibleSearch(n=n, p=p)
print(f)
f_mod = [1, 0, 1]
res = getRankMatrix(f=f, f_mod=f_mod, p=p)

print(res)