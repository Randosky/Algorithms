n, W = map(int, input().split())

menu = []
for i in range(n):
    p, c = map(int, input().split())
    menu.append((p, c, i+1))

best = [[0, 0, []]]

for p, c, i in menu:
    new_best = [ [cost+p, cal+c, items+[i]] for cost, cal, items in best if cost+p<=W ]
    best += new_best
    best.sort(key=lambda x: (-x[1], -len(x[2]), x[2]))

ans_cost, ans_cal, ans_items = best[0]
ans_items = sorted(ans_items)

print(len(ans_items), ans_cal)
print(*ans_items)
