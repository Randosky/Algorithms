from collections import defaultdict
orks = list(map(int, input().split()))
height = map(int, input().split())


d = defaultdict(list)
for i, v in enumerate(orks):
    d[v].append(orks.index(v, i))

for h in height:
    count_left, count_right, maxCount = 0, 0, 0
    for i, ind in enumerate(d[h]):
        count_left = i + 1
        count_right = len(orks) - ind - len(d[h]) + i
        current = count_left * count_right
        maxCount = current if current > maxCount else maxCount
    print(maxCount, end=" ")