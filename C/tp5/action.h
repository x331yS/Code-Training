#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "support.h"

#define CONTACT "../contact.txt"

typedef struct contact {
    char *firstname;
    char *lastname;
    int age;
} Contact;

int addContact(char *firstName, char *lastName, int age);

void listContacts();

void searchContacts();