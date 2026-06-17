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



