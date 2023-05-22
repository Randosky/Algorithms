class Queue:
    a = []
    b = []

    def push(self, i, k):
        self.a.append((i, k))

    def pop(self, k):
        while len(self.a):
            self.b.append(self.a.pop())
        for i in range(len(self.b)):
            if self.b[i][1] == k:
                return self.b.pop()[0]
        return -1

    def popTop(self):
        if len(self.b) == 0 and len(self.a) == 0:
            return -1

        while len(self.a):
            self.b.append(self.a.pop())

        ind = 0
        maximum = self.b[0]
        for i in range(len(self.b)):
            if self.b[i][1] >= maximum[1]:
                maximum = self.b[i]
                ind = i
        self.b.pop(ind)
        return maximum[0]

    def size(self):
        return len(self.a) + len(self.b)

    def popAll(self, k):
        res = []
        while len(self.a):
            self.b.append(self.a.pop())

        for i in range(len(self.b)):
            if k in self.b[0]:
                res.append(str(self.b.pop()[0]))
        return " ".join(res)

    def clear(self):
        self.a.clear()
        self.b.clear()

queue = Queue()
answers = []

while True:
    cmd = input().strip().split()
    if cmd[0] == "push":
        queue.push(int(cmd[1]), int(cmd[2]))
        answers.append("ok")
    elif cmd[0] == "pop":
        if cmd[1] == "top":
            answers.append(queue.popTop())
        else:
            answers.append(queue.pop(int(cmd[1])))
    elif cmd[0] == "popall":
        answers.append(queue.popAll(int(cmd[1])))
    elif cmd[0] == "size":
        answers.append(queue.size())
    elif cmd[0] == "clear":
        queue.clear()
        answers.append("ok")
    elif cmd[0] == "exit":
        answers.append("bye")
        break

print(*answers, sep="\n")