import math
from collections import Counter

def solve_permutation_count_by_order(group_n, order_m):
    output = []
    
    def lcm(a, b):
        return abs(a * b) // math.gcd(a, b)

    def find_valid_partitions(n, m, current_max, current_partition, partitions_list):
        """Рекурсивно находит наборы длин циклов, чей НОК равен m, а сумма <= n."""
        current_lcm = 1
        for x in current_partition:
            current_lcm = lcm(current_lcm, x)
            
        current_sum = sum(current_partition)
        
        if current_lcm == m and current_sum <= n:
            sorted_part = tuple(sorted(current_partition, reverse=True))
            if sorted_part not in partitions_list:
                partitions_list.append(sorted_part)
            
        for x in range(min(current_max, n - current_sum), 1, -1):
            if m % x == 0:
                find_valid_partitions(n, m, x, current_partition + [x], partitions_list)

    output.append("=== ПОДСЧЁТ ПОДСТАНОВОК ЗАДАННОГО ПОРЯДКА ===")
    output.append(f"Симметрическая группа: S_{group_n}")
    output.append(f"Искомый порядок элементов: n = {order_m}\n")
    
    output.append(f"--- Шаг 1: Поиск цикловых структур в S_{group_n} с НОК = {order_m} ---")
    
    raw_partitions = []
    find_valid_partitions(group_n, order_m, group_n, [], raw_partitions)
    
    if not raw_partitions:
        output.append(f"Внимание: В группе S_{group_n} невозможно составить комбинацию циклов с НОК = {order_m}.")
        output.append(f"Максимальная сумма длин циклов не должна превышать {group_n}.\n")
        output.append("-" * 45)
        output.append(f"=> Результат: N_{group_n}^({order_m}) = 0")
        return "\n".join(output)
        
    output.append(f"Найденные базовые комбинации длин циклов (длиной > 1):")
    for part in raw_partitions:
        output.append(f"  * {list(part)}")
    output.append("")
    
    output.append("--- Шаг 2: Расчёт количества подстановок для каждой структуры ---")
    
    total_permutations = 0
    step = 1
    
    for part in raw_partitions:
        current_sum = sum(part)
        full_partition = list(part) + [1] * (group_n - current_sum)
        counts = Counter(full_partition)
        
        output.append(f"Структура {step}: Полный набор циклов (включая неподвижные точки): {full_partition}")
        
        formula_top = f"{group_n}!"
        formula_bottom_parts = []
        denominator = 1
        
        for length in sorted(counts.keys(), reverse=True):
            count = counts[length]
            denominator *= (length ** count) * math.factorial(count)
            formula_bottom_parts.append(f"({length}^{count} * {count}!)")
            
        formula_bottom = " * ".join(formula_bottom_parts)
        num_for_this_part = math.factorial(group_n) // denominator
        total_permutations += num_for_this_part
        
        output.append(f"  Формула: {formula_top} / [{formula_bottom}]")
        output.append(f"  Вычисление: {math.factorial(group_n)} / {denominator} = {num_for_this_part}\n")
        step += 1
        
    output.append("-" * 45)
    output.append(f"=> Финальный ответ: N_{group_n}^({order_m}) = {total_permutations}")
    
    return "\n".join(output)
