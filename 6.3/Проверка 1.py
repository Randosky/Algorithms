def sort_by_choice(lst):
    for i in range(len(lst)):
        pt = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[pt]:
                pt = j
        key = lst[i]
        lst[i] = lst[pt]
        lst[pt] = key
        if i == len(lst) // 2 - 1:
            print(*lst)


inputArray = list(map(int, input().split()))

sort_by_choice(inputArray)
print(*inputArray)
