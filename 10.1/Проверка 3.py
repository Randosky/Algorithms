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
        t.l.parent = t
    if t.r is not None:
        t.r.parent = t

    return t


def print_tree(n, row=""):
    if not n:
        return

    if n == root:
        parent_left_right = [None, None]
    else:
        parent_left_right = [n.parent.l, n.parent.r]

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

    print_tree(root)
