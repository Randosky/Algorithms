def merge_sort_count(lst):
    n = len(lst)
    if n <= 1:
        return lst, 0

    # Разделение на две половины и рекурсивный вызов функции для них
    mid = n // 2
    left, a = merge_sort_count(lst[:mid])
    right, b = merge_sort_count(lst[mid:])

    # Слияние и подсчет количества пар
    result = []
    i = j = count = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            result.append(left[i])
            i += 1
            count += len(right)
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result, a + b + count


n = int(input())
stones = []
for i in range(n):
    stones.append(int(input()))

print(merge_sort_count(stones)[1])