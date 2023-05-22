n, bag = map(int, input().split())

cakes = []
for _ in range(n):
    price, volume = map(int, input().split())
    cakes.append((price/volume, price, volume))

cakes.sort(reverse=True)

final_cost = 0
for cake in cakes:
    if bag >= cake[2]:
        bag -= cake[2]
        final_cost += cake[1]
    else:
        final_cost += bag * cake[0]
        break

print(cakes)
print('{:.2f}'.format(final_cost))
