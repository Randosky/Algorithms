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
    q = {start: [start]}

    index = 0
    while q:
        num = list(q)[0]

        for next_num in [flip_first(num), flip_last(num), shift_right(num), shift_left(num)]:
            if next_num not in q.keys():
                q[next_num] = q[num] + [next_num]
            if next_num == end:
                return q[next_num]

        index += 1
    return {}


s = int(input())
e = int(input())
print(*find_shortest_sequence(s, e), sep="\n")
# queue = find_shortest_sequence(s, e)
# for k, v in queue.items():
#     print(k, v)