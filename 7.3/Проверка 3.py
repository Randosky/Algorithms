n, W = map(int, input().split())

# создаем список блюд, где для каждого блюда храним его цену и калорийность
dishes = []
for i in range(n):
    p, c = map(int, input().split())
    dishes.append((p, c, i+1))

# сортируем список блюд по цене
dishes.sort()

# создаем массив для динамического программирования
dp = [[0] * (W+1) for _ in range(n+1)]

# заполняем массив dp
for i in range(1, n+1):
    for j in range(1, W+1):
        # если текущее блюдо можно выбрать, то выбираем его и добавляем его калории
        if dishes[i-1][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-dishes[i-1][0]] + dishes[i-1][1])
        # иначе не выбираем текущее блюдо
        else:
            dp[i][j] = dp[i-1][j]

# находим максимальную калорийность
max_calories = dp[n][W]

# находим выбранные блюда
selected_dishes = []
j = W
for i in range(n, 0, -1):
    if dp[i][j] != dp[i-1][j]:
        selected_dishes.append(dishes[i-1][2])
        j -= dishes[i-1][0]

# выводим результат
print(len(selected_dishes), max_calories)
print(*sorted(selected_dishes))
