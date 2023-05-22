n, m = map(int, input().split())
plates = list(input().split())

ans = [n]

# С помощью i мы двигаем зеркало
# Потом идем по получившимся срезам циклом. По левому <---- По правому ---->.
# И если элемент из левого среза == элементу из правого среза (эти элементы стоят на равном растоянии от зеркала)
# Если все такие элементы равны на текущих срезах, то мы можем сказать, что зеркало поставили правильно
# А если хоть раз не равны, то сразу понятно, что они не равны

for i in range(1, n // 2 + 1):
    count = 0
    flag = True

    for j in range(i):
        print(plates[i - j - 1], plates[i + j], "-", i)
        if plates[i - j - 1] == plates[i + j]:
            count += 1
        else:
            flag = False
            break

    if flag:
        ans.append(len(plates) - count)

print(*ans)
