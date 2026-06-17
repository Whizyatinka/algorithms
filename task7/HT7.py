#Деревья
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def solve_tree(root):
    ans = [-10 ** 9]
    def dfs(v):
        if not v:
            return 0
        l = max(0, dfs(v.left))
        r = max(0, dfs(v.right))
        ans[0] = max(ans[0], l + r + v.val)
        return max(l, r) + v.val
    dfs(root)
    return ans[0]

def input_tree():
    print("Задача Деревья(6):\n")
    root_num = 0
    n = int(input("Введите количество вершин: "))
    nodes = {}
    print("Введите данные о вершинах дерева, если потомка нет - пишите None")
    print("Формат: номер, значение, левый потомок, правый")
    for i in range(n):
        s = input().split()
        num = int(s[0])
        if i == 0:
            root_num = num
        val = int(s[1])
        l = s[2]
        r = s[3]
        if num not in nodes:
            nodes[num] = Node(val)
        else:
            nodes[num].val = val
        if l != "None":
            l = int(l)
            if l not in nodes:
                nodes[l] = Node(0)
            nodes[num].left = nodes[l]
        if r != "None":
            r = int(r)
            if r not in nodes:
                nodes[r] = Node(0)
            nodes[num].right = nodes[r]
    return nodes[root_num]

print(solve_tree(input_tree()))

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

#Разделяй и властвуй
def find_mm(a, l, r):
    if l == r:
        return a[l], a[l]

    mid = (l + r) // 2

    mn1, mx1 = find_mm(a, l, mid)
    mn2, mx2 = find_mm(a, mid + 1, r)

    mn = min(mn1, mn2)
    mx = max(mx1, mx2)

    return mn, mx

print("Задача Разделяй и властвуй(1):\n")
nums = list(map(int, input("Введите список чисел, минимум и максимум которого вас интересует через пробел: ").split()))
# nums = [5, 7, 2, 4, 9, 6]

mn, mx = find_mm(nums, 0, len(nums) - 1)

print("Минимальный элемент:", mn)
print("Максимальный элемент:", mx)

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