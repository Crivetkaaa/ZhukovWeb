def solve_primitiv_chlen(a: str) -> str:
    output = []

    def moreChlenov(a: str, b: str) -> tuple[str, str]:
        a = a.lstrip("0") or "0"
        b = b.lstrip("0") or "0"

        if int(a, 2) < int(b, 2):
            return "0", a

        zero = len(a) - len(b)
        b_shifted = b + "0" * zero
        answer = ""

        for _ in range(zero + 1):
            if a[0] == "0":
                answer += "0"
            else:
                answer += "1"
                result = bin(
                    int(a, 2) ^ int(b_shifted, 2)
                )[2:]
                a = result.zfill(len(a))

            a = a[1:]
            b_shifted = b_shifted[:-1]

        a = a.lstrip("0") or "0"
        answer = answer.lstrip("0") or "0"

        return answer, a

    def find_dels(n: int) -> list[int]:
        dels = []

        for i in range(2, n):
            if n % i == 0:
                dels.append(i)

        return dels

    def poly_to_str(binary_str: str) -> str:
        binary_str = binary_str.lstrip("0") or "0"

        if binary_str == "0":
            return "0"

        terms = []
        length = len(binary_str)

        for i, bit in enumerate(binary_str):
            if bit == "1":
                power = length - i - 1

                if power == 0:
                    terms.append("1")
                elif power == 1:
                    terms.append("x")
                else:
                    terms.append(f"x^{power}")

        return " + ".join(terms)

    output.append(
        "=== ПРОВЕРКА МНОГОЧЛЕНА НА ПРИМИТИВНОСТЬ ==="
    )

    a = a.strip()

    if not a or any(bit not in "01" for bit in a):
        return "Ошибка: введите двоичную строку многочлена."

    a = a.lstrip("0") or "0"
    n = len(a) - 1

    if n < 1:
        return "Ошибка: степень многочлена должна быть >= 1."

    max_per = 2 ** n - 1

    output.append(f"Входной многочлен: {a}")
    output.append(f"Вид многочлена: {poly_to_str(a)}")
    output.append(f"Степень многочлена: {n}")
    output.append(f"Максимальный период: {max_per}")
    output.append("")

    output.append("--- Поиск делителей максимального периода ---")

    dels = find_dels(max_per)

    if not dels:
        output.append(
            f"У числа {max_per} нет собственных делителей больше 1."
        )

    output.append(f"Найденные делители: {dels}")
    output.append("")

    for d in dels:
        output.append("=" * 60)
        output.append(f"Проверяем делитель периода d = {d}")

        if d < n:
            output.append(
                f"Степень проверяемого многочлена ({d}) "
                f"меньше степени исходного ({n})."
            )
            output.append("Деление пропускается.")
            output.append("")
            continue

        test_poly = "1" + "0" * (d - 1) + "1"

        output.append(f"Делимое: {test_poly}")
        output.append(
            f"В математическом виде: x^{d} + 1"
        )
        output.append(f"Делитель: {a}")
        output.append(
            f"В математическом виде: {poly_to_str(a)}"
        )
        output.append("")
        output.append("--- Выполнение деления ---")

        answer, ost = moreChlenov(test_poly, a)

        output.append(f"Двоичное частное: {answer}")
        output.append(
            f"Частное в виде многочлена: {poly_to_str(answer)}"
        )
        output.append(f"Двоичный остаток: {ost}")
        output.append(
            f"Остаток в виде многочлена: {poly_to_str(ost)}"
        )

        if ost == "0":
            output.append("")
            output.append(
                f"Остаток равен 0: исходный многочлен делит "
                f"x^{d} + 1 без остатка."
            )
            output.append(
                f"Обнаружен период, не превышающий {d}."
            )
            output.append("Вердикт: НЕПРИМИТИВНЫЙ")
            return "\n".join(output)

        output.append(
            "Остаток не равен 0: деление не нацело."
        )
        output.append("")

    output.append("=" * 60)
    output.append(
        "Ни один из проверенных делителей периода "
        "не дал нулевого остатка."
    )
    output.append(
        "Вердикт: ПРИМИТИВНЫЙ"
    )
    output.append(
        f"Период равен {max_per}."
    )

    return "\n".join(output)


print(solve_primitiv_chlen("11111"))
