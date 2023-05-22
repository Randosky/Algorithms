def partition(array):
    pivot = array[len(array) // 2]
    l = [x for x in array if x < pivot]
    r = [x for x in array if x > pivot]
    e = [x for x in array if x == pivot]

    return l, e, r

def kth_element(array, k):
    if len(array) == 1:
        return array[0]

    l, e, r = partition(array)

    if k < len(l):
        return kth_element(l, k)
    elif k < len(l) + len(e):
        return e[0]
    else:
        return kth_element(r, k - len(l) - len(e))


lst = list(map(int, input().split()))
print(kth_element(lst, int(input())))