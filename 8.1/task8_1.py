def partition(array, left, right):
    if right - left <= 1:
        return left

    separator = array[right - 1]
    i, j = left, right - 1

    while i <= j:
        while array[i] < separator:
            i += 1
        while i <= j and array[j] >= separator:
            j -= 1

        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    array[i], array[right - 1] = separator, array[i]
    print(separator)

    return i

def qsort(array, left, right):
    if right - left <= 1:
        return

    middle = partition(array, left, right)
    qsort(array, left, middle)
    qsort(array, middle + 1, right)

arr = list(map(int, input().split()))
qsort(arr, 0, len(arr))
print(*arr)