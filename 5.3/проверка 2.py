class Node:
    def __init__(self, n, i):
        self.number = n
        self.index = i
        self.next = None
        self.prev = None


class Queue:
    length = 0

    def __init__(self):
        self.start = None
        self.end = None
        self.prince = -1
        self.knightsBeforePrince = 0

    def pushKnight(self, n):
        tmp = Node(n, self.length)
        if self.end is None:
            self.start = tmp
            self.end = tmp
            self.length += 1

            if self.prince == -1:
                self.knightsBeforePrince += 1

            return
        tmp.next = None
        self.end.next = tmp
        tmp.prev = self.end
        self.end = tmp
        self.length += 1

        if self.prince == -1:
            self.knightsBeforePrince += 1
        return

    def pushNobleman(self, n):
        tmp = self.start
        if tmp is None:
            self.pushKnight(n)
            return

        count = 0
        while tmp is not None:
            if self.length % 2 == 0:
                half = self.length // 2
            else:
                half = self.length // 2 + 1
            if half == count:
                self.addInHalf(tmp, n, half)
                self.length += 1

                if self.prince == -1:
                    self.knightsBeforePrince += 1

                return
            count += 1
            tmp = tmp.next


        return

    def addInHalf(self, node, value, index):
        tmp = Node(value, index)
        node_next = node.next
        if node_next is None:
            tmp.next = None
            node.next = tmp
            tmp.prev = node
            self.end = tmp
            return
        node_next.prev = tmp
        tmp.next = node_next
        node.next = tmp
        tmp.prev = node

    def pushPrince(self, n):
        self.prince = n
        self.length += 1
        return

    def pop(self):
        node = self.start
        v_next = node.next
        v_prev = node.prev

        if v_prev is not None:
            v_prev.next = v_next
        if v_next is not None:
            v_next.prev = v_prev

        node.prev = None
        node.next = None

        if node == self.start:
            self.start = v_next
        if node == self.end:
            self.end = v_prev

        return node.number


queue = Queue()
answers = []

for person in range(int(input())):
    cmd = input().strip().split()
    if cmd[0] == "+":
        queue.pushKnight(cmd[1])
    elif cmd[0] == "*":
        queue.pushNobleman(cmd[1])
    elif cmd[0] == "!":
        queue.pushPrince(cmd[1])
    elif cmd[0] == "-":
        answers.append(queue.pop())

print(*answers, sep="\n")
