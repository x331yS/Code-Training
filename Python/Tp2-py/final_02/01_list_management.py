#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display messages with list content.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "01_list_management.py"
#               - Créer 3 listes
#                 - "my_list_one" contenant les nombres 10 et 20
#                 - "my_list_two"
#                 - "my_list_three"
#               - Ajouter les valeurs "Ten" et "Twenty" dans "my_list_two"
#               - Ajouter les listes "my_list_one" et "my_list_two"
#                 dans "my_list_three"
#               - Créer une fonction "display_all_list" qui réalise
#                 les actions suivantes
#                 - Utilisation de la "Structure de contrôle" FOR
#                 - Affiche le contenu des trois listes
#               - Dans la fonction "main" appeler la fonction "display_all_list"
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


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':

    display_all_list()
