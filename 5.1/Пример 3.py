from collections import deque

answers = []
queue = deque()

while True:
    cmd = input().strip()
    if cmd.startswith("push"):
        queue.append(cmd.split()[1])
        print("ok")
        continue

    elif cmd == "pop":
        print(queue.popleft())
        continue

    elif cmd == "front":
        tmp = queue.popleft()
        queue.appendleft(tmp)
        print(tmp)
        continue

    elif cmd == "size":
        print(len(queue))
        continue

    elif cmd == "view":
        answer = []
        for elem in queue:
            answer.append(elem)
        print(", ".join(map(str, answer)))
        continue

    elif cmd == "clear":
        queue.clear()
        print("ok")
        continue

    elif cmd == "exit":
        print("bye")
        break



