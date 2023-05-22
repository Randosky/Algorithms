import random

print("1 1 15")
myarray1 = sorted([random.randint(0, 100) for _ in range(15)])
myarray2 = sorted([random.randint(0, 100) for _ in range(15)])

a = list(map(str, myarray1))
b = list(map(str, myarray2))
c = reversed(b)
print(" ".join(a))
print(" ".join(c))
print("1")
print("0 0")