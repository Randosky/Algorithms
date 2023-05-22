class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

answers = []
start = None
end = None
size = 0

while True:
    cmd = input()
    if cmd.startswith("push"):
        tmp = Node(int(cmd.split()[1]))
        if end is None:
            start = tmp
            end = tmp
        tmp.next = None
        tmp.prev = end
        end.next = tmp
        end = tmp
        size += 1
        print("ok")
        continue

    elif cmd == "pop":
        tmp = start
        v_prev = start.prev
        v_next = start.next
        if v_next is not None:
            v_next.prev = v_prev

        start.prev = None
        start.next = None
        start = v_next
        size -= 1
        print(tmp.value)
        continue

    elif cmd == "front":
        print(start.value)
        continue

    elif cmd == "size":
        print(size)
        continue

    elif cmd == "view":
        answer = []
        if start == end and start is None:
            print("Очередь пуста")
            continue
        tmp = start
        answer.append(tmp.value)
        while tmp != end:
            tmp = tmp.next
            answer.append(tmp.value)
        print(", ".join(map(str, answer)))
        continue

    elif cmd == "clear":
        start = None
        end = None
        print("ok")
        continue

    elif cmd == "exit":
        print("bye")
        break

# print(*answers, sep="\n")



