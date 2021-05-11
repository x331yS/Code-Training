#include <stdio.h>
#include <math.h>

float areaRect(float x, float y) {
    return x * y;
}

float perimRect(float x, float y) {
    return (x + y) * 2;
}

float areaCircle(float r) {
    return r * r * M_PI;
}

float perimCircle(float r) {
    return 2 * r * M_PI;
}

float areaSquare(float side) {
    return side * side;
}

float perimSquare(float side) {
    return side * 4;
}

float calculate(int fig, int type) {
    float result, x, y, r, side;
    switch (fig) {
        case 1:
            printf("Type in the X value of a rectangle ");
            scanf("%f", &x);
            printf("Type in the Y value of a rectangle ");
            scanf("%f", &y);

            switch (type) {
                case 1:
                    result = areaRect(x, y);
                    break;
                case 2:
                    result = perimRect(x, y) /**/;
                    break;
            }
            break;
        case 2:
            printf("Type in the radius of a circle ");
            scanf("%f", &r);

            switch (type) {
                case 1:
                    result = areaCircle(r) /**/;
                    break;
                case 2:
                    result = perimCircle(r) /**/;
                    break;
            }
            break;
        case 3:
            printf("Type in the side of a square ");
            scanf("%f", &side);
            switch (type) {
                case 1:
                    result = areaSquare(side) /**/;
                    break;
                case 2:
                    result = perimSquare(side) /**/;
                    break;
            }
            break;
    }
    return result;
}

int menu_figure() {
    int choice;
    do {
        printf("Please select one figure from the list below:\n1. Rectangle\n2. Circle\n3. Square\n");
        scanf("%d", &choice);
    } while (choice < 1 || choice > 3);

    return choice;
}

int menu_type() {
    int choice = -1;
    do {
        printf("Please select what do you want to calculate:\n1. Area\n2. Perimeter\n");
        scanf("%d", &choice);
    } while (choice < 1 || choice > 2);

    return choice;
}

int main() {
    // * 1
    float rect_x, rect_y;
    printf("Type in the X value of a rectangle ");
    scanf("%f", &rect_x);
    printf("Type in the Y value of a rectangle ");
    scanf("%f", &rect_y);
    float rect_area = areaRect(rect_x, rect_y);
    printf("The area of a square with x=%.2f, y=%.2f is equal to %.2f\n", rect_x, rect_y, rect_area);

    // * 2
    float circle_r;
    printf("Type in the radius of a circle ");
    scanf("%f", &circle_r);
    float circle_area = areaCircle(circle_r);
    printf("The area of a cirlce with radius of %.2f is equal to %.2f\n", circle_r, circle_area);

    // * 3
    float square_side;
    printf("Type in the side of a square ");
    scanf("%f", &square_side);
    float square_area = areaSquare(square_side);
    printf("The area of a square with a side %.2f is equal to %.2f\n", square_side, square_area);

    // * 4
    int fig = menu_figure();
    int type = menu_type();

    float result = calculate(fig, type);

    printf("%.2f\n", result);

    return 0;
}