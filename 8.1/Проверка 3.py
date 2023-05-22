def partition(arr, l, r):
    if r - l <= 1:
        return l

    pivot = arr[r - 1]
    print(pivot)
    i = l
    j = r - 1

    while i < j:
        while arr[i] < pivot: i += 1
        while i < j and arr[j] >= pivot: j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        else:
            break

    arr[i], arr[r - 1] = pivot, arr[i]
    return i


def quick_sort(arr, l, r):
    if r - l <= 1:
        return

    m = partition(arr, l, r)
    quick_sort(arr, l, m)
    quick_sort(arr, m + 1, r)

    return arr


lst = list(map(int, input().split()))
sorted_lst = quick_sort(lst, 0, len(lst))
print(" ".join(map(str, sorted_lst)))
