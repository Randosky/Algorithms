from collections import deque

operations = ["+", "-", "*", "/", "%"]
stack = deque()

for symbol in input().split():
    if symbol in operations:
        y, x = stack.pop(), stack.pop()
        if symbol == "+":
            stack.append(x + y)
        if symbol == "-":
            stack.append(x - y)
        if symbol == "*":
            stack.append(x * y)
        if symbol == "/":
            stack.append(x // y)
        if symbol == "%":
            stack.append(x % y)
    else:
        stack.append(int(symbol))

print(stack.pop())
