import matplotlib.pyplot as plt

sizes = [10000, 25000, 50000, 75000, 100000, 150000]

times_quicksort = [0.0021795, 0.0064099, 0.0141533, 0.0196712, 0.0271559, 0.0443151]
times_2threads = [0.0020294, 0.0053852, 0.0136737, 0.0104846, 0.0271646, 0.031747]
times_4threads = [0.0017516, 0.0037924, 0.0098066, 0.008741, 0.0177516, 0.0241165]
times_8threads = [0.0017203, 0.0027756, 0.0096826, 0.0076124, 0.012949, 0.016937]

speedup_2 = [1.07396, 1.19028, 1.03507, 1.8762, 0.99968, 1.39588]
speedup_4 = [1.24429, 1.6902, 1.44324, 2.25045, 1.52977, 1.83754]
speedup_8 = [1.26693, 2.30937, 1.46173, 2.5841, 2.09714, 2.61647]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(sizes, times_quicksort, 'o-', label='quick sort')
plt.plot(sizes, times_2threads, 's-', label='2 threads')
plt.plot(sizes, times_4threads, '^-', label='4 threads')
plt.plot(sizes, times_8threads, 'd-', label='8 threads')
plt.xlabel('Размер массива')
plt.ylabel('Время (сек)')
plt.title('Время выполнения')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(sizes, speedup_2, 's-', label='2 threads')
plt.plot(sizes, speedup_4, '^-', label='4 threads')
plt.plot(sizes, speedup_8, 'd-', label='8 threads')
plt.xlabel('Размер массива')
plt.ylabel('Speedup')
plt.title('Коэффициент ускорения')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
