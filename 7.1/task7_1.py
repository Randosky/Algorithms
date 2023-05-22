def count_pairs(array):
    length = len(array)
    if length <= 1:
        return 0

    left = array[:length // 2]
    right = array[length // 2:]

    count = count_pairs(left) + count_pairs(right)

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            count += len(left) - i
            j += 1
        else:
            i += 1

    array.sort()
    return count


n = int(input())
stones = [int(input()) for _ in range(n)]
print(count_pairs(stones))
