from primes import FIRST_PRIMES
import random 
import time 
import math
from gcd import getGCD
import gmpy2
from miller_rabin_test import execMillerRabin
# bits = 4096
# # range_diapasone = range(2**(bits - 1), 2**bits - 1)

# p = random.randint(2**(bits - 1), 2**bits - 1)
# start_big_prime_gen = time.time()
# gmpy2.is_prime(p, 15)
# end_big_prime_gen = time.time()
# time_of_work = end_big_prime_gen - start_big_prime_gen
# print(f"Время работы gmpy2.is_prime(): bits={bits}: {time_of_work:.6f}")
# start_big_prime_gen = time.time()
# execMillerRabin(p)
# end_big_prime_gen = time.time()
# time_of_work = end_big_prime_gen - start_big_prime_gen
# print(f"Время работы execMillerRabin: bits={bits}: {time_of_work:.6f}")
# BIG_PRIME_PRODUCT = math.prod(FIRST_PRIMES)
# math.gcd(p, BIG_PRIME_PRODUCT)
# start_custom_gcd = time.time()
# getGCD(p, BIG_PRIME_PRODUCT)
# end_custom_gcd = time.time()

# time_of_work_custom_gcd = end_custom_gcd - start_custom_gcd
# print(f"Время работы getGCD(custom GCD function): {time_of_work_custom_gcd:.6f}(sec.)")

# start_custom_gcd = time.time()
# math.gcd(p, BIG_PRIME_PRODUCT)
# end_custom_gcd = time.time()

# time_of_work_custom_gcd = end_custom_gcd - start_custom_gcd
# print(f"Время работы math.GCD(burned-in function): {time_of_work_custom_gcd:.6f}(sec.)")
# state = gmpy2.random_state()
# n = 10
# for _ in range(20):
#     a = random.randint(2, n - 2)
#     print(a)
#     print()