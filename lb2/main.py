from list_def import modular_inverse

if __name__ == "__main__":
    # Ввод элемента и модуля с консоли
    element = int(input("Введите элемент: "))
    modulus = int(input("Введите модуль: "))
    
    # Вычисление и вывод результата
    modular_inverse(element, modulus)