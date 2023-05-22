# функция для подсчёта веса строки
def calculate_weight(s, weights):
    n = len(s)
    max_dist = [0] * 32  # массив максимальных расстояний
    for i in range(n):
        c = ord(s[i]) - ord('а')
        dist = max(i, n-1-i)
        if dist > max_dist[c]:
            max_dist[c] = dist
    weight = sum(max_dist[c] * weights[c] for c in range(32))
    return weight

# считываем строку и веса букв
s = input().strip()
weights = list(map(int, input().strip().split()))

# подсчитываем вес строки
weight = calculate_weight(s, weights)

# запускаем цикл перестановок
changed = True
while changed:
    changed = False
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            # переставляем символы
            s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
            new_weight = calculate_weight(s, weights)
            if new_weight > weight:
                # сохраняем строку и обновляем вес
                max_s = s
                weight = new_weight
                changed = True
            # возвращаем символы на свои места
            s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]

# выводим результат
print(max_s, weight)
