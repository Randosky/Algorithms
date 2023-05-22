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


def find_min(n):
    if not n:
        return -1

    if n.l is not None:
        return find_min(n.l)
    else:
        return n.v


def find_max(n):
    if not n:
        return -1

    if n.r is not None:
        return find_max(n.r)
    else:
        return n.v


def print_tree(n):
    if not n:
        return

    print_tree(n.l)
    print(n.v, end=" ")
    print_tree(n.r)


if __name__ == "__main__":
    array = list(map(int, input().split()))
    root = from_array(array)

    while True:
        message = input().strip().split()
        if message[0] == "list":
            print_tree(root)
            print()
        elif message[0] == "delete":
            if root is None:
                print("Ok")
                continue
            node = find(root, int(message[1]))
            if node is None:
                print("Ok")
                continue
            delete(node, root)
            print("Ok")
        elif message[0] == "find":
            node = find(root, int(message[1]))
            print("Такая банка есть") if node is not None else print("Такой банки нет")
        elif message[0] == "add":
            if root is None:
                root = Node(int(message[1]), None)
                print("Ok")
                continue
            add(root, int(message[1]))
            print("Ok")
        elif message[0] == "min":
            value = find_min(root)
            print(value) if value != -1 else print("Склад пуст")
        elif message[0] == "max":
            value = find_max(root)
            print(value) if value != -1 else print("Склад пуст")
        elif message[0] == "exit":
            break
