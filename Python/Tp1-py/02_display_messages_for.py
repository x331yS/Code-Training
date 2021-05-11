# Deposit:      - Dans un fichier python nommé "02_display_messages_for.py"
#               - Créer une variable "my_first_name" avec votre prénom
#               - Créer une variable "my_last_name" avec votre nom de famille
#               - Créer une variable "my_occurrence" avec le nombre 10
#               - Afficher le message "Hello world (FOR)!"
#               - Avec la structure de contrôle itérative "for"
#                 - Afficher le message
#                   "([occurrence]): My name is ‘[prénom] [nom de famille]’"
#                   en utilisant les variables précédentes
#                 - "occurrence" correspond à la position dans
#                   la structure de contrôle itérative
#                 - Utiliser "my_occurrence" pour afficher le message 10 fois

my_first_name = "Florian"
my_last_name = "Lejosne"
my_occurence = 10

print('Hello World(FOR)!')

for occurrence in range(my_occurence):
    print("({0}): My name is ‘{1} {2}’".format(occurrence, my_first_name, my_last_name))
