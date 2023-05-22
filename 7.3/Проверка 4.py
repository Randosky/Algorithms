from collections import OrderedDict

n, W = map(int, input().split())

menu = OrderedDict()
for i in range(n):
    p, c = map(int, input().split())
    menu[i] = (p, c)

best = [[0, 0, []]]

for i, (p, c) in menu.items():
    new_best = []
    for cost, cal, items in best:
        new_cost = cost + p
        new_cal = cal + c
        if new_cost <= W:
            new_items = items + [i]
            new_best.append([new_cost, new_cal, new_items])

    best += new_best
    best.sort(key=lambda x: (-x[1], -len(x[2]), x[2]))

ans_cost, ans_cal, ans_items = best[0]
ans_items = [i+1 for i in ans_items]

print(len(ans_items), ans_cal)
print(*ans_items)
