def create_mas(str_mas: str) -> list:
    str_mas.replace(" ", "")
    str_mas = str_mas.replace("(", "").replace(")", "")
    mas = str_mas.split(",")
    return [int(i) for i in mas]

def solve_reverse(mas: str) -> str:
    mas = create_mas(mas)
    output = []

    output.append(
        "=== ПОИСК ОБРАТНОЙ ПЕРЕСТАНОВКИ ==="
    )

    output.append("")
    output.append(
        f"Исходная перестановка: {mas}"
    )

    output.append("")
    output.append(
        "--- Формирование соответствия ---"
    )

    first_line = sorted(mas)

    output.append(
        f"Первая строка: {first_line}"
    )
    output.append(
        f"Вторая строка: {mas}"
    )

    di = dict(zip(first_line, mas))

    output.append("")
    output.append(
        f"Полученное соответствие: {di}"
    )

    output.append("")
    output.append(
        "--- Построение обратной перестановки ---"
    )

    sorted_mas = sorted(
        mas,
        key=lambda x: di[x]
    )

    for i in range(len(sorted_mas)):
        output.append(
            f"Шаг {i + 1}: {sorted_mas[i]}"
        )

    output.append("-" * 45)

    output.append(
        f"=> Обратная перестановка: {sorted_mas}"
    )
    output.append("\n")
    return "\n".join(output)