from list_def import (
    modular_inverse, 
    gcd_extended, 
    solve_modular_equation, 
    encode, 
    solve_system_of_congruences, 
    frequency_analysis, 
    decode_affine,
    attempt_decrypt,
    save_results_to_file
)

def nod():
    element = int(input("Введите элемент 'a': "))
    modulus = int(input("Введите модуль 'm': "))

    gcd, a, b = gcd_extended(element, modulus)

    if a == 0:
        print(f"Достигнут базовый случай: a = 0, возвращаем (НОД={b}, x=0, y=1)")
    else:
        print(f"\nРезультат: НОД({element}, {modulus}) = {gcd}, коэффициенты x = {a}, y = {b}")

def Obratno_A():
    element = int(input("Введите элемент 'a': "))
    modulus = int(input("Введите модуль 'm': "))
    
    inverse = modular_inverse(element, modulus)
    if inverse is not None:
        print(f"Обратный элемент для {element} по модулю {modulus} равен {inverse}")

def SoMoEq():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    m = int(input("Введите значение m: "))

    solutions = solve_modular_equation(a, b, m)

    if solutions:
        print(f"Решения для {a} * x ≡ {b} (mod {m}): {solutions}")
    else:
        print("Решений нет.")

def print_encode():
    text_inp = input("Введите текст для шифрования: ")
    a = int(input("Укажите 'a': "))
    b = int(input("Укажите 'b': "))
    encrypted_text = encode(a, b, text_inp, alphabet)
    print(f"Зашифрованный текст: {encrypted_text}")

def SolSysOfCon():
    a = int(input("Введите значение a: "))
    b = int(input("Введите значение b: "))
    c = int(input("Введите значение c: "))
    d = int(input("Введите значение d: "))
    m = int(input("Введите значение m: "))

    solutions = solve_system_of_congruences(a, b, c, d, m)

    if solutions:
        print(f"Решения для ({a}*x + y) mod {m} ≡ {b} и ({c}*x + y) mod {m} ≡ {d}: {solutions}")
    else:
        print("Решений нет для заданных параметров.")

def text_analis():
    cipher_text = input("Введите зашифрованный текст: ")
    
    frequency_result = frequency_analysis(cipher_text)
    
    print("\nЧастотный анализ шифротекста:")
    for letter, count in frequency_result:
        print(f"Буква: '{letter}' - Частота: {count}")

def decrypt_text():
    cipher_text = input("Введите зашифрованный текст для расшифровки: ")
    known_pairs = {}  # Вы можете добавить известные пары, например: {'А': 'Е', 'Б': 'И'}
    results = attempt_decrypt(cipher_text, alphabet, known_pairs)

    # Сохранение результатов в файл
    save_file = input("Хотите сохранить результаты в файл? (y/n): ").strip().lower()
    if save_file == 'y':
        filename = input("Введите имя файла для сохранения: ")
        save_results_to_file(results, filename)
        print(f"Результаты сохранены в {filename}")

if __name__ == "__main__":

    alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"  # 0-31 позиций, 32 шт
    com = ''

    while com != 'exit':
        print("\n1. Нахождения НОД(a,m)" +
              "\n2. Вычисление элемента, обратного к данному элементу в кольце вычетов по заданному модулю." +
              "\n3. Решение сравнения вида 'ax mod m ≡ b'." +
              "\n4. Решение системы сравнений." +
              "\n5. Расчитать частоту символов в строке." +
              "\n6. Расшифровка." +
              "\n7. Шифровка." +
              "\nexit\n")
        
        com = input("Выберите действие: ")

        if com == "1":
            nod()
        elif com == "2":
            Obratno_A()
        elif com == "3":
            SoMoEq()
        elif com == "4":
            SolSysOfCon()
        elif com == "5":
            text_analis()
        elif com == "6":
            decrypt_text()
        elif com == "7":
            print_encode()
        elif com == "exit":
            print("Выход из программы.")
        else:
            print("Некорректный выбор. Пожалуйста, выберите действие снова.")
