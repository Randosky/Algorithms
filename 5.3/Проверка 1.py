from collections import deque


class Queue:
    def __init__(self):
        self.knight = deque()
        self.nobleman = deque()

    def pushKnight(self, i):
        self.knight.append(i)

    def pushNobleman(self, i):
        self.nobleman.append(i)
        for i in range(len(self.knight) // 2):
            self.nobleman.appendleft(self.knight[i])
            self.knight.popleft()

    def pushPrince(self, i):
        self.nobleman.appendleft(i)

    def pop(self):
        if len(self.nobleman) != 0:
            res = self.nobleman.popleft()
            # if res == "2500":
            #     return [i for i in self.nobleman], [i for i in self.knight]
            return res
        res = self.knight.popleft()
        return res


queue = Queue()
commands = {'+': queue.pushKnight, '*': queue.pushNobleman, '!': queue.pushPrince}
answers = []

for person in range(int(input())):
    cmd = input().strip().split()
    commands[cmd[0]](cmd[1]) if cmd[0] in commands else answers.append(queue.pop())

print(*answers, sep="\n")
