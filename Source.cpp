#include <iostream>
#include <vector>
#include <thread>
#include <chrono>
#include <ctime>

using namespace std;

const int splitlength = 2000;

int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

void quicksort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int index = partition(arr, low, high);
        quicksort(arr, low, index - 1);
        quicksort(arr, index + 1, high);
    }
}

void quicksortParallel(vector<int>& arr, int low, int high, int num_threads) {
    if (low < high) {
        int index = partition(arr, low, high);
        if (num_threads > 1 && (high - low) > splitlength) {
            thread left_thread(quicksortParallel, ref(arr), low, index - 1, num_threads / 2);
            quicksortParallel(arr, index + 1, high, num_threads - num_threads / 2);
            left_thread.join();
        }
        else {
            quicksort(arr, low, index - 1);
            quicksort(arr, index + 1, high);
        }
    }
}

vector<int> generateArray(int size) {
    vector<int> arr(size);
    for (int i = 0; i < size; i++) {
        arr[i] = rand() % size;
    }
    return arr;
}

int main() {
    vector<int> sizes = { 10000, 25000, 50000, 75000, 100000, 150000 };
    vector<double> times_quicksort;
    vector<double> times_2threads;
    vector<double> times_4threads;
    vector<double> times_8threads;
    vector<double> speedup_2;
    vector<double> speedup_4;
    vector<double> speedup_8;
    for (int size : sizes) {
        vector<int> original = generateArray(size);

        // 1. Обычная быстрая сортировка
        vector<int> arr1 = original;
        auto start = chrono::high_resolution_clock::now();
        quicksort(arr1, 0, size - 1);
        auto end = chrono::high_resolution_clock::now();
        double time_quicksort = chrono::duration<double>(end - start).count();
        times_quicksort.push_back(time_quicksort);

        // 2. Параллельная с 2 потоками
        vector<int> arr2 = original;
        start = chrono::high_resolution_clock::now();
        quicksortParallel(arr2, 0, size - 1, 2);
        end = chrono::high_resolution_clock::now();
        double time_2t = chrono::duration<double>(end - start).count();
        times_2threads.push_back(time_2t);

        // 3. Параллельная с 4 потоками
        vector<int> arr4 = original;
        start = chrono::high_resolution_clock::now();
        quicksortParallel(arr4, 0, size - 1, 4);
        end = chrono::high_resolution_clock::now();
        double time_4t = chrono::duration<double>(end - start).count();
        times_4threads.push_back(time_4t);

        // 4. Параллельная с 8 потоками
        vector<int> arr8 = original;
        start = chrono::high_resolution_clock::now();
        quicksortParallel(arr8, 0, size - 1, 8);
        end = chrono::high_resolution_clock::now();
        double time_8t = chrono::duration<double>(end - start).count();
        times_8threads.push_back(time_8t);

        // Коэффициенты ускорения
        speedup_2.push_back(time_quicksort / time_2t);
        speedup_4.push_back(time_quicksort / time_4t);
        speedup_8.push_back(time_quicksort / time_8t);
    }

    setlocale(LC_ALL, "Russian");

    cout << "Размеры массивов: ";
    for (int size : sizes) {
        cout << size << " ";
    }
    cout << endl << endl;

    cout << "БС(сек) ";
    for (double t : times_quicksort) {
        cout << t << " ";
    }
    cout << endl;

    cout << "БС_П 2 потока (сек) ";
    for (double t : times_2threads) {
        cout << t << " ";
    }
    cout << endl;

    cout << "БС_П 4 потока (сек) ";
    for (double t : times_4threads) {
        cout << t << " ";
    }
    cout << endl;

    cout << "БС_П 8 потока (сек) ";
    for (double t : times_8threads) {
        cout << t << " ";
    }
    cout << endl << endl;

    cout << "Speedup 2 потока ";
    for (double s : speedup_2) {
        cout << s << " ";
    }
    cout << endl;

    cout << "Speedup 4 потока ";
    for (double s : speedup_4) {
        cout << s << " ";
    }
    cout << endl;

    cout << "Speedup 8 потоков ";
    for (double s : speedup_8) {
        cout << s << " ";
    }
    cout << endl;

    return 0;
}