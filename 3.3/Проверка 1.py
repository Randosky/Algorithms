n, m = map(int, input().split())
plates = list(input().split())

ans = [n]

for i in range(1, n // 2 + 1):
    right_a_m = plates[i:]
    right_b_m = plates[:i]
    if right_b_m == right_a_m[:len(right_b_m)][::-1]:
        ans.append(len(right_a_m))
    print("left", "right", plates[i:])
    count = 0
    for j in range(i):
        count += 1
        print(i - j - 1, i + j)
        print(plates[i - j - 1], plates[i + j])
    print()

print(*ans)
