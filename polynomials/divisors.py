import math

def getPrimeDivisors(n: int):
    """
    Возвращает все простые
    делители числа n.
    n: int - число (Example: степень многочлена)
    """
    sqrt_n = int(math.sqrt(n))
    divisors: list[int] = []

    for d in range(2, sqrt_n):
        if n % d == 0:
            divisors.append(d)
            while n % d == 0:
                n //= d

    if n > 1:
        divisors.append(n)

    return divisors