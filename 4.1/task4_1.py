from collections import deque
f_in = open("input.txt", "r")
f_out = open("output.txt", "w")
size = int(f_in.readline())
stack = deque()

for line in f_in:
    line = line.strip()
    if line.startswith("push"):
        _, value = line.split()
        if size == len(stack) and size != 0:
            stack.popleft()
        if size != 0:
            stack.append(value)
        f_out.write('ok\n')

    elif line == "pop":
        f_out.write(f'{stack.pop()}\n')

    elif line == "count":
        f_out.write(f'{len(stack)}\n')

    elif line == "exit":
        f_out.write('bye\n')
        break
