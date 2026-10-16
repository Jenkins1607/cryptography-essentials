import time
import math
import secrets
from miller_rabin_test import execMillerRabin
from primes import FIRST_PRIMES
import gmpy2

BIG_PRIME_PRODUCT = math.prod(FIRST_PRIMES)             

def findPrimeNumbers(bits: int) -> int:

    while True:

        q = secrets.randbits(bits)
        q |= (1 << (bits - 1)) | 1

        if q in FIRST_PRIMES:
            return q

        if gmpy2.gcd(q, BIG_PRIME_PRODUCT) > 1:
            continue  # составное

        if not execMillerRabin(q, k=1):
            continue

        if execMillerRabin(q, k=15):
            return q

