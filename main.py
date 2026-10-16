import time
import numpy as np
from find_inverse import getInverseElement
from fast_pow import fastPow
from miller_rabin_test import execMillerRabin
from find_prime_numbers import findPrimeNumbers
from gauss import execGaussMethod  
import gmpy2
from primitive_elements import (
    getAllPrimitiveNumbers,
    getMinPrimitiveNumber,
    generateSafePrimeTwist
    )


# ==========================================
# БЛОК 1: Тест обратного элемента
# ==========================================
def test_inverse_element():
    print("=" * 50)
    print("1) Нахождение обратного элемента")
    print("=" * 50)
    
    # 400 и 10^9 не взаимно просты (НОД=400), поэтому берем 17 и 31
    n, mod = 17, 31 
    
    inv = getInverseElement(element=n, mod=mod)
    print(f"{n}^-1 (mod {mod}) = {inv}")
    print(f"Проверка (встроенный pow): {pow(n, -1, mod)}\n")

# ==========================================
# БЛОК 2: Тест быстрого возведения в степень
# ==========================================
def test_fast_pow():
    print("=" * 50)
    print("2) Быстрое возведение в степень")
    print("=" * 50)
    
    base, exp, mod = 2, 41, 10**9 + 7
    
    result = fastPow(base=base, exp=exp, mod=mod)
    print(f"{base}^{exp} (mod {mod}) = {result}")
    print(f"Проверка (встроенный pow): {pow(base, exp, mod)}\n")

# ==========================================
# БЛОК 3: Тест Миллера-Рабина
# ==========================================
def test_miller_rabin():
    print("=" * 50)
    print("3) Тест Миллера-Рабина")
    print("=" * 50)
    
    prime_num = 2027
    print(f"Проверяем число {prime_num} на простоту (15 свидетелей):")
    is_prime = execMillerRabin(n=prime_num, k=15)
    print(f"Результат: {is_prime}\n")

# ==========================================
# БЛОК 4: Генерация простого числа
# ==========================================
def test_find_prime():
    print("=" * 50)
    print("4) Генерация большого простого числа")
    print("=" * 50)
    
    # 1024 бита может считать пару секунд, для быстрого теста ставим 256
    bits = 256 
    print(f"Ищем простое число длиной {bits} бит...")
    p = findPrimeNumbers(bits=bits)
    print(f"Найдено:\n{p}\n")

# ==========================================
# БЛОК 5: Метод Гаусса
# ==========================================
def test_gauss_method():
    print("=" * 50)
    print("5) Метод Гаусса по модулю p")
    print("=" * 50)
    
    A = [
        [3, 2, 1], 
        [1, 3, 5], 
        [5, 4, 3]
    ]
    b = [0, 5, 3]
    mod = 11
    
    print("Исходная матрица A:")
    print(np.array(A))
    print(f"Вектор b: {b}")
    print(f"Модуль: {mod}\n")
    
    triangle_matrix = execGaussMethod(A, b, mod)
    
    print("Результат (треугольная расширенная матрица [A | b]):")
    print(triangle_matrix)

# ==========================================
# БЛОК 6: Поиск примитивных элементов
# ==========================================
def test_get_all_primitive_numbers(bits: int):
    """
    Тестирует функцию поиска всех примитивных элементов по модулю.
    """
    start = time.time()
    p, q = generateSafePrimeTwist(bits=bits)
    g: int = getMinPrimitiveNumber(p, q) # находим минимальный примитивный элемент
    getAllPrimitiveNumbers(p=p, g=g,  count=1)
    end = time.time()
    time_of_work = end - start
    print("=====================================================")
    print(f"Общее время работы алгоритма getAllPrimitiveNumbers(bits={bits}): {time_of_work}")
    print("=====================================================")
    
def main():
    # test_inverse_element()
    # test_fast_pow()
    # test_miller_rabin()
    # test_find_prime()
    # test_gauss_method()
    # test_get_all_primitive_numbers()
    # p, q = generateSafePrimeTwist(bits=1024)
    # p = findPrimeNumbers(bits=bits)
    # g = getMinPrimitiveNumber(p, q, mod=p) # мин. примитивный эл-т
    # findPrimeNumbers(bits=4096)
    test_get_all_primitive_numbers(2048)
    # res = fastPow(base=15482988487147978591613821919937041202878168914467550160769641895236090411351477300888379083830623883627598990195489321261267224177016636698113248484898557076438074236079088972503558263669710265917660495831058410422727537833365068010898832273189704416632308921957385524879800410114435070630882998351130831146, exp=9937041202878168914467550160769641895236090411351477300888379083830623883627598990195489321261267224177016636698113248484898557076438074236079088972503558263669710265917660495831058410422727537833365068010898832273189704416632308921957385524879800410114435070630882998351130831146, mod=12345367685432123456756432)
    # print(res)
    # candidate = 15482988487147978591613821919937041202878168914467550160769641895236090411351477300888379083830623883627598990195489321261267224177016636698113248484898557076438074236079088972503558263669710265917660495831058410422727537833365068010898832273189704416632308921957385524879800410114435070630882998351130831146
    # res = execMillerRabin(candidate)
    # test_prime = gmpy2.is_prime(candidate)
    # print(res, test_prime, sep="\n")
    # test_gauss_method()
if __name__ == "__main__":
    main()