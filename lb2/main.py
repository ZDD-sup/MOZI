from list_def import modular_inverse, extended_euclidean, solve_modular_equation, encode, solve_system_of_congruences, frequency_analysis

def nod():
    element = int(input("Введите элемент 'a': "))
    modulus = int(input("Введите модуль 'm': "))

    gcd, a, b = extended_euclidean(element, modulus)

    if (a==0):
        print(f"Достигнут базовый случай: a = 0, возвращаем (НОД={b}, x=0, y=1)")
    else:
        print(f"\nРезультат: НОД({a}, {b}) = {gcd}, коэффициенты x = {a}, y = {b}")

def Obratno_A():
    element = int(input("Введите элемент 'a': "))
    modulus = int(input("Введите модуль 'm': "))
    
    modular_inverse(element, modulus)

def SoMoEq():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    m = int(input("Введите значение m: "))

    solve_modular_equation(a, b, m)

def print_encode():
    text_inp = str(input("Введите текстдля шифрования: "))
    a = int(input("Укажите 'a': "))
    b = int(input("Укажите 'b': "))
    encode(a, b, text_inp, alphabet)

def SolSysOfCon():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    d = int(input("Введите значение d: "))
    m = int(input("Введите значение m: "))

    # Решаем систему сравнений
    solutions = solve_system_of_congruences(a, b, c, d, m)

    # Выводим решения
    if solutions:
        print(f"Решения для ({a}*x + y) mod {m} ≡ {b} и ({c}*x + y) mod {m} ≡ {d}: {solutions}")
    else:
        print(f"Решений нет для заданных параметров.")

def text_analis():
    cipher_text = input("Введите зашифрованный текст: ")
    
    frequency_result = frequency_analysis(cipher_text)
    
    print("\nЧастотный анализ шифротекста:")
    for letter, count in frequency_result:
        print(f"Буква: '{letter}' - Частота: {count}")



if __name__ == "__main__":

    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя" # 0-31 позиций, 32шт
    com = ''

    while(com!='exit'):
        print("\n1. Нахождения НОД(a,m)" +
                "2. Вычисление элемента, обратного к данному элементу в кольце вычетов по заданному модулю.\n" +
                "3. Решение сравнения вида 'ax mod m ≡ b'.\n" +
                "4. Решение системы стравнений." +
                "5. Расчитать частоту символов в строке." +
                "6. Расшифровка.\n" +
                "7. Шифровка\n" +
                "exit\n")
        
        com = str(input("Выберите действие: "))

        if (com == "1"):
            nod()

        elif (com == "2"):
            Obratno_A()

        elif (com == "3"):
            SoMoEq()

        elif (com == "4"):
            SolSysOfCon()

        elif (com == "5"):
            text_analis()

        elif (com == "6"):
            pass

        elif (com == "7"):
            print_encode()
