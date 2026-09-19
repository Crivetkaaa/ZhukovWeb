def solve_slae(matrix, z):
    matrix = [row[:] for row in matrix]

    rows = len(matrix)
    cols = len(matrix[0])
    num_vars = cols - 1

    output = []

    def mod(x):
        return x % z

    def print_matrix():
        for row in matrix:
            output.append(f"  {row}")
        output.append("")

    inverses = {
        el: pow(el, -1, z)
        for el in range(1, z)
    }

    output.append("=== ИСХОДНАЯ МАТРИЦА ===")
    print_matrix()

    output.append("=== НАЧАЛО ПРЯМОГО ХОДА МЕТОДА ГАУССА ===")
    output.append("")

    r_idx = 0
    pivot_cols = []

    for c_idx in range(num_vars):
        if r_idx >= rows:
            break

        pivot = matrix[r_idx][c_idx]

        if pivot == 0:
            for r in range(r_idx + 1, rows):
                if matrix[r][c_idx] != 0:
                    matrix[r_idx], matrix[r] = matrix[r], matrix[r_idx]
                    pivot = matrix[r_idx][c_idx]

                    output.append(
                        f"[ДЕЙСТВИЕ]: Поменяли местами "
                        f"Строку {r_idx} и Строку {r}"
                    )
                    print_matrix()
                    break
            else:
                output.append(
                    f"[ИНФО]: Столбец c_idx={c_idx} "
                    f"под строкой r_idx={r_idx} содержит только нули."
                )
                output.append("")
                continue

        pivot_cols.append(c_idx)

        if pivot != 1:
            inv = inverses[pivot]

            matrix[r_idx] = [
                mod(el * inv)
                for el in matrix[r_idx]
            ]

            output.append(
                f"[ДЕЙСТВИЕ]: Умножаем Строку {r_idx} "
                f"на {inv} (обратный элемент к {pivot} mod {z}), "
                f"чтобы получить ведущую 1:"
            )
            print_matrix()

        for r in range(r_idx + 1, rows):
            leading = matrix[r][c_idx]

            if leading != 0:
                matrix[r] = [
                    mod(
                        matrix[r][c] -
                        leading * matrix[r_idx][c]
                    )
                    for c in range(cols)
                ]

                output.append(
                    f"[ДЕЙСТВИЕ]: Из Строки {r} вычитаем "
                    f"(Строка {r_idx} * {leading}), "
                    f"чтобы обнулить элемент под ведущей единицей:"
                )
                print_matrix()

        r_idx += 1

    output.append(
        "=== НАЧАЛО ОБРАТНОГО ХОДА "
        "МЕТОДА ГАУССА-ЖОРДАНА ==="
    )
    output.append("")

    for step in range(len(pivot_cols) - 1, -1, -1):
        pivot_row = step
        pivot_col = pivot_cols[step]

        for r in range(pivot_row - 1, -1, -1):
            upper_element = matrix[r][pivot_col]

            if upper_element != 0:
                matrix[r] = [
                    mod(
                        matrix[r][c] -
                        upper_element * matrix[pivot_row][c]
                    )
                    for c in range(cols)
                ]

                output.append(
                    f"[ДЕЙСТВИЕ]: Из Строки {r} вычитаем "
                    f"(Строка {pivot_row} * {upper_element}), "
                    f"чтобы обнулить элемент "
                    f"НАД ведущей единицей:"
                )
                print_matrix()

    free_cols = [
        c
        for c in range(num_vars)
        if c not in pivot_cols
    ]

    vector_free = [0] * num_vars

    vectors_free_vars = {
        free_c: [0] * num_vars
        for free_c in free_cols
    }

    for r, pivot_col in enumerate(pivot_cols):
        vector_free[pivot_col] = matrix[r][-1]

        for free_c in free_cols:
            vectors_free_vars[free_c][pivot_col] = mod(
                -matrix[r][free_c]
            )

    for free_c in free_cols:
        vectors_free_vars[free_c][free_c] = 1

    output.append(
        f"=== ОБЩЕЕ РЕШЕНИЕ ДЛЯ МАТРИЦЫ {rows}x{cols} ==="
    )

    output.append(
        f"Базисные переменные: "
        f"{[f'x{p + 1}' for p in pivot_cols]}"
    )

    output.append(
        f"Свободные переменные: "
        f"{[f'x{f + 1}' for f in free_cols]}"
    )

    output.append("")

    mid = num_vars // 2

    for i in range(num_vars):
        left = (
            f"┌ x{i + 1} ┐"
            if i == 0
            else f"└ x{i + 1} ┘"
            if i == num_vars - 1
            else f"│ x{i + 1} │"
        )

        v_free = (
            f"┌ {vector_free[i]} ┐"
            if i == 0
            else f"└ {vector_free[i]} ┘"
            if i == num_vars - 1
            else f"│ {vector_free[i]} │"
        )

        sign = " = " if i == mid else "   "

        right_parts = []

        for free_c in free_cols:
            val = vectors_free_vars[free_c][i]

            v_part = (
                f"┌ {val} ┐"
                if i == 0
                else f"└ {val} ┘"
                if i == num_vars - 1
                else f"│ {val} │"
            )

            if i == mid:
                right_parts.append(
                    f" + x{free_c + 1} * {v_part}"
                )
            else:
                right_parts.append(
                    f"        {v_part}"
                )

        output.append(
            f"{left}{sign}{v_free}"
            f"{''.join(right_parts)}"
        )

    output.append("")
    output.append(
        f"Всего решений = "
        f"{z}^{len(free_cols)} = {z ** len(free_cols)}"
    )

    return "\n".join(output)
