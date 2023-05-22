from collections import defaultdict
orks = list(map(int, input().split()))
height = map(int, input().split())

# Словарь, где ключ - уникальное значение роста, а значение - список индексов этих ростов в массиве orks
d = defaultdict(list)
for i, v in enumerate(orks):
    d[v].append(orks.index(v, i))

# count_right рассчитывается по формуле:
# общее кол-во справа (len(orks) - ind - 1) - кол-во с равными справа, где кол-во с равными справа равно:
# общая длина текущего массива (len(d[h]) - кол-во равных слева (count_left = i + 1)
for h in height:
    count_left, count_right, maxCount = 0, 0, 0
    for i, ind in enumerate(d[h]):
        count_left = i + 1 # Кол-во равных слева
        count_right = len(orks) - ind - len(d[h]) + i # Кол-во неравных справа
        current = count_left * count_right
        maxCount = current if current > maxCount else maxCount
    print(maxCount, end=" ")