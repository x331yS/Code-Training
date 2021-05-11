#include <stdio.h>

int compte(const int *tab, int longueur_tab, int chiffre_a_compter) {
    int counter = 0;
    for (int i = 0; i < longueur_tab; i++) {
        if (chiffre_a_compter == tab[i])
            counter++;
    }
    return counter;
}

void multi(const int *tab_in, int longueur_tab, int *tab_out, int multiplicateur) {
    for (int i = 0; i < longueur_tab; i++) {
        tab_out[i] = tab_in[i] * multiplicateur;
    }
}

void calcul(const int *tab_in, int longueur_tab, int *tab_out, int operation, int valeur) {
    for (int i = 0; i < longueur_tab; i++) {
        switch (operation) {
            case 0:
                tab_out[i] = tab_in[i] + valeur;
                break;
            case 1:
                tab_out[i] = tab_in[i] - valeur;
                break;
            case 2:
                tab_out[i] = tab_in[i] * valeur;
                break;
            case 3:
                tab_out[i] = tab_in[i] / valeur;
                break;
            default:
                printf("Operation invalide %d\n", operation);
        }
    }
}

int main() {
    int tableau[9] = {1, 2, 3, 4, 1, 2, 3, 4, 5};
    int tableau_multi[9];
    int tableau_action[9];

    //* vars
    int num = 3,
            tabSize = 9,
            multNum = 3,
    operation = 3;

    //* count of num
    int count_of_num = compte(tableau, tabSize, num);
    printf("Count of %d: %d\n\n", num, count_of_num);

    //* multi
    multi(tableau, tabSize, tableau_multi, multNum);
    for (int i = 0; i < tabSize; i++) {
        printf("%d * %d -> %d\n", tableau[i], multNum, tableau_multi[i]);
    }
    //*Action
    calcul(tableau, tabSize, tableau_action, operation, num);
    printf("\n");
    char operation_char;
    switch (operation) {
        case 0:
            operation_char = '+';
            break;
        case 1:
            operation_char = '-';
            break;
        case 2:
            operation_char = '*';
            break;
        case 3:
            operation_char = '/';
            break;
    }
    for (int i = 0; i < tabSize; i++) {
        printf("%d %c %d -> %d\n", tableau[i], operation_char, num, tableau_action[i]);
    }
    return 0;
}