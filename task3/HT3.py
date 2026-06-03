import matplotlib.pyplot as plt
import random
import time
#quick sort
def quick_sort(arr, low, high):
    if low < high:
        index = partition(arr, low, high)
        quick_sort(arr, low, index - 1)
        quick_sort(arr, index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


arr = [7,6,523,234,45]
quick_sort(arr, 0, len(arr)-1)
print(arr)

#Shell sort
def shell_sort(arr):
    n = len(arr)
    step = n // 2

    while step > 0:
        for i in range(step, n):
            temp = arr[i]
            j = i
            while j >= step and arr[j - step] > temp:
                arr[j] = arr[j - step]
                j -= step
            arr[j] = temp
        step //= 2

arr = [1,5,77,4,2,1]
shell_sort(arr)
print(arr)

#comb sort
def comb_sort(arr):
    n = len(arr)
    step = n - 1

    while step > 1:
        step = int(step // 1.3)
        i = 0
        while i + step < n:
            if arr[i] > arr[i + step]:
                arr[i], arr[i + step] = arr[i + step], arr[i]
            i += 1

arr = [4,7,4,2,6,8]
comb_sort(arr)
print(arr)

sizes = list(range(10000, 100001, 10000))
time_quick = []
time_shell = []
time_comb = []

for n in sizes:
    print(f"Тестирование при n = {n} ...")
    arr = [random.randint(0, n) for _ in range(n)]

    arr_quick = arr
    t0 = time.perf_counter()
    quick_sort(arr_quick, 0, len(arr_quick) - 1)
    t1 = time.perf_counter()
    time_quick.append(1000*(t1 - t0))

    arr_shell = arr
    t0 = time.perf_counter()
    shell_sort(arr_shell)
    t1 = time.perf_counter()
    time_shell.append(1000*(t1 - t0))

    arr_comb = arr
    t0 = time.perf_counter()
    comb_sort(arr_comb)
    t1 = time.perf_counter()
    time_comb.append(1000*(t1 - t0))

plt.figure(figsize=(10, 6))
plt.plot(sizes, time_quick, marker='o', label='Quick sort')
plt.plot(sizes, time_shell, marker='s', label='Shell sort')
plt.plot(sizes, time_comb, marker='^', label='Comb sort')

print(time_quick, time_comb, time_shell, sep = '\n')

plt.title('Скорости работы алгоритмов')
plt.xlabel('Размер массива')
plt.ylabel('Время выполнения, mс')
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.show()
