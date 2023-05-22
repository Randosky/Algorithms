def brs(index, length, array, counter, minimum, maximum):
    if index == length:
        print(" ".join(map(str,array)))
        counter += 1
        return counter

    countLowerI = 0
    for i in range(minimum, maximum + 1):
        if index > 0 and i >= array[index - 1]:
            break
        if countLowerI >= length - index - 1:
            countLowerI += 1
            array[index] = i
            counter = brs(index + 1, length, array, counter, minimum, i - 1)
        else:
            countLowerI += 1
            continue


    return counter

if __name__ == "__main__":
    k, mn, mx = map(int, input().split())
    total_count = brs(0, k, [0] * k, 0, mn, mx)
    print(total_count)
