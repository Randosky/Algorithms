from collections import deque


class Queue:
    queue1 = deque()
    queue2 = deque()
    prince = False

    def push(self, num):
        self.queue1.append(num)

    def pushNoble(self, num):
        self.queue2 = deque(list(self.queue1)[len(self.queue1) // 2 + len(self.queue1) % 2:])
        self.queue1 = deque(list(self.queue1)[:len(self.queue1) // 2 + len(self.queue1) % 2])
        if len(self.queue1) + len(self.queue2) % 2 == 0:
            self.queue1.append(num)
        else:
            self.queue2.appendleft(num)
        self.queue1 = self.queue1 + self.queue2


    def pushPrince(self, num):
        self.queue1.appendleft(num)
        self.prince = True

    def pop(self):
        if self.prince:
            self.prince = False
            return self.queue1.popleft()
        return self.queue1.popleft()

queue = Queue()

for _ in range(int(input())):
    line = input().strip().split()
    if line[0] == "+":
        queue.push(line[1])
        continue
    elif line[0] == "*":
        queue.pushNoble(line[1])
        continue
    elif line[0] == "!":
        queue.pushPrince(line[1])
        continue
    elif line[0] == "-":
        print(queue.pop())
        continue

