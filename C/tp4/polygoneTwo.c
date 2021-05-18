#include <stdio.h>
#include <math.h>
struct six_polygon {
    int coord1[2];
    int coord2[2];
    int coord3[2];
    int coord4[2];
    int coord5[2];
    int coord6[2];
};


float polygoneOfSixOnly(struct six_polygon polygone) {
    float result = 0;
    result += sqrt(pow(polygone.coord2[1] - polygone.coord1[1], 2) + pow(polygone.coord2[0] - polygone.coord1[0], 2));
    result += sqrt(pow(polygone.coord3[1] - polygone.coord2[1], 2) + pow(polygone.coord3[0] - polygone.coord2[0], 2));
    result += sqrt(pow(polygone.coord4[1] - polygone.coord3[1], 2) + pow(polygone.coord4[0] - polygone.coord3[0], 2));
    result += sqrt(pow(polygone.coord5[1] - polygone.coord4[1], 2) + pow(polygone.coord5[0] - polygone.coord4[0], 2));
    result += sqrt(pow(polygone.coord6[1] - polygone.coord5[1], 2) + pow(polygone.coord6[0] - polygone.coord5[0], 2));
    result += sqrt(pow(polygone.coord1[1] - polygone.coord6[1], 2) + pow(polygone.coord1[0] - polygone.coord6[0], 2));
    return result;
}

//int main() {
//    struct six_polygon mypolygon = {
//            {2,  0},
//            {6,  0},
//            {10, -2},
//            {8,  -6},
//            {2,  -8},
//            {0,  -4}
//    };
//    double result = polygoneOfSixOnly(mypolygon);
//    printf("The Perimeter is -> %.2f\n", result);
//    return 0;
//}