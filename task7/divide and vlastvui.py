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
