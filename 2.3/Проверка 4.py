import math

v_o, v_s = map(int, input().split())
s = int(input()) / 100

def half_method():
    eps = 1e-7
    left = 0.000001
    right = 0.999999
    middle = (left + right) / 2
    while abs(func(middle)) > eps:
        if ((func(left) > 0) and (func(middle) < 0)) or ((func(left) < 0) and (func(middle) > 0)):
            right = middle
        elif ((func(middle) > 0) and (func(right) < 0)) or ((func(middle) < 0) and (func(right) > 0)):
            left = middle
        middle = (left + right) / 2
    return middle

def func(x):
    return (x / (v_s * math.sqrt((1-s)**2 + x**2))) - ((1-x)/ (v_o * math.sqrt(s**2 + (1-x)**2)))

print('{0:.6f}'.format(1 - round(half_method(), 6)))
