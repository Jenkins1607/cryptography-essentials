"""
Поиск примитивных элементов
"""
import time
from miller_rabin_test import execMillerRabin
import gmpy2
from primes import FIRST_PRIMES
import math
import secrets
from UI.UI_primitives import UIprimitives

_RND = gmpy2.random_state(secrets.randbits(128))
BIG_PRIME_PRODUCT = math.prod(FIRST_PRIMES)  

def generateSafePrimeTwist(bits: int) -> tuple[int, int]:
    """
    Возвращает пару простых чисел (p, q), где p = 2q + 1.
    bits: int - размер числа (в битах) для генерации
    """
    start = time.time()
    attempts = 0
    
    _randbits = secrets.randbits
    _execMillerRabin = execMillerRabin
    
    # Заранее подготавливаем маску для старшего и младшего бита
    bit_mask = (1 << (bits - 1)) | 1
    while True:
        attempts += 1

        UIprimitives.progessBar(attempts)

        q = _randbits(bits) | bit_mask
        p = (q << 1) | 1

        check_1 = (q not in FIRST_PRIMES and gmpy2.gcd(q, BIG_PRIME_PRODUCT) > 1)
        check_2 = (p not in FIRST_PRIMES and gmpy2.gcd(p, BIG_PRIME_PRODUCT) > 1)

        if check_1 or check_2:
            continue
        
        # фильтруем
        if not _execMillerRabin(q, k=1, verbose=False): continue
        if not _execMillerRabin(p, k=1, verbose=False): continue

        if execMillerRabin(q, k=15, verbose=False) and execMillerRabin(p, k=15, verbose=False):
            end = time.time()
            UIprimitives.SPT(attempts, start, end, p, q)
            return p, q


def getMinPrimitiveNumber(p: int, q: int) -> int:
    """
    Находит наименьший 
    примитивный элемент 
    по модулю (p) по правилу Эйлера.
    p: int - модуль (p = 2q + 1);
    q: int - простое число.
    """
    start = time.time()
    SUP = 300

    exp1 = 2
    exp2 = q
    for g in range(2, SUP):
        if gmpy2.powmod(g, exp1, p) != 1 and gmpy2.powmod(g, exp2, p) != 1:
            end = time.time()
            UIprimitives.MPN(start, end, p, g)
            
            return g

def getAllPrimitiveNumbers(p: int, g: int, count: int = 100) -> set[int]:
    """
    Возвращает все 
    примитивные элементы 
    по модулю (p).
    bits: int - запрашиваемый размер числа для generateSafePrimeTwist(bits);
    count: int - размер множества примитивных элементов (Для ограничения).
    """
    start = time.time()

    group_order: int = p - 1
    primitives_set: set[int] = set()

    if g == -1:
        return [] # модуль составной

    actual_count = min(count, group_order)
    while len(primitives_set) < actual_count:
        k = gmpy2.mpz_random(_RND, p - 3) + 2          # p in [2, p-2]
        
        if gmpy2.gcd(k, group_order) == 1:
            primitive_element = gmpy2.powmod(g, k, p)
            primitive_element = int(primitive_element)
            primitives_set.add(primitive_element)

    end = time.time()

    UIprimitives.APN(start, end)
    UIprimitives.APN_WRITE_FILE(primitives_set)

    return primitives_set

