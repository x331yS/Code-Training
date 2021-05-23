#include "action.h"
#include "main.h"

int getLinesAmount() {
    int *counter = malloc(sizeof(int));
    *counter = 0;
    FILE *fp;
    char c;
    fp = fopen(CONTACT, "r");
    if (fp == NULL) {
        printf("/===== Could not open file %s =====/", CONTACT);
        return 0;
    }
    for (c = getc(fp); c != EOF; c = getc(fp))
        if (c == '\n')
            *counter = *counter + 1;
    fclose(fp);
    return *counter;
}

char *toLowerCase(char *str) {
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] >= 65 && str[i] <= 90)
            str[i] += 32;
    }
    return str;
}

void exitingMenu() {
    int exitChoice;
    printf("\n\n/=== What would you like to do now ? ===/\n/===     1. Back to menu             ===/\n/===     2. Exit                     ===/\n\n/===== Your choice: ");
    scanf("%d", &exitChoice);
    if (exitChoice == 1) {
        menu();
    }
    if (exitChoice == 2) {
        printf("/=====  Exiting...  =====/\n");
        exit(1);
    } else {
        printf("\n/===== Invalid choice, retry pls ... =====/\n");
        exitingMenu();
    }
}