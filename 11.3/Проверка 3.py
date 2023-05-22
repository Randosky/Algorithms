from collections import deque


def action_1(msg):
    if msg // (10 ** (len(str(msg)) - 1)) != 9:
        msg += 10 ** (len(str(msg)) - 1)
    return msg


def action_2(msg):
    if msg % 10 != 1:
        msg -= 1
    return msg


def action_3(msg):
    return int(str(msg)[-1] + str(msg)[:-1])


def action_4(msg):
    return int(str(msg)[1:] + str(msg)[0])


def getPath(e, q):
    p = []
    while e:
        p.append(e)
        e = q[e]
    return p


def getFullPath(s, e):
    q = {s: None}
    numbersInUse = deque()
    numbersInUse.append(s)

    while numbersInUse:
        digit = numbersInUse.popleft()
        nextDigits = [action_1(digit), action_2(digit), action_3(digit), action_4(digit)]

        for nextDigit in nextDigits:
            if nextDigit not in q:
                numbersInUse.append(nextDigit)
                q[nextDigit] = digit

    return getPath(e, q)


if __name__ == "__main__":
    queue = getFullPath(int(input()), int(input()))
    print(*reversed(queue), sep="\n")
