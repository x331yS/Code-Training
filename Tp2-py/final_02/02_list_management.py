#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display messages with list content.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "02_list_management.py"
#               - Recopier le comportement du fichier précédent
#               - Créer une fonction "check_add_or_remove" qui réalise
#                 les actions suivantes
#                 - Prendre 2 arguments en entrée
#                   - "input_list", une liste...
#                   - "input_value", une valeur.
#                 - Retourner une variable de sortie
#                   - "input_list" la liste modifiée
#                 - Instruction de la fonction
#                   - Avec la "structure de contrôle" IF
#                     - Vérifier la présence de la valeur "input_value"
#                       dans la liste "input_list"
#                     - Si présente, la retirer de la liste
#                     - Si absente, l’ajouter dans la liste
#               - Dans la fonction "main" réaliser les actions suivantes
#                 - Appeler la fonction "display_all_list"
#                   Pour afficher le contenu présent à l’origine du programme
#                 - Appeler la fonction "check_add_or_remove" avec
#                   - "my_list_one" et "Thirty"
#                   - "my_list_two" et "30"
#                 - Appeler la fonction "display_all_list"
#                   Pour afficher le contenu modifié dans le du programme
#                 - Avec la "structure de contrôle" FOR et
#                   la "structure de donnée" 20, 10, "Twenty", "Ten"
#                   - Appeler la fonction "check_add_or_remove" avec
#                     - "my_list_one" et la valeur courante de
#                       la "structure de contrôle"
#                     - "my_list_two" et la valeur courante de
#                       la "structure de contrôle"
#                 - Appeler la fonction "display_all_list"
#                   Pour afficher le contenu modifié dans le du programme
# 
#               - A la fin du programme, vous devez obtenir
#                 - "my_list_one" avec des nombre en lettre
#                   de manière décroissante
#                 - "my_list_two" avec des nombre en chiffre
#                   de manière décroissante
#                 - "my_list_three" avec les deux listes modifiées
#
# Author:       DESTOMBES Matthieu
#
# Date:         2021.02.22
# ##############################################################################

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

# Variable creation
my_list_one = [10, 20]
my_list_two = []
my_list_three = []

# Adding value to second list
my_list_two.append("Ten")
my_list_two.append("Twenty")

# Adding value to third list
my_list_three.append(my_list_one)
my_list_three.append(my_list_two)


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def display_all_list():
    """
    This function display all the list content of the current program.

    :return: None
    """

    global my_list_one
    global my_list_two
    global my_list_three

    for current_list in my_list_one, my_list_two, my_list_three:
        print("Current list contain: {0}".format(current_list))


def check_add_or_remove(input_list, input_value):
    """
    This function check the list content and:
    - Add value if not exist.
    - Remove value if exist.

    :param input_list: List - List to modify
    :param input_value: Variant - Value to check
    :return: List - The new list
    """

    if input_value not in input_list:
        input_list.append(input_value)

    else:
        input_list.remove(input_value)

    return input_list


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':

    print("\n")

    display_all_list()

    my_list_one = check_add_or_remove(my_list_one, "Thirty")
    my_list_two = check_add_or_remove(my_list_two, 30)

    print("\n")

    display_all_list()

    for value_to_change in 20, 10, "Twenty", "Ten":
        my_list_one = check_add_or_remove(my_list_one, value_to_change)
        my_list_two = check_add_or_remove(my_list_two, value_to_change)

    print("\n")

    display_all_list()
