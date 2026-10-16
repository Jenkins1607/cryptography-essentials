class UImiller_rabin:
    """
    UI layer for miller_rabin test
    """
    def is_composite(a, n):
        print(f"Число {n} составное, свидетель: {a}\n")

    def is_prime(n, k):
        print(f"\nЧисло {n} ВЕРОЯТНО простое (k={k})")