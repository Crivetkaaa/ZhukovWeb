import math


def solve_log(p, y):
    output = []

    phi = p - 1
    n = phi
    elementary = []

    limit = int(math.isqrt(phi))

    output.append("=== ДИСКРЕТНОЕ ЛОГАРИФМИРОВАНИЕ ПО МОДУЛЮ ===")
    output.append("")
    output.append("Шаг 1: Разложение порядка группы (phi) на простые множители")
    output.append(f"n = p - 1 => n = {p} - 1 = {phi}")
    output.append("")

    def findElementary():
        nonlocal n

        for i in range(2, limit + 1):
            while n % i == 0:
                if i not in elementary:
                    elementary.append(i)
                n //= i

        if n > 1:
            elementary.append(n)

    def writeElementary():
        findElementary()

        output.append(
            f"Простые множители числа {phi}: {elementary}"
        )
        output.append("-" * 50)

    def findMinElementary():
        output.append(
            "Шаг 2: Поиск минимального первообразного корня (g_min)"
        )

        g_min = None

        for i in range(2, p):
            is_root = True

            output.append(f"Проверяем число i = {i}:")

            for el in elementary:
                power = phi // el
                res = pow(i, power, p)

                output.append(
                    f"  {i}^{power} mod {p} = {res}"
                )

                if res == 1:
                    is_root = False

                    output.append(
                        f"  -> Число {i} НЕ подходит, так как получили 1."
                    )
                    break

            if is_root:
                g_min = i

                output.append(
                    f"  -> Так как ни разу не получили 1, "
                    f"число g = {i} — это минимальный первообразный корень!"
                )
                break

        output.append("-" * 50)

        return g_min

    writeElementary()
    g_min = findMinElementary()

    output.append("Шаг 3: Метод Больших и Малых шагов")
    output.append(
        f"Решаем уравнение: {g_min}^x ≡ {y} (mod {p})"
    )

    m = math.isqrt(phi) + 1

    output.append(
        f"Вычисляем шаг таблицы m = ⌈√{phi}⌉ = {m}"
    )

    output.append("")
    output.append("--- Часть A: Малые шаги ---")
    output.append(
        f"Формула: R(j) = y * g^j mod p, где j от 0 до {m - 1}"
    )

    baby_steps = {}

    res_baby = y

    for j in range(m):
        baby_steps[res_baby] = j

        output.append(
            f"  j = {j}: значение = {res_baby}"
        )

        res_baby = (res_baby * g_min) % p

    output.append("")
    output.append("--- Часть Б: Большие шаги ---")

    giant_base = pow(g_min, m, p)

    output.append(
        f"База для больших шагов: "
        f"g^m mod p = {g_min}^{m} mod {p} = {giant_base}"
    )

    output.append(
        f"Формула: L(i) = (g^m)^i mod p = "
        f"{giant_base}^i mod p, где i от 1 до {m}"
    )

    x_res = None
    res_giant = giant_base

    for i in range(1, m + 1):
        line = (
            f"  i = {i}: {giant_base}^{i} mod {p} = {res_giant}"
        )

        if res_giant in baby_steps:
            j = baby_steps[res_giant]

            output.append(
                line +
                f" -> НАЙДЕНО СОВПАДЕНИЕ "
                f"со значением из малых шагов (j = {j})!"
            )

            x_res = i * m - j

            output.append("")
            output.append("Финальный расчет:")
            output.append(
                f"x = i * m - j = {i} * {m} - {j} = {x_res}"
            )

            break

        output.append(line + " (совпадений нет)")

        res_giant = (res_giant * giant_base) % p

    output.append("-" * 50)

    if x_res is not None:
        check = pow(g_min, x_res, p)

        output.append(
            f"Проверка: {g_min}^{x_res} mod {p} = "
            f"{check} (Должно быть {y})"
        )
    else:
        output.append("Решение не найдено.")

    return "\n".join(output)
