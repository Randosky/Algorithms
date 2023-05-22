import sys
from collections import deque


class Queue:
    def __init__(self):
        self.queue = deque()

    def pushKnight(self, i):
        self.queue.append(i)
        return

    def pushNobleman(self, i):
        if len(self.queue) % 2 == 0:
            half = len(self.queue)//2
        else:
            half = len(self.queue)//2 + 1
        self.queue.insert(half, i)
        return

    def pushPrince(self, i):
        self.queue.appendleft(i)
        return

    def pop(self):
        return self.queue.popleft()


queue = Queue()
commands = {'+': queue.pushKnight, '*': queue.pushNobleman, '!': queue.pushPrince}
answers = []

n = input()
for cmd in sys.stdin:
    cmd = cmd.strip().split()
    commands[cmd[0]](cmd[1]) if cmd[0] in commands else answers.append(queue.pop())

print(*answers, sep="\n")