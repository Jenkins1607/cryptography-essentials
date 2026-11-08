import time
from poly_gcd import (
    polyMod,
    polyMul
    )

def polyFastPow(base: list[int], exp: int, f_mod: list[int], p: int) -> list[int]:
    """
    Быстрое возведение 
    многочлена base в степень 
    exp по модулю многочлена f.
    
    base: list[int] - многочлен;
    exp: int - степень для base;
    f_mod: list[int] - многочлен (модуль);
    p: int - характеристика поля.
    """

    result = [1]
    current_exp = exp
    current_base = polyMod(a=base,b=f_mod,p=p)
    
    if current_exp & 1:
        result = current_base
    
    current_exp >>= 1

    while current_exp > 0:
        current_base_mult = polyMul(f1=current_base, f2=current_base, p=p)
        current_base = polyMod(a=current_base_mult, b=f_mod, p=p)

        if current_exp & 1:
            next_mult = polyMul(f1=result, f2=current_base, p=p)
            result = polyMod(a=next_mult, b=f_mod, p=p)

        current_exp >>= 1

    return result


start = time.time()
res = polyFastPow(base=[1, 0, 1], exp=10_000_000, f_mod=[1, 0, 1, 0, 0, 1], p=101)
end = time.time()

time_of_work = end - start

print(f"Результат: {res}", f"Время работы polyFastPow: {time_of_work}", sep='\n')

# print(res)
