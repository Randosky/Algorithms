n, m = map(int, input().split())
plates = list(input().split())

# n, m = 6, 2
# n, m = 7, 2
# n, m = 5, 2
# plates = ['1', '1', '2', '2', '1', '1']
# plates = ["1", "1", "1", "2", "2", "1", "1"]
# plates = ["1", "2", "2", "1", "1"]
ans = [n]

for i in range(1, n//2 + 1):
    right_b_m = plates[:i]
    right_a_m = plates[i:]
    flag = True
    for j in range(len(right_b_m)):
        if right_b_m[-j-1] != right_a_m[j]:
            flag = False
            break
    if flag:
        ans.append(len(right_a_m))

print(*ans)