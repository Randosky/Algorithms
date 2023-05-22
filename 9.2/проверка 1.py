from collections import Counter

class Node:
    c: str
    w: int

    def __init__(self, c, w, zero, one):
        self.c = c
        self.w = w
        self.zero = zero
        self.one = one

def huffman_tree(f):
    arr = []
    for c, w in f.items():
        arr.append(Node(c, w, None, None))

    while len(arr) > 1:
        t1 = min(arr, key=lambda n: n.w)
        arr.remove(t1)
        t2 = min(arr, key=lambda n: n.w)
        arr.remove(t2)

        node = Node(None, t1.w + t2.w, t1, t2)
        arr.append(node)

    return arr[0]


def dfs(node, code, codes):
    if node.c is not None:
        codes[node.c] = code
    else:
        dfs(node.zero, code + '0', codes)
        dfs(node.one, code + '1', codes)

    return codes

if __name__ == "__main__":
    s = input()
    if len(s) == 1:
        print(1)
    else:
        freq = Counter(s)
        tree = huffman_tree(freq)
        e_s = dfs(tree, '', {})
        res_s = []
        for char in s:
            res_s.append(e_s[char])

        print(len("".join(res_s)))