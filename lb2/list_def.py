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

