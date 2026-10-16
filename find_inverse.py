"""
Нахождение обратного элемента по модулю mod
"""
from euklid import execEuklid

def getInverseElement(element: int, mod: int):
    """
    Возвращает обратный элемент 
    по модулю mod
    """
    q_list, remainders = execEuklid(element, mod)
    gcd = remainders[-2]
    if gcd != 1:
        return f"Обратный элемент не существует (GСD = {gcd})"
    
    S = len(q_list)
    p_0 = 1
    p_1 = q_list[0]
    p_list = [p_0, p_1]

    for i in range(2, S + 1):
        p_list.append(q_list[i - 1]*p_list[i - 1] + p_list[i - 2])

    # вывод обратного элемента
    exp = (S - 1)
    inv_elem = p_list[-2]
    if exp % 2 != 0:
        inv_elem *= -1

    return inv_elem
