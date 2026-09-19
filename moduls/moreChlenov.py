def solve_polynomial_gcd(a: str, b: str) -> str:
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

    def poly_xor(a: str, b: str) -> str:
        res = bin(int(a, 2) ^ int(b, 2))[2:]
        return res if res else "0"

    def poly_mul(a: str, b: str) -> str:
        p1 = int(a, 2)
        p2 = int(b, 2)
        res = 0

        while p2 > 0:
            if p2 & 1:
                res ^= p1

            p1 <<= 1
            p2 >>= 1

        return bin(res)[2:]

    def extended_gcd_gf2(
        a: str,
        b: str
    ) -> tuple[str, str, str]:

        a = a.lstrip("0") or "0"
        b = b.lstrip("0") or "0"

        if b == "0":
            return a, "1", "0"

        q, r = moreChlenov(a, b)

        gcd, x1, y1 = extended_gcd_gf2(b, r)

        x = y1
        y = poly_xor(
            x1,
            poly_mul(q, y1)
        )

        output.append(
            f"Обратный шаг: {gcd} = "
            f"{a} * ({x}) ⊕ {b} * ({y})"
        )

        return gcd, x, y

    output.append(
        "=== ПОИСК НОД ПОЛИНОМОВ И ОБРАТНЫЙ АЛГОРИТМ В GF(2) ==="
    )

    orig_a = a
    orig_b = b

    output.append("")
    output.append(
        "--- Прямой ход: Алгоритм Евклида ---"
    )

    step = 1
    temp_a = a
    temp_b = b

    while "1" in temp_b:
        answer, new_a = moreChlenov(
            temp_a,
            temp_b
        )

        output.append(
            f"Шаг {step}: {temp_a} = "
            f"{answer} * {temp_b} + {new_a}"
        )

        temp_a = temp_b
        temp_b = new_a
        step += 1

    output.append("--------------------------------")
    output.append(
        f"=> Итоговый НОД: {temp_a}"
    )

    output.append("")
    output.append(
        "--- Обратный ход: "
        "Линейное представление НОД в GF(2) ---"
    )

    if "1" not in orig_a or "1" not in orig_b:
        x = "1" if "1" in orig_a else "0"
        y = "1" if "1" in orig_b else "0"

        gcd_val = (
            orig_a
            if "1" in orig_a
            else orig_b
        )
    else:
        gcd_val, x, y = extended_gcd_gf2(
            orig_a,
            orig_b
        )

    output.append("--------------------------------")
    output.append(
        f"=> Коэффициенты Безу (полиномы): "
        f"X = {x}, Y = {y}"
    )

    check = poly_xor(
        poly_mul(orig_a, x),
        poly_mul(orig_b, y)
    )

    output.append(
        f"Проверка: ({orig_a} * {x}) ⊕ "
        f"({orig_b} * {y}) = {check}"
    )

    return "\n".join(output)
