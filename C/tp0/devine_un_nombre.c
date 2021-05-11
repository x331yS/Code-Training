#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    const int MAX = 100, MIN = 1;
    srand(time(NULL));
    int randomNumber = (rand() % (MAX - MIN + 1)) + MIN;
    int userInput = -1;
    do
    {
        printf("Type in your number: ");
        scanf("%d", &userInput);
        if (userInput > randomNumber)
        {
            printf("Your number is bigger than that the computer has generated\n");
        }
        else if (userInput < randomNumber)
        {
            printf("Your number is smaller than that the computer has generated\n");
        }
        else
        {
            printf("Congratulations, %d is the correct number!\n", userInput);
            break;
        }
    } while (1);
    return 0;
}