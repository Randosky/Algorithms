def findGymnasts(array):
    array.sort()
    temp_array = []
    total_weight = 0
    total_count = 0
    for elem in array:
        if elem[2] >= total_weight:
            temp_array.append(elem)
            temp_array.sort(key=lambda x: x[1])
            total_count += 1
            total_weight += elem[1]
        else:
            if temp_array[len(temp_array) - 1][1] > elem[1]:
                total_weight -= temp_array.pop()[1]
                temp_array.append(elem)
                temp_array.sort(key=lambda x: x[1])
                total_weight += elem[1]

    return total_count

if __name__ == "__main__":
    gymnasts = []

    for _ in range(int(input())):
        n, m, w = input().split(";")
        gymnasts.append((int(m) + int(w), int(w), m))

    count = findGymnasts(gymnasts)
    print(count)
