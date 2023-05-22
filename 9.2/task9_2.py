from collections import Counter

class Node:
    def __init__(self, char, freq, zero, one):
        self.char = char
        self.freq = freq
        self.zero = zero
        self.one = one

def huffman(f):
    nodes = [Node(char, freq, None, None) for char, freq in f.items()]

    while len(nodes) > 1:
        node1 = min(nodes, key=lambda node: node.freq)
        nodes.remove(node1)
        node2 = min(nodes, key=lambda node: node.freq)
        nodes.remove(node2)

        new_node = Node(freq=node1.freq + node2.freq, char=None, zero=node1, one=node2)
        nodes.append(new_node)

    return nodes[0]


def assign_code(node, code, codes=None):
    if codes is None:
        codes = {}
    if node.char is not None:
        codes[node.char] = code
    else:
        assign_code(node.zero, code + '0', codes)
        assign_code(node.one, code + '1', codes)

    return codes

message = input()
if len(message) == 1:
    print(1)
else:
    frequencies = Counter(message)
    encoded_msg = assign_code(huffman(frequencies), '')
    print(len("".join(encoded_msg[char] for char in message)))