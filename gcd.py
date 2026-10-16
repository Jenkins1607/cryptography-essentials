def getGCD(a: int, b: int) -> int:
    """
    Возвращает целое число - НОД(a, b)
    """
    while b != 0:
        a, b = b, a % b
    return a