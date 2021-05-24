#include "action.h"

int addContact(char *firstName, char *lastName, int age) {
    FILE *file = fopen(CONTACT, "a+");
    Contact contact = {
            firstName,
            lastName,
            age
    };
    if (file == NULL) {
        fclose(file);
        return 1;
    }
    fprintf(
            file,
            "%s %s %d\n",
            contact.firstname,
            contact.lastname,
            contact.age
    );
    fclose(file);
    printf("\n/===== New contact create : %s %s =====/", contact.firstname, contact.lastname);
    return 0;
}

void listContacts() {
    FILE *file = NULL;
    file = fopen(CONTACT, "r+");
    int i;
    if (file != NULL) {

        int age = 0;
        char *firstname = malloc(sizeof(char *) * 100);
        char *lastname = malloc(sizeof(char *) * 100);
        printf("\n\n/=============    ============/\n\n\n");
        printf("/===== Contact List =====/\n");
        for (i = 0; i < countBackN(); i++) {
            fscanf(file, "%s %s %d", firstname, lastname, &age);
            printf("%d) %s %s - %d\n", i + 1, firstname, lastname, age);
        }
    }
    printf("There is %d contact(s)", i);
    printf("\n\n/=============    ============/\n");
    fclose(file);
}

void searchContacts(char wordS[100]) {
    int bool = 0;
    FILE *file;
    char word[100];
    file = fopen(CONTACT, "r");
    int i = 0;
    if (!file)
        printf("\n/=====Cant open file: %s =====/\n", CONTACT);
    toLowerCase(wordS);
    printf("\n");
    while (fgets(word, 100, file) != NULL) {
        ++i;
        toLowerCase(word);
        if (strstr(word, wordS) != NULL) {
            printf("/==== Contact found! ====/ \n %d) %s", i, word);
            bool = 1;
        }
    }
    if (bool == 0) {
        printf("/==== No Contact found! ====/");
    }
    fclose(file);
}