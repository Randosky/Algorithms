def sort_by_insert(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        pt = i - 1
        while pt >= 0 and key < lst[pt]:
            lst[pt + 1] = lst[pt]
            pt -= 1
        lst[pt + 1] = key
        if len(lst) % 2 == 0 and i == len(lst) // 2 - 1:
            print(*lst)
        elif len(lst) % 2 != 0 and i == len(lst) // 2:
            print(*lst)


inputArray = list(map(int, input().split()))

sort_by_insert(inputArray)
print(*inputArray)
