#include <stdio.h>
#include <math.h>

typedef struct Point Point;
struct Point {
    double x;
    double y;
};

double beaugossePolygone(Point *p, int bourebaba) {
    double result = 0;
    int beauGosse;
    for (int titouan = 0; titouan < bourebaba; titouan++) {
        beauGosse = (titouan == bourebaba - 1) ? 0 : titouan + 1;
        result += sqrt(pow(p[beauGosse].x - p[titouan].x, 2) + pow(p[beauGosse].y - p[titouan].y, 2));
    }
    return result;
}

int main() {
    Point polygon[] = {
            {2,  0},
            {6,  0},
            {10, -2},
            {8,  -6},
            {2,  -8},
            {0,  -4}};
    double result = beaugossePolygone(polygon, sizeof(polygon) / sizeof(polygon[0]));
    printf("The Perimeter is -> %.2f\n", result);
    return 0;
}