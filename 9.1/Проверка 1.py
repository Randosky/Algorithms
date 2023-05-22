def take_cake(arr, w):
    total_sum = 0
    for item in arr:
        if w < item[1]:
            total_sum += w * item[2]
            break
        else:
            w -= item[1]
            total_sum += item[0]

    return total_sum

n, last_volume = map(int, input().split())

cakes = []
for _ in range(n):
    p, v = map(int, input().split())
    cakes.append((p, v, p/v))

cakes.sort(key=lambda cake: cake[2], reverse=True)
print('{:.2f}'.format(take_cake(cakes, last_volume)))