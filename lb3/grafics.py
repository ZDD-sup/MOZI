import gradio as gr
import matplotlib.pyplot as plt
from list_def import preprocess_text, calculate_entropy_for_k

# Функция для построения графика
def plot_entropy(text):
    # Предобработка текста
    processed_text = preprocess_text(text)

    # Расчет энтропии для k от 1 до 5
    entropies = calculate_entropy_for_k(processed_text, 5)

    # Разделим k и нормализованную энтропию
    k_values = [e[0] for e in entropies]
    entropy_values = [e[1] for e in entropies]

    for k, entropy in zip(k_values, entropy_values):
        print(f"Энтропия для {k}-грамм / {k}^{k}: {entropy:.4f}")

    # Построение графика
    plt.figure(figsize=(8, 6))
    plt.plot(k_values, entropy_values, marker='o', linestyle='-', color='b')
    plt.title('Зависимость H_k(T) / k^k от k')
    plt.xlabel('k')
    plt.ylabel('H_k(T) / k^k')
    plt.grid(True)

    # Вместо plt.close(), используйте plt.show() для визуализации
    plt.tight_layout()
    plt.show()  # Отображаем график локально

    # Для Gradio нужно возвращать объект matplotlib, а не саму функцию
    return plt.gcf()  # График в виде объекта Matplotlib


# Интерфейс Gradio
iface = gr.Interface(
    fn=plot_entropy,
    inputs="text",
    outputs="plot",
    title="График зависимости H_k(T) / k^k от k",
    description="Введите текст, чтобы увидеть график зависимости энтропии для k-грамм (от 1 до 5)."
)

# Запуск интерфейса
iface.launch()