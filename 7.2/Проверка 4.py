# def brs(index, sec_index, array, minimum, maximum):
#     if sec_index == k:
#         return
#
#     if index == k:
#         print(*array)
#         brs(0, sec_index + 1, [], minimum, maximum + k - 1)
#     else:
#         array.append(maximum)
#         brs(index + 1, sec_index, array, minimum, maximum - 1)
#
#
# if __name__ == "__main__":
#     k, mn, mx = map(int, input().split())
#     brs(0, 0, [], mn, mx)
#     # print(total_count)


import itertools

m = 36
n = 39
k = 3

# создаем список чисел в диапазоне m до n
numbers = list(range(m, n + 1))

# генерируем все возможные размещения длины k из списка чисел
arrangements = list(itertools.permutations(numbers, k))
srt = sorted(arrangements, reverse=True)

count = 0
for i in range(len(srt)):
    arr = srt[i]
    if arr[0] < arr[1] < arr[2]:
        print(*arr[::-1])
        count += 1

print(count)