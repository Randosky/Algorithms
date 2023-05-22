dishes_count, money = map(int, input().split())
dishes = []

for i in range(dishes_count):
    dishes.append(list(map(int, input().split())) + [i + 1])

def merge_sort(array):
    length = len(array)
    if length <= 1:
        return

    left = array[:length // 2]
    right = array[length // 2:]

    merge_sort(left)
    merge_sort(right)

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] >= right[j][0]:
            j += 1
        else:
            i += 1

    array.sort()
    return array

dishes = merge_sort(dishes)
total_count = 0
total_calories = 0
total_price = 0
numbers = []

i = 0
while total_price < money:
    total_price += dishes[i][0]
    if total_price <= money:
        total_count += 1
        total_calories += dishes[i][1]
        numbers.append(dishes[i][2])
        i += 1
    else: break

print(total_count, total_calories)
numbers.sort()
print(*numbers)