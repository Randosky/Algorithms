class Node:
    def __init__(self, v, p):
        self.v = v
        self.p = p
        self.l = None
        self.r = None


def from_array(nums):
    if not nums:
        return None

    m = (len(nums)) // 2 - 1 if len(nums) % 2 == 0 else (len(nums)) // 2

    t = Node(nums[m], None)
    t.l = from_array(nums[:m])
    t.r = from_array(nums[m + 1:])

    if t.l is not None:
        t.l.p = t
    if t.r is not None:
        t.r.p = t

    return t


def next_node(v):
    n = find(root, v)
    if n is None:
        return None
    if n.r is not None:
        nxt = n.r
        while nxt.l is not None:
            nxt = nxt.l
        return nxt.v
    nxt = n
    while (nxt.p is not None) and (nxt.p.r == nxt):
        nxt = nxt.p
    if nxt.p is None:
        return None
    return nxt.p.v


def add(n, v):
    if n is None:
        return
    if v < n.v:
        if n.l is None:
            n.l = Node(v, n)
            return
        add(n.l, v)
    else:
        if n.r is None:
            n.r = Node(v, n)
            return
        add(n.r, v)


def find(n, v):
    if n is None:
        return None
    if n.v == v:
        return n
    if n.v > v:
        return find(n.l, v)
    else:
        return find(n.r, v)


def delete(n, r):
    if n is None:
        return

    if (n.l is None) or (n.r is None):
        child = None
        if n.l is not None:
            child = n.l
        else:
            child = n.r
        if n == r:
            r = child
            if child is not None:
                child.p = None
        if n.p.l == n:
            n.p.l = child
            if child is not None:
                child.p = n.p
        else:
            n.p.r = child
            if child is not None:
                child.p = n.p
    else:
        nxt = n.r
        while nxt.l is not None:
            nxt = nxt.l
        n.v = nxt.v
        delete(nxt, r)


def print_tree(n, row=""):
    if not n:
        return

    if n == root:
        parent_left_right = [None, None]
    else:
        parent_left_right = [n.p.l, n.p.r]

    if parent_left_right[0] is not None and parent_left_right[1] is not None:
        last = False if parent_left_right[0] == n else True
    else:
        last = True

    if n == root:
        print(n.v)
    else:
        print(row + ("└───" if last else "├───") + str(n.v))

    if n.l:
        print_tree(n.l, row + ("" if n == root else ("    " if last else "│   ")))
    if n.r:
        print_tree(n.r, row + ("" if n == root else ("    " if last else "│   ")))


if __name__ == "__main__":
    array = list(map(int, input().split()))
    root = from_array(array)

    while True:
        message = input().strip().split()
        if message[0] == "print":
            print_tree(root)
        elif message[0] == "delete":
            if root is None:
                continue
            node = find(root, int(message[1]))
            if node is None:
                continue
            delete(node, root)
            print("Ok")
        elif message[0] == "find":
            node = find(root, int(message[1]))
            print("Число нашлось") if node is not None else print("Число не нашлось")
        elif message[0] == "add":
            if root is None:
                root = Node(int(message[1]), None)
                continue

            for i in range(1, len(message)):
                add(root, int(message[i]))
            print("Ok")
        elif message[0] == "next":
            value = next_node(int(message[1]))
            print("Следующего числа нет") if value is None else print(value)
        elif message[0] == "exit":
            break
