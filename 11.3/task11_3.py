from collections import deque


def flip_first(num):
    l = len(str(num)) - 1
    first = num // (10 ** l)
    if first != 9:
        num += 10 ** l
    return num


def flip_last(num):
    last = num % 10
    if last != 1:
        num -= 1
    return num


def shift_right(num):
    return int(str(num)[-1] + str(num)[:-1])


def shift_left(num):
    return int(str(num)[1:] + str(num)[0])


def find_shortest_sequence(start, end):
    q = {start: None}
    numbers = deque()
    numbers.append(start)

    while numbers:
        num = numbers.popleft()

        for next_num in [flip_first(num), flip_last(num), shift_right(num), shift_left(num)]:
            if next_num not in q:
                numbers.append(next_num)
                q[next_num] = num

    path = []
    while end:
        path.append(end)
        end = q[end]

    return path


s = int(input())
e = int(input())
print(*reversed(find_shortest_sequence(s, e)), sep="\n")
