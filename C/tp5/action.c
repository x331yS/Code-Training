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
    return 0;
};

void listContacts() {
    FILE *file = NULL;
    file = fopen(CONTACT, "r+");
    if (file != NULL) {
        int i = 0;
        int age = 0;
        char *firstname = malloc(sizeof(char *) * 100);
        char *lastname = malloc(sizeof(char *) * 100);
        printf("\n\n/=============    ============/\n\n\n");
        printf("/===== Contact List =====/\n");
        for (int i = 0; i < getLinesAmount(); i++) {
            fscanf(file, "%s %s %d", firstname, lastname, &age);
            printf("%d) %s %s - %d\n", i + 1, firstname, lastname, age);
        }
        free(firstname);
        free(lastname);
    }
    printf("\n\n/=============    ============/\n");
    fclose(file);
};

void searchContacts() {
    int bool = 0;
    FILE *file;
    char word[100], wordS[100];
    file = fopen(CONTACT, "r");
    int i = 0;
    if (!file)
        printf("\n/=====Cant open file: %s =====/\n", CONTACT);

    printf("/===== Search for : ");
    scanf("%s", wordS);
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