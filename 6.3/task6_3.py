array = list(map(int, input().split()))

def choice_sort(arr):
    for i in range(len(arr)):
        pt = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[pt]:
                pt = j
        arr[i], arr[pt] = arr[pt], arr[i]
        if i == len(array) // 2 - 1:
            print(" ".join(map(lambda x: str(x), arr)))

choice_sort(array)
print(" ".join(map(lambda x: str(x), array)))
