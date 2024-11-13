from grafics import iface

# def main():
#     alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"  # 0-31 позиций, 32 шт
#     # Текст для анализа
#     text = str(input("Введите текст: "))

#     # Предобработка текста
#     processed_text = preprocess_text(text,alphabet)

#     # Расчет энтропии для k от 1 до 5
#     entropies = calculate_entropy_for_k(processed_text, 5)

#     # Вывод результатов
#     for k, entropy in enumerate(entropies, start=1):
#         print(f"Энтропия для {k}-грамм / {k}^{k}: {entropy:.4f}")

if __name__ == "__main__":
    iface.launch()