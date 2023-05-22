from collections import deque
inputTXT = open("input.txt", "r")
size = int(inputTXT.readline())
outputTXT = open("output.txt", "w")
stack = deque()

def push(string):
    _, value = string.split()
    if size == len(stack) and size != 0:
        stack.popleft()
    if size != 0:
        stack.append(value)
    outputTXT.write('ok\n')

def pop():
    outputTXT.write(str(stack.pop()) + '\n')

def count():
    outputTXT.write(str(len(stack)) + '\n')

def exit():
    outputTXT.write('bye\n')


for line in inputTXT:
    line = line.strip()
    if line[:4] == "push":
        push(line)
    elif line == "count":
        count()
    elif line == "pop":
        pop()
    elif line == "exit":
        exit()
        break
