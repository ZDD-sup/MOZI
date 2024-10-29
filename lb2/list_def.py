def extended_euclidean(a, b):
    """Расширенный алгоритм Евклида: находит НОД и коэффициенты x и y."""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def modular_inverse(element, modulus):
    """Вычисляет обратный элемент в кольце вычетов по модулю."""
    gcd, x, _ = extended_euclidean(element, modulus)
    
    # Если НОД не равен 1, то обратного элемента не существует
    if gcd != 1:
        print(f"Элемент {element} не имеет обратного по модулю {modulus}")
        return None
    
    # Приводим x к положительному значению, если он отрицательный
    inverse = x % modulus
    print(f"Обратный элемент для {element} по модулю {modulus} равен {inverse}")
    return inverse

def solve_modular_equation(a, b, m):
    """Решает сравнение a * x ≡ b (mod m) и находит все решения, если они существуют."""
    gcd, x, _ = extended_euclidean(a, m)
    
    # Проверяем, делится ли b на gcd
    if b % gcd != 0:
        print("Решений нет, так как НОД(a, m) не делит b.")
        return []

    # Находим частное решение x0, приводя x к положительному значению
    x0 = (x * (b // gcd)) % m
    solutions = [(x0 + i * (m // gcd)) % m for i in range(gcd)]
    
    # Выводим решения
    print(f"Решения для {a} * x ≡ {b} (mod {m}): {solutions}")
    return solutions
