import math

string = input()

def findSubString():
    subString = []
    maxDigit = 0
    currentAnswer = []

    # Если половина
    halfString = string[:len(string) // 2]
    if 2 * halfString == string:
        currentAnswer = [2, halfString]
        maxDigit = 2

    # Достаточно идти до корня длины, потому что больше корня ответ может быть только в половине
    for i in range(int(math.sqrt(len(string)) + 1)):
        subString.append(string[i])
        k = len(string) // len(subString)

        if k * "".join(subString) == string and k > maxDigit:
            currentAnswer = [k, "".join(subString)]
            maxDigit = k

    # Если до корня не нашли и не половина, то ответ только сама строка и 1
    return currentAnswer if currentAnswer else [1, string]

print(*findSubString())

