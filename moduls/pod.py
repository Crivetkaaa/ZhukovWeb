def solve_permutation_power(permutation_str, power):
    output = []
    
    output.append("=== ВОЗВЕДЕНИЕ ПОДСТАНОВКИ В СТЕПЕНЬ ===")
    output.append(f"Исходная подстановка: {permutation_str}")
    output.append(f"Степень: {power}\n")
    
    cleaned = permutation_str.replace("(", "")
    cycles = cleaned.split(")")[:-1]
    
    output.append("--- Шаг 1: Расчет остатков и сдвиг элементов ---")
    final_cycles = []
    
    for i, c in enumerate(cycles, 1):
        c_len = len(c)
        new_power = power % c_len
        output.append(f"Цикл {i}: ({c})")
        output.append(f"  Длина цикла: {c_len}")
        output.append(f"  Остаток от деления степени: {power} % {c_len} = {new_power}")
        
        if new_power == 0:
            output.append(
                f"  Результат: цикл переходит в тождественную подстановку (e). "
                f"Элементы на своих местах."
                )
            final_cycles.append(f"({c})")
            continue
            
        transitions = {}
        for j in range(c_len):
            current_elem = c[j]
            next_elem = c[(j + new_power) % c_len]
            transitions[current_elem] = next_elem
            
        visited = set()
        sub_cycles = []
        
        for elem in c:
            if elem not in visited:
                shifted_c_list = []
                curr = elem
                while curr not in visited:
                    visited.add(curr)
                    shifted_c_list.append(curr)
                    curr = transitions[curr]
                
                if len(shifted_c_list) > 1:
                    sub_cycles.append(f"({''.join(shifted_c_list)})")
        
        if sub_cycles:
            res_c = "".join(sub_cycles)
            output.append(f"  Результат после сдвига на {new_power} поз. вперед: {res_c}")
            final_cycles.extend(sub_cycles)
        else:
            output.append(f"  Результат: элементы цикла образуют только неподвижные точки (исчезают).")
    
    output.append("-" * 45)
    
    res = "".join(final_cycles)
    if not res:
        res = "e (тождественная подстановка — все элементы на своих местах)"
        
    output.append(f"=> Результат: {res}")
    
    return "\n".join(output)
