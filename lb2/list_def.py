def gcd_extended(a, b):
    """
    Расширенный алгоритм Евклида: находит НОД двух чисел и коэффициенты x и y,
    такие что a * x + b * y = НОД(a, b).

    Параметры:
    a (int): Первое число.
    b (int): Второе число.

    Возвращает:
    tuple: Кортеж из трех элементов:
        - int: НОД(a, b)
        - int: Коэффициент x, такой что a * x + b * y = НОД(a, b)
        - int: Коэффициент y, такой что a * x + b * y = НОД(a, b)

    Примечание:
    Алгоритм может использоваться для решения линейных диофантовых уравнений
    и для нахождения обратных элементов по модулю.
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(element, modulus):
    """
    Вычисляет обратный элемент в кольце вычетов по модулю.

    Параметры:
    element (int): Элемент, для которого требуется найти обратный по модулю.
    modulus (int): Модуль, относительно которого вычисляется обратный элемент.

    Возвращает:
    int или None: Обратный элемент для заданного элемента по модулю, если он существует. 
                  Если обратный элемент не существует (т.е. НОД(element, modulus) ≠ 1), 
                  возвращает None.
    """
    gcd, x, _ = gcd_extended(element, modulus)
    
    if gcd != 1:
        print(f"Элемент {element} не имеет обратного по модулю {modulus}")
        return None
    
    return x % modulus


def solve_modular_equation(a, b, m):
    """
    Решает сравнение a * x ≡ b (mod m) и находит все решения, если они существуют.

    Параметры:
    a (int): Коэффициент перед переменной x в уравнении.
    b (int): Константа в уравнении.
    m (int): Модуль, по которому производится вычисление.

    Возвращает:
    list: Список всех решений x, удовлетворяющих уравнению. Если решений нет, возвращает пустой список.
    """
    gcd, x, _ = gcd_extended(a, m)
    
    if b % gcd != 0:
        print("Решений нет, так как НОД(a, m) не делит b.")
        return []

    x0 = (x * (b // gcd)) % m
    solutions = [(x0 + i * (m // gcd)) % m for i in range(gcd)]
    
    print(f"Решения для {a} * x ≡ {b} (mod {m}): {solutions}")
    return solutions


def encode(a: int, b: int, text: str, alphabet: str) -> str:
    """
    Шифрует текст с использованием линейного шифра (a * x + b) по заданному алфавиту.

    Параметры:
    a (int): Коэффициент для шифрования (множитель).
    b (int): Смещение для шифрования (константа).
    text (str): Входной текст, который необходимо зашифровать.
    alphabet (str): Строка, представляющая алфавит, используемый для шифрования.

    Возвращает:
    str: Зашифрованный текст, в котором символы, входящие в указанный алфавит, заменяются на соответствующие зашифрованные символы,
         а остальные символы (например, пробелы и пунктуация) остаются без изменений.
    """
    new_text = []
    for letter in text:
        if letter == 'Ё':
            letter = 'Е'

        if letter in alphabet:
            x = alphabet.index(letter)
            y = (a * x + b) % len(alphabet)
            new_text.append(alphabet[y])
        else:
            new_text.append(letter)

    return ''.join(new_text)


def solve_system_of_congruences(a, b, c, d, m):
    """
    Решает систему сравнений вида:
    (a*x + y) mod m ≡ b
    (c*x + y) mod m ≡ d

    Параметры:
    a (int): Коэффициент в первом уравнении.
    b (int): Константа в первом уравнении.
    c (int): Коэффициент во втором уравнении.
    d (int): Константа во втором уравнении.
    m (int): Модуль.

    Возвращает:
    list: Список решений для (x, y). Если решений нет, возвращает пустой список.
    """
    solutions = []

    delta = (d - b) % m
    coef = (c - a) % m
    gcd_coef, _, _ = gcd_extended(coef, m)
    if gcd_coef == 0 or delta % gcd_coef != 0:
        print("Система сравнений не имеет решений для заданных параметров.")
        return []

    for x in range(m):  # Перебираем все возможные значения x
        y = (b - a * x) % m  # Находим y из первого уравнения
        if (c * x + y) % m == d:  # Проверяем, удовлетворяет ли y второму уравнению
            solutions.append((x, y))

    return solutions


def frequency_analysis(cipher_text):
    """
    Выполняет частотный анализ шифротекста и возвращает отсортированный список букв по убыванию частоты.

    Параметры:
    cipher_text (str): Зашифрованный текст.

    Возвращает:
    list: Список кортежей, где каждый кортеж содержит букву и её частоту, отсортированный по убыванию частоты.
    """
    frequency = {}
    
    for char in cipher_text:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1

    return sorted(frequency.items(), key=lambda item: item[1], reverse=True)
