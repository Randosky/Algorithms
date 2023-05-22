def bubble(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                t = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = t
        if i == k - 1:
            print(*lst)

inputArray = list(map(int, input().split()))
k = int(input())

bubble(inputArray)
print(*inputArray)
