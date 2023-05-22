# n, m = map(int, input().split())
# plates = list(input().split())

# n, m = 6, 2
n, m = 7, 2
# n, m = 5, 2
# plates = ['1', '1', '2', '2', '1', '1']
plates = ["1", "1", "1", "2", "2", "1", "1"]
# plates = ["1", "2", "2", "1", "1"]
ans = [n]

for i in range(1, n//2 + 1):
    right_b_m = plates[:i]
    right_a_m = plates[i:]
    if right_b_m == right_a_m[:len(right_b_m)][::-1]:
        ans.append(len(right_a_m))

    print(i - 1, i)
    print(right_b_m, right_a_m, len(right_a_m))
    print(right_b_m, right_a_m[:len(right_b_m)][::-1])
    print()

print(*ans)