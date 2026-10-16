import secrets
import gmpy2
from gmpy2 import mpz
from UI.UI_miller_rabin import UImiller_rabin

_RND = gmpy2.random_state(secrets.randbits(128))

def execMillerRabin(n: int, k: int = 15, verbose: bool = True) -> bool:
    """
    True  - число ВЕРОЯТНО простое
    False - число ТОЧНО составное
    n: int - проверяемое число
    k: int - количество свидетелей
    verbose: bool - печать результата
    """
    n = mpz(n)

    if n < 2:
        return False
    if n < 4:                # 2, 3
        return True
    if not n & 1:
        return False

    n_1 = n - 1                         
    n_4 = n - 4
    
    s = gmpy2.bit_scan1(n_1)
    t = n_1 >> s
    

    _powmod = gmpy2.powmod
    _mpz_random = gmpy2.mpz_random
    _state = _RND

    for round in range(k):
        if round == 0:
            a = mpz(2)
        else:
            a = _mpz_random(_state, n_4) + 3          # a in [3, n-2]

        x = _powmod(a, t, n)

        # перед циклом проверяется стартовая точка (r=0)
        # 1) a^t ≡ 1 (mod n)
        # 2) a^(t*(2^r)) ≡ n-1 (mod n) ≡ -1 (mod n)
        if x == 1 or x == (n - 1): # x == n-1 для a^(t^(2^0))
            continue
        
        for _ in range(s - 1):
            x = (x * x) % n
            if x == (n_1):
                break                                 # раунд пройден
            if x == 1:                                # нетривиальный корень из 1 ()
                if verbose:
                    UImiller_rabin.is_composite(a, n)
                return False
        else:
            if verbose:
                UImiller_rabin.is_composite(a, n)
            return False

    if verbose:
        UImiller_rabin.is_prime(n, k)
    return True