def found(a, max_el=9):
    output = []

    def get_elements(max_el):
        elements = [f"{i}" for i in range(max_el + 1)]
        return elements

    output.append("=== ПОСТРОЕНИЕ ПОДСТАНОВКИ ===")

    output.append("")
    output.append(f"Исходная подстановка: {a}")

    new_a = a.replace("(", "").split(")")[:-1]

    elements = get_elements(max_el)


    up = []
    down = []

    output.append("")
    output.append("--- Поиск образов элементов ---")

    for el in elements:
        original_el = el

        for els in new_a:
            if el in els:
                el = els[
                    (els.index(el) + 1) % len(els)
                ]

        up.append(original_el)
        down.append(el)

        output.append(f"{original_el} -> {el}")

    output.append("")
    output.append("-" * 45)

    output.append(
        f"Верхняя строка: {up}"
    )

    output.append(
        f"Нижняя строка: {down}"
    )

    return "\n".join(output)
