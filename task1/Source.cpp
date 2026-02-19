#include <iostream>
#include <queue>
#include <chrono>

using namespace std;
using namespace chrono;

int main() {
    int N;
    cout << "Сколько элементов добавить? ";
    cin >> N;

    queue<int> q;
    auto start = high_resolution_clock::now();
    for (int i = 0; i < N; i++) {
        q.push(i);
    }
    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);
    cout << "Время: " << duration.count() << " микросекунд" << endl;

    return 0;
}           


