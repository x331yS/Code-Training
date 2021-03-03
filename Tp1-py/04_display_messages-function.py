# Deposit:      - Dans un fichier python nommé "04_display_messages_function.py"
#               - Créer une variable "my_first_name" avec votre prénom
#               - Créer une variable "my_last_name" avec votre nom de famille
#               - Créer une variable "my_occurrence" avec le nombre 5
#               - Créer une variable "current_occurrence" avec le nombre 0
#               - Créer une variable "my_main_loop" avec le nombre 10
#               - Créer une fonction "first_part"
#                 qui réalise les actions suivantes
#                 - Afficher le message "Hello world (PART 1)!"
#                 - Avec structure de contrôle itérative "for"
#                   - Afficher le message "([occurrence]): My name is ‘[prénom] [nom de famille]’"
#                     en utilisant les variables précédentes
#                   - "occurrence" correspond à la position dans
#                     la structure de contrôle itérative
#                   - Utiliser "my_occurrence" pour afficher le message 5 fois
#               - Créer une fonction "second_part"
#                 qui réalise les actions suivantes
#                 - Afficher le message "Hello world (PART 2)!"
#                 - Avec structure de contrôle itérative "while"
#                   - Afficher le message "([current_occurrence]): My name is ‘[prénom] [nom de famille]’"
#                     en utilisant les variable précédente
#                   - Utiliser l’incrémentation et les variables
#                     "current_occurrence" et "my_occurrence"
#                     pour afficher le message 5 fois
#               - Avec structure de contrôle itérative "for"
#                 - Utiliser "my_main_loop" pour boucler 10 fois
#                 - Avec la structure de contrôle séquentiel "if"
#                   - Pour les 5 premiers passages appeler
#                     la fonction "first_part"
#                   - Pour les 5 derniers passages appeler
#                     la fonction "second_part"

my_first_name = "Florian"
my_last_name = "Lejosne"
my_occurrence = 5
current_occurrence = 0
my_main_loop = 10


def first_part():
    global current_occurrence
    current_occurrence = 0
    print('Hello world (PART 1)!')
    for i in range(my_occurrence):
        print(current_occurrence, ': My name is {0} {1}', format(my_first_name), format(my_last_name))
        current_occurrence += 1


def second_part():
    global current_occurrence
    current_occurrence = 0
    print('Hello world (PART 2)!')
    while current_occurrence <= my_occurrence:
        print(current_occurrence, ': My name is', my_first_name, my_last_name)
        current_occurrence += 1


for my_main_loop in range(my_main_loop):
    if my_main_loop < 5:
        first_part()
    else:
        second_part()
