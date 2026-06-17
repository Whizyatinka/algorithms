#backtracking
print("Задача поиска с возвратом(5):\n")
n, k = map(int, input("Введите количество вершин и цветов: ").split())

g = []

for i in range(n):
    s = input(f"Введите {i+1} из {n} строку матрицы смежности: ").strip()
    g.append(list(map(int, s)))

clr = [0] * n


def ok(v, c):
    for i in range(n):
        if g[v][i] == 1 and clr[i] == c:
            return False
    return True


def bt(v):
    if v == n:
        return True

    for c in range(1, k + 1):
        if ok(v, c):
            clr[v] = c

            if bt(v + 1):
                return True

            clr[v] = 0

    return False


if bt(0):
    print("YES")
    print(*clr)
else:
    print("NO")