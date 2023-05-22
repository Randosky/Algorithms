n, m = map(int, input().split())
plates = list(input().split())

ans = [n]

for i in range(1, n // 2 + 1):
    count = 0
    flag = True

    for j in range(i):
        if plates[i - j - 1] == plates[i + j]:
            count += 1
        else:
            flag = False
            break

    if flag:
        ans.append(len(plates) - count)

print(*ans)
