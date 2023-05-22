class PriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, i, k):
        self.queue.append((k, i))
        self.queue.sort(reverse=True)
        return "ok"

    def popTop(self):
        if not self.queue:
            return "-1"
        else:
            k, i = self.queue.pop(0)
            return i

    def pop_k(self, k):
        for i in range(len(self.queue)):
            if self.queue[i][0] == k:
                _, j = self.queue.pop(i)
                return j
        return "-1"

    def size(self):
        return len(self.queue)

    def popAll(self, k):
        removed = []
        for i in range(len(self.queue) - 1, -1, -1):
            if self.queue[i][0] == k:
                _, j = self.queue.pop(i)
                removed.append(j)
        if removed:
            return " ".join(removed)
        else:
            return "-1"

    def clear(self):
        self.queue.clear()
        return "ok"


queue = PriorityQueue()
answers = []

while True:
    cmd = input().strip().split()
    if cmd[0] == "push":
        answers.append(queue.push(cmd[1], cmd[2]))
    elif cmd[0] == "pop":
        if cmd[1] == "top":
            answers.append(queue.popTop())
        else:
            answers.append(queue.pop_k(cmd[1]))
    elif cmd[0] == "popall":
        answers.append(queue.popAll(cmd[1]))
    elif cmd[0] == "size":
        answers.append(queue.size())
    elif cmd[0] == "clear":
        answers.append(queue.clear())
    elif cmd[0] == "exit":
        answers.append("bye")
        break

print(*answers, sep="\n")