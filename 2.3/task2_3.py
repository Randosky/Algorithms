import math

v_o, v_s = map(int, input().split())
s = int(input()) / 100

# Формула функции
# time = ((v_s * math.sqrt((1-s)**2 + p**2)) + (v_o * math.sqrt(s**2 + (1-p)**2))) / (v_s * v_o)

# Формула производной функции, так мы находим мин значение времени
# time = abs((p / (v_s * math.sqrt((1-s)**2 + p**2))) - ((1-p)/ (v_o * math.sqrt(s**2 + (1-p)**2))))

def f(p):
    return (p / (v_s * math.sqrt((1-s)**2 + p**2))) - ((1-p)/ (v_o * math.sqrt(s**2 + (1-p)**2)))

# Данное решение для формулы производной
def bisection(left, right):
    while abs(f(right) - f(left)) > 0.0000001:
        middle = (right + left) / 2
        if f(middle) == 0 or abs(f(middle)) < 0.0000001:
            break
        elif f(middle) * f(left) < 0:
            right = middle
        else:
            left = middle
    return (right + left) / 2
a = 0.000001
b = 0.999999

print('{0:.6f}'.format(1 - round(bisection(a, b), 6)))