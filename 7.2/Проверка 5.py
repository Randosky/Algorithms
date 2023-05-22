# def generate_arrangements(m, n, k):
#     if k == 0:
#         return [[]]
#     arrangements = []
#     for i in range(n, m, -1):
#         for j in generate_arrangements(i+1, n, k-1):
#             arrangements.append([i] + j)
#     return arrangements
#
#
# m = 36
# n = 39
# k = 3
#
# arrangements = generate_arrangements(m, n, k)
#
# print(*arrangements, sep="\n")
# print(len(arrangements))
from itertools import combinations

k, mn, mx = map(int, input().split())
count = 0
for i in combinations([i for i in range(mn, mx+1)], k):
    count += 1
    print(*list(reversed(i)))
print(count)