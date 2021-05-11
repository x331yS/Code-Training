#include <stdio.h>
#include <string.h>

int it_int(int a, int b) {
    return a == b;
}

//! strlen : longueur d’une chaîne
int mystrlen(const char *str) {
    int count = 0;
    while (str[count] != 0)
        count++;
    return count;
}

//! strcpy : copie d’une chaîne
void mystrcpy(const char *inputStr, char *outputStr) {
    int i = 0;
    while (inputStr[i] != '\0') {
        outputStr[i] = inputStr[i];
        i++;
    }
};


//! strcat : concaténation de chaînes
char *mystrcat(char *str1, const char *str2) {
    int index = mystrlen(str1),
            counter = 0;

    while (str2[counter] != '\0') {
        str1[index] = str2[counter];
        index++;
        counter++;
    }
    return str1;
}



//! strcmp : comparaisons de chaînes
int mystrcmp(const char *str1, const char *str2) {
    if (mystrlen(str1) != mystrlen(str2))
        return 1;
    int len = mystrlen(str1);
    for (int i = 0; i < len; i++) {
        if (str1[i] != str2[i])
            return 1;
    }
    return 0;
}

//! strchr : rechercher un caractére dans une chaîne
char *mystrchr(const char *p, int ch) {
    char *res = (char *) p;
    int i = 0;
    for (; res[i] != (char) ch; i++) {
        if (res[i] == '\0')
            return NULL;
    }
    return (res + i);
}

//! strstr : recherche une chaîne dans une autre
char *mystrstr(const char *str1, const char *str2) {
    char *p1 = (char *) str1, *p2 = (char *) str2, *p3;
    int j = 0;
    for (int i = 0; i < strlen(str1); i++) {
        if (*p1 == *p2) {
            p3 = p1;
            for (j = 0; j < strlen(str2); j++) {
                if (*p3 == *p2) {
                    p3++;
                    p2++;
                } else
                    break;
            }
            p2 = (char *) str2;
            if (j == strlen(str2)) {
                return (p1 + i - mystrlen(str2));
            }
        }
        p1++;
    }
    return NULL;
}

int main() {

    char str1[] = "Strings",
            str4[1000] = {0},
            str5[1000] = {0},
            str6[1000] = "Con",
            str7[1000] = "Cat",
            str8[1000] = "Con",
            str9[1000] = "Cat";

    //! Test My strlen
    printf("Test 1(strlen): %d -> %d\n", it_int(mystrlen(str1), strlen(str1)), mystrlen(str1));

    //! Test My strcpy
    mystrcpy(str1, str4);
    strcpy(str5, str1);
    printf("Test 2(strcpy): %d -> %s\n", !strcmp(str4, str5), str4);

    //! Test My strcat
    strcat(str6, str7);
    mystrcat(str8, str9);
    printf("Test 3(strcat): %d -> %s\n", !strcmp(str6, str8), str6);

    //! Test My strcmp
    printf("Test 4(strcmp): %d -> %d\n", it_int(strcmp(str6, str8), mystrcmp(str6, str8)), mystrcmp(str6, str8));

    //! Test My strchr
    const char stri[] = "https://www.github/x33lyS.com";
    const char ch = '.';
    char *myret = mystrchr(stri, ch);
    char *ret = strchr(stri, ch);
    printf("Test 5(strchr): %d -> %s\n", !strcmp(ret, myret), myret);

    //! Test My strstr
    const char haystack[20] = "TestSdStringTest";
    const char needle[10] = "String";
    char *ret2 = strstr(haystack, needle);
    char *myret2 = mystrstr(haystack, needle);
    printf("Test 6(strstr): %d -> %s\n", !strcmp(ret2, myret2), myret2);
    return 0;
}