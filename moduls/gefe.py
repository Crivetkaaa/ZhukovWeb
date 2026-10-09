def generate_fec_code(registers: list[str], start_registers: list[str],
                      len_message: int, text: str):

    output = []
    results = []

    len_message = len_message - len(start_registers[0])
    
    def format_bits(bits):
        return " ".join(bits[i:i + 4] for i in range(0, len(bits), 4))

    output.append("=== ГЕНЕРАТОР ГЕФФЕ ===")
    output.append("")

    output.append("Исходные данные:")
    output.append(f"Количество регистров: {len(registers)}")
    output.append(f"Длина выходной последовательности: {len_message}")
    output.append(f"Открытый текст: {format_bits(text)}")
    output.append("")

    for i in range(len(registers)):
        output.append(f"--- Регистр {i} ---")
        output.append(f"Характеристический многочлен: {registers[i]}")
        output.append(f"Начальное состояние: {start_registers[i]}")

        register = registers[i][::-1][0:-1]
        bits = [j for j in range(len(register)) if register[j] == '1']

        init_state = start_registers[i]
        output.append(f"({init_state})")
        init_elements = [f"a_{idx}={val}" for idx, val in enumerate(init_state)]
        output.append(", ".join(init_elements))

        k = 0
        result = start_registers[i]
        n = len(result)  # Начальное количество элементов (степень)

        while k < len_message:
            current_index = n + k
            
            formula_symbols = [f"a_{k + bit}" for bit in bits]
            formula_str = " ⊕ ".join(formula_symbols)
            
            formula_vals = [result[k + bit] for bit in bits]
            vals_str = " ⊕ ".join(formula_vals)

            xor_result = 0
            for bit in bits:
                xor_result ^= int(result[k + bit])

            output.append(f"a_{current_index} = {formula_str}")
            output.append(f"a_{current_index} = {vals_str} = {xor_result}")

            result += str(xor_result)
            k += 1

        results.append(result)
        output.append("")
        output.append(f"Выходная последовательность: {format_bits(result)}")
        output.append("")

    output.append("--- Формирование гаммы генератора Геффе ---")
    output.append("")

    res = ""
    for i, el in enumerate(results[-1]):
        if el == '1':
            res += results[0][i]
        else:
            res += results[1][i]

    output.append(f"Управляющая последовательность: {format_bits(results[-1])}")
    output.append(f"Последовательность регистра 0: {format_bits(results[0])}")
    output.append(f"Последовательность регистра 1: {format_bits(results[1])}")
    output.append("")
    output.append(f"Полученная гамма: {format_bits(res)}")
    output.append("")

    final_result = "".join(str(int(a) ^ int(b)) for a, b in zip(res, text))

    output.append("--- Шифрование открытого текста ---")
    output.append("")
    output.append(f"Открытый текст: {format_bits(text)}")
    output.append(f"Гамма:          {format_bits(res)}")
    output.append(f"Шифртекст:      {format_bits(final_result)}")

    return "\n".join(output)
