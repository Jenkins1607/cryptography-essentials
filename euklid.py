
def execEuklid(a: int, b: int) -> tuple[list[int], list[int]]:
    """
    Возвращает два списка:
    q_list - список неполных частных;
    remainders - список остатков.
    """
    q_list = []
    remainders = []
    cur_a = max(a, b) # 2027
    cur_b = min(a, b) # 5

    i = 0
    while  cur_b != 0:
        q = cur_a // cur_b # неполное частное 
        # q's = [405, 2, 2]
        remaind = cur_a % cur_b # остаток
        # remainders = [2, 1, 0]

        q_list.append(q)
        remainders.append(remaind)

        cur_a = cur_b
        cur_b = remainders[i]

        i += 1

    return (q_list, remainders)