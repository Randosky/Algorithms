def partition(arr, l, r):
    if r - l <= 1:
        return l

    pivot = arr[r - 1][0]
    i = l
    j = r - 1

    while i <= j:
        while arr[i][0] < pivot: i += 1
        while arr[j][0] > pivot: j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break

    return i


def quick_sort(arr, l, r):
    if r - l <= 1:
        return

    m = partition(arr, l, r)
    quick_sort(arr, l, m)
    quick_sort(arr, m, r)
    # while not r - l <= 1:
    #     m = partition(arr, l, r)
    #     if m - l > r - m:
    #         quick_sort(arr, m, r)
    #         r = m
    #     else:
    #         quick_sort(arr, l, m)
    #         l = m

b = [list(map(int, input().split())) for i in range(int(input()))]
# n = int(input())
# b = []
# for _ in range(n):
#     b.append(tuple(map(int, input().split())))
p = list(map(int, input().split()))
quick_sort(b, 0, len(b))
p_c = [0] * len(p)

for ind, p_item in enumerate(p):
    for b_item in b:
        if b_item[0] > p_item:
            break
        if b_item[1] >= p_item:
            p_c[ind] += 1

print(*p_c, sep="\n")
