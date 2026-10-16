class UIprimitives:
    """
    UI layer for primitive_elements
    """
    def progessBar(attempts: int):
        if attempts % 5000 == 0:
            # Длина полоски — 20 символов. Кадры меняются по кругу (оператор %)
            bar_position = (attempts // 5000) % 20
            
            # Строим полоску: заполняем символом '█', а остальное пробелами ' '
            bar = "█" * bar_position + " " * (20 - bar_position)
            
            # \r сбрасывает курсор в начало строки, end="" убирает перенос строки
            print(f"\rПоиск [ {bar} ] Попыток: {attempts}", end="", flush=True)

    def SPT(attempts: int, start, end, p, q):
        print("\nФильтрация завершена")
        print("\n===============================================================================================")
        print(f"Время работы generateSafePrimeTwist: {end - start:.6f} (сек.)")
        print(f"Общее количество попыток: {attempts}")
        print(f"SPT:\nq:\n{q};\np=2q + 1:\n{p})")
        print("===============================================================================================\n") 

    def MPN(start, end, p, g):
        print(f"\nМинимальный примитивный элемент (mod {p}): {g}")
        print("=====================================================")
        print(f"Время работы getMinPrimitiveNumber: {end - start:.6f} (сек.)")
        print("=====================================================")

    def APN(start, end):
        print("\n=====================================================")
        print(f"Время работы getAllPrimitiveNumbers: {end - start:.6f} (сек.)")
        print("=====================================================\n")

        print(f"Множество примитивных элементов: ВЫВОД СОХРАНЕН В ФАЙЛ PRIMITIVES_SET.txt")

    def APN_WRITE_FILE(primitives_set):
        with open("PRIMITIVES_SET.txt", "w", encoding="utf-8") as f:
            f.write("=== МНОЖЕСТВО ПРИМИТИВНЫХ ЭЛЕМЕНТОВ ===\n\n")

            # Перебираем элементы по одному и записываем каждый с новой строки
            for index, element in enumerate(primitives_set, start=1):
                f.write(f"Элемент №{index}:\n{element}\n\n")