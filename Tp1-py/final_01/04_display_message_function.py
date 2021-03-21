#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display multiple messages with defined variables
#               by FOR and WHILE.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
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
#
# Author:       DESTOMBES Matthieu
#
# Date:         2021.02.08
# ##############################################################################

# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

# First function
def first_part():
    # Variable creation
    my_first_name = "Matthieu"
    my_last_name = "DESTOMBES"
    my_occurrence = 5

    # Display message one time
    print("Hello world (PART 1)!")

    # For loop with range 10
    for occurrence in range(my_occurrence):
        # Display message
        print(
            "({0}): My name is ‘{1} {2}’".format(
                occurrence,
                my_first_name,
                my_last_name
            )
        )


# Second function
def second_part():
    # Variable creation
    my_first_name = "Matthieu"
    my_last_name = "DESTOMBES"
    my_occurrence = 5
    current_occurrence = 0

    # Display message one time
    print("Hello world (PART 2)!")

    # While start to 0 until occurrence is lower than 5
    while current_occurrence < my_occurrence:
        # Display message
        print(
            "({0}): My name is ‘{1} {2}’".format(
                current_occurrence,
                my_first_name,
                my_last_name
            )
        )

        current_occurrence += 1


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':
    # Variable creation
    my_main_loop = 10

    for main_occurrence in range(my_main_loop):

        if main_occurrence < 5:

            first_part()

        else:

            second_part()
