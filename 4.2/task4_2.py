from collections import deque

operations = {
    "+": lambda x, y : x + y,
    "-": lambda x, y : x - y,
    "*": lambda x, y : x * y,
    "/": lambda x, y : x // y,
    "%": lambda x, y : x % y,
}

stack = deque()
for char in input().split():
    if char in operations:
        b, a =  stack.pop(), stack.pop()
        stack.append(operations[char](a, b))
    else:
        stack.append(int(char))

print(stack.pop())
