dishes_count, money = map(int, input().split())
dishes = []

for i in range(dishes_count):
    dishes.append(list(map(int, input().split())))

def merge_sort(array):
    length = len(array)
    if length <= 1:
        return array

    left = array[:length // 2]
    right = array[length // 2:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

dishes = merge_sort(dishes)

def getBreakfast(arr, ind, count, calories, budget, numbers):
    if ind < 0:
        return 0
    if budget <= 0:
        return [count, calories, budget, numbers]

    for index in range(len(arr)):
        count += 1
        calories += arr[ind-1][1]
        budget -= arr[ind-1][0]
        numbers.append(index)
        print(ind, index)
        return getBreakfast(arr, ind - 1, count, calories, budget, numbers)

print(dishes)
print(getBreakfast(dishes, len(dishes), 0, 0, money, []))
# total_count = 0
# total_calories = 0
# total_price = 0
# numbers = []
#
# for i in range(len(dishes)):
#     if total_price + dishes[i][0] <= money:
#         total_price += dishes[i][0]
#         total_calories += dishes[i][1]
#         numbers.append(dishes[i][2])
#         total_count += 1
#     else:
#         break
#
# print(total_count, total_calories)
# numbers.sort()
# print(*numbers)
