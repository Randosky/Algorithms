import sys

queue = []
answers = []

n = input()
for line in sys.stdin:
    line = line.strip().split()
    if line[0] == "+":
        queue.append(line[1])
    elif line[0] == "*":
        if len(queue) % 2 == 0:
            half = len(queue) // 2
        else:
            half = len(queue) // 2 + 1
        queue.insert(half, line[1])
    elif line[0] == "!":
        queue.insert(0, line[1])
    elif line[0] == "-":
        print(queue.pop(0), end="\n")
print(*answers, sep="\n")
