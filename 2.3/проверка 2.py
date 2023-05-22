import math

v_o, v_s = map(int, input().split())
s = int(input()) / 100

minTime = 123123123123
correct_point = 0
limit_right, limit_left = 0, 0
if 0.0 <= s < 0.3:
    limit_left, limit_right = 600000, 1000000
elif 0.3 <= s < 0.5:
    limit_left, limit_right = 400000, 800000
elif 0.5 <= s < 0.7:
    limit_left, limit_right = 100000, 500000
elif 0.7 <= s < 1.0:
    limit_left, limit_right = 0, 400000
for point in range(limit_left, limit_right):
    p = float('{:.6f}'.format(point / 1000000))

    # Формула функции
    # time = ((v_s * math.sqrt((1-s)**2 + p**2)) + (v_o * math.sqrt(s**2 + (1-p)**2))) / (v_s * v_o)

    # Формула производной функции, так мы находим мин значение времени
    # time = abs((p / (v_s * math.sqrt((1-s)**2 + p**2))) - ((1-p)/ (v_o * math.sqrt(s**2 + (1-p)**2))))

    if time < minTime:
        minTime = time
        correct_point = p
print('{:.6f}'.format(1 - correct_point))