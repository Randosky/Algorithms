import math


def getSub(string):
    sub, kMax, ans, str_len = [], 0, [1, string], len(string)

    half = string[:str_len // 2]
    if half * 2 == string:
        kMax = 2
        ans = [kMax, half]

    for i in range(round(math.sqrt(str_len))):
        sub.append(string[i])
        k = str_len // len(sub)

        if "".join(sub) * k == string and k > kMax:
            kMax = k
            ans = [kMax, "".join(sub)]

    return ans


print(*getSub(input()))
