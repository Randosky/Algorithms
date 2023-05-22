def count_pairs(k, left, right):
    if right - left < 2:
        return 0
    mid = (left + right) // 2
    count = count_pairs(k, left, mid) + count_pairs(k, mid, right)
    i, j = left, mid
    while i < mid and j < right:
        if k[i] >= k[j]:
            count += right - j
            i += 1
        else:
            j += 1
    k[left:right] = sorted(k[left:right])
    return count

n = int(input())
k = []
for i in range(n):
    k.append(int(input()))
print(count_pairs(k, 0, n))
