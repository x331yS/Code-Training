#include <stdio.h>
#include <math.h>

struct polygon_6 {
    int coord1[2];
    int coord2[2];
    int coord3[2];
    int coord4[2];
    int coord5[2];
    int coord6[2];
};

double calcP6(struct polygon_6 polygone) {
    double result = 0;
    int
            x[6] = {polygone.coord1[0], polygone.coord2[0], polygone.coord3[0], polygone.coord4[0], polygone.coord5[0], polygone.coord6[0]},
            y[6] = {polygone.coord1[1], polygone.coord2[1], polygone.coord3[1], polygone.coord4[1], polygone.coord5[1], polygone.coord6[1]},
            j;
    for (int i = 0; i < 6; i++) {
        j = i + 1;
        if (j == 6)
            j = 0;
        result += sqrt(pow(x[j] - x[i], 2) + pow(y[j] - y[i], 2));
    }
    return result;
}

//int main() {
//    struct polygon_6 mypolygon = {
//            {2,  0},
//            {6,  0},
//            {10, -2},
//            {8,  -6},
//            {2,  -8},
//            {0,  -4}
//    };
//    double result = calcP6(mypolygon);
//    printf("The Perimeter is -> %.2f\n", result);
//    return 0;
//}