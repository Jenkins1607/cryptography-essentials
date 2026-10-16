"""
Метод Гаусса по модулю mod
(Приведение матрицы 
к ступенчатому виду)
"""
import numpy as np

def execGaussMethod(A: list[list[int]], b: list[int], mod: int) -> np.ndarray:
    """
    Возвращает расширенную матрицу, 
    приведенную к треугольному виду 
    по модулю mod.
    """
    A_mat = np.array(A, dtype=int) % mod
    b_mat = np.array(b, dtype=int).reshape(-1, 1) % mod
    
    # Создаем расширенную матрицу 
    M: np.ndarray = np.hstack((A_mat, b_mat))
    ROWS, COLS = M.shape
    
    # Прямой ход 
    pivot_row = 0  # Текущая строка для ведущего элемента
    
    # Идем по столбцам (кроме последнего - это вектор b)
    for col in range(COLS - 1):
        # Если все строки уже обработаны, выходим
        if pivot_row >= ROWS:
            break
            
        # Ищем ненулевой элемент в текущем столбце
        non_zero_indexes = np.nonzero(M[pivot_row:, col])[0]

        # Если нашли, меняем строки местами
        if len(non_zero_indexes) > 0:
            actual_pivot_row = pivot_row + non_zero_indexes[0]
            if actual_pivot_row != pivot_row:
                M[[pivot_row, actual_pivot_row]] = M[[actual_pivot_row, pivot_row]]

        # Если весь столбец ниже pivot_row нулевой - идем к следующему столбцу
        if M[pivot_row, col] == 0:
            continue

        # НОРМАЛИЗАЦИЯ: делаем ведущий элемент равным 1
        inv = pow(int(M[pivot_row, col]), -1, mod)
        M[pivot_row] = (M[pivot_row] * inv) % mod

        # обнуляем элементы ниже диагонали
        for row in range(pivot_row + 1, ROWS):
            if M[row, col] == 0:
                continue

            factor = M[row, col]  # Теперь factor = M[row, col] * 1, т.к. ведущий уже = 1
            M[row] = (M[row] - factor * M[pivot_row]) % mod
        
        pivot_row += 1
    
    # ПРОВЕРКА НА НЕСОВМЕСТНОСТЬ
    for row in range(ROWS):
        # Если вся строка (кроме последнего элемента) нулевая, а последний элемент не нулевой
        if np.all(M[row, :-1] == 0) and M[row, -1] != 0:
            raise ValueError(f"Система несовместна: строка {row} имеет вид [0 0 ... 0 | {M[row, -1]}]")
            
    return M