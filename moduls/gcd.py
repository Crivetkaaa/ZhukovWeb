def solve_gcd(a, b):
    output = []

    def nod(a, b):
        answer = a // b
        new_a = a % b
        return answer, new_a

    def extended_gcd(a, b):
        if a == 0:
            return b, 0, 1

        gcd, x1, y1 = extended_gcd(b % a, a)

        x = y1 - (b // a) * x1
        y = x1

        output.append(
            f"Обратный шаг: {gcd} = "
            f"{a} * ({x}) + {b} * ({y})"
        )

        return gcd, x, y

    orig_a = a
    orig_b = b

    output.append(
        "=== ПОИСК НОД И ОБРАТНЫЙ АЛГОРИТМ ЕВКЛИДА ==="
    )

    output.append("")
    output.append(
        f"--- Прямой ход: Поиск НОД "
        f"для чисел {orig_a} и {orig_b} ---"
    )

    nod_num = b
    step = 1

    if b == 0:
        nod_num = a
    else:
        while b != 0:
            answer, new_a = nod(a, b)

            output.append(
                f"Шаг {step}: {a} = "
                f"{answer} * {b} + {new_a}"
            )

            a = b

            if new_a != 0:
                nod_num = new_a

            b = new_a
            step += 1

    output.append("-" * 45)
    output.append(
        f"=> НОД({orig_a}, {orig_b}) = {nod_num}"
    )

    output.append("")
    output.append(
        "--- Обратный ход: Линейное представление НОД "
        "(Соотношение Безу) ---"
    )

    if orig_a == 0 or orig_b == 0:
        x = 1 if orig_a != 0 else 0
        y = 1 if orig_b != 0 else 0

        output.append(
            "Один из параметров равен 0. "
            "Очевидное решение:"
        )
    else:
        gcd_val, x, y = extended_gcd(
            orig_a,
            orig_b
        )

    output.append("-" * 45)
    output.append(
        f"=> Коэффициенты Безу: x = {x}, y = {y}"
    )

    output.append(
        f"Проверка: {orig_a} * ({x}) + "
        f"{orig_b} * ({y}) = "
        f"{orig_a * x + orig_b * y}"
    )

    return "\n".join(output)
