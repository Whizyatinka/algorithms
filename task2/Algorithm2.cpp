#include <iostream>
#include <cstdlib>
#include <ctime>

double monte_carlo_area(int num_points = 100000) {
    int inside = 0;

    double x_min = 2.0, x_max = 7.0;
    double y_min = -43.0, y_max = 145.0;

    double rect_area = (x_max - x_min) * (y_max - y_min);

    for (int i = 0; i < num_points; ++i) {
        double x = x_min + ((double)rand() / RAND_MAX) * (x_max - x_min);
        double y = y_min + ((double)rand() / RAND_MAX) * (y_max - y_min);

        double lower = -x * x + 6;
        double upper = 3 * x * x - 2;

        if (y >= lower && y <= upper) {
            inside++;
        }
    }

    return (inside / (double)num_points) * rect_area;
}

int main() {
    setlocale(LC_ALL, "rus");
    srand(time(0));
    double area = monte_carlo_area();
    std::cout << "площадь области: " << area << std::endl;
    return 0;
}
