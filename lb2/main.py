from list_def import modular_inverse, extended_euclidean, solve_modular_equation

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

if __name__ == "__main__":

    com = ''

    while(com!='exit'):
        print("1. Нахождения НОД(a,m)" +
              "2. Вычисление элемента, обратного к данному элементу в кольце вычетов по заданному модулю.\n" +
              "3. Решение сравнения вида 'ax mod m ≡ b'.\n" +
              "4. Расшифровка.\n" +
              "5. Шифровка\n" +
              "exit\n")
        
        com = str(input("Выберите действие: "))

        if (com == "1"):
            nod()

        elif (com == "2"):
            Obratno_A()

        elif (com == "3"):
            SoMoEq()

        elif (com == "4"):
            pass

        elif (com == "5"):
            pass
