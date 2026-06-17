#ДП
print("Задача ДП(4):\n")
x = int(input("Введите сумму: "))
k = int(input("Введите число номиналов: "))

coins = list(map(int, input("Введите номиналы через пробел: ").split()))

INF = 10 ** 9

dp = [INF] * (x + 1)
dp[0] = 0

for i in range(1, x + 1):
    for c in coins:
        if i - c >= 0:
            dp[i] = min(dp[i], dp[i - c] + 1)

if dp[x] == INF:
    print(-1)
else:
    print(dp[x])
