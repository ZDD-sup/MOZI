import re
import math
from collections import Counter

alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"  # 0-31 позиций, 32 шт

def preprocess_text(text):
    text = text.lower()
    text = text.replace('ё', 'е') if 'е' in alphabet else text
    allowed_chars = f"[^{alphabet}]"
    text = re.sub(allowed_chars, '', text)
    return text

# Функция для получения k-грамм
def get_k_grams(text, k):
    return [text[i:i+k] for i in range(len(text) - k + 1)]

# Функция для вычисления частоты k-грамм
def compute_frequencies(k_grams):
    return Counter(k_grams)

# Функция для вычисления энтропии k-грамм
def compute_entropy(frequencies, total_k_grams):
    entropy = 0
    for count in frequencies.values():
        p = count / total_k_grams
        entropy -= p * math.log2(p)
    return entropy

# Функция для вычисления энтропии для разных значений k
def calculate_entropy_for_k(text, max_k):
    entropies = []
    for k in range(1, max_k + 1):
        k_grams = get_k_grams(text, k)
        frequencies = compute_frequencies(k_grams)
        total_k_grams = len(k_grams)
        entropy = compute_entropy(frequencies, total_k_grams)
        # Нормализуем энтропию
        normalized_entropy = entropy / (k ** k)
        entropies.append((k, normalized_entropy))
    return entropies