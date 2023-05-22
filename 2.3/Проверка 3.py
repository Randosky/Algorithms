import math

v_o, v_s = map(int, input().split())
s = int(input()) / 100


# Формула функции
# time = ((v_s * math.sqrt((1-s)**2 + x**2)) + (v_o * math.sqrt(s**2 + (1-x)**2))) / (v_s * v_o)

# Формула производной функции, так мы находим мин значение времени
# time = (x / (v_s * math.sqrt((1-s)**2 + x**2))) - ((1-x)/ (v_o * math.sqrt(s**2 + (1-x)**2)))

def f(x):
    return (x / (v_s * math.sqrt((1-s)**2 + x**2))) - ((1-x)/ (v_o * math.sqrt(s**2 + (1-x)**2)))


# Данное решение для формулы производной
def dichotomy(left, right):
    while abs(f(right) - f(left)) > 0.0000001:
        middle = (right + left) / 2
        if f(middle) * f(left) < 0:
            right = middle
        else:
            left = middle
    return (right + left) / 2

print('{0:.6f}'.format(1 - round(dichotomy(0.000001, 0.999999), 6)))
