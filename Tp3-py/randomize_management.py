#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script randomize numbers for riddle game
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:
#               Objectifs :
#                                • Gérer 3 variables internes au programme
#                                • Un nombre généré de manière aléatoire entre deux bornes définies
#                                • Valeur par défaut à ‘None’
#                                • La borne supérieur
#                                • Valeur par défaut à ‘1000’
#                                • La borne inférieur
#                                • Valeur par défaut à ‘0’
#                                • Utilisation de 6 fonctions permettant
#                                • La génération, puis la récupération du nombre aléatoire en mémoire
#                                • L’affectation, puis la récupération de la borne supérieur en mémoire
#                                • L’affectation, puis la récupération de la borne inférieur en mémoire
#                                • Un programme de test dans le fichier qui permet de vérifier que
#                                  les fonctions fonctionnent correctement
#                                • Affichage des valeurs par défaut en mémoire (Limites et Nombre généré)
#                                • Génération et affichage du nombre avec limites par défaut
#                                • Modification des limites supérieur (150) et inférieur (100)
#                                • Affichage des nouvelles valeurs (Limites uniquement)
#                                • Génération et affichage du nombre avec limites modifiées
#
#
#               Contraintes :
#                                • Fichier python nommé « randomize_management.py »
#                                • Les 3 variables globales doivent être nommées
#                                       • « internal_number »
#                                       • « internal_upper_limit »
#                                       • « internal_lower_limit »
#                                • Les 6 fonctions doivent être nommées
#                                       • « set_internal_number »
#                                       • « get_internal_number »
#                                       • « set_internal_upper_limit »
#                                       • « get_internal_upper_limit »
#                                       • « set_internal_lower_limit »
#                                       • « get_internal_lower_limit »
#                                 • Aucun « print » dans les fonctions
#                                 • Fonction « main » avec le programme de test
#                                 • Ne doit pas s’exécuter si le fichier est importé
#                                 • Toutes les affectations, modifications des
#                                 variables internes doivent utiliser les fonctions définies à cet effet
#                                 • Toutes récupérations des valeurs contenues dans
#                                   les variables internes doivent utiliser les fonctions définies à cet effet
#                                 • Toute la partie mise en forme faite avec des « print » doit-être
#                                   contenue dans le programme de test
#
#
# Author:       LEJOSNE Florian
#
# Date:         2021.03.20
# ##############################################################################


# ==============================================================================
# IMPORTS
# ==============================================================================

import random

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

internal_number = None
internal_lower_limit = 0
internal_upper_limit = 1000


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

# Defining function
def get_internal_number():
    """
    This function retrieves the internal_number variable from global variable
    and return it.

    :return: internal_number
    """
    # Importing variable from global scope
    global internal_number
    # Returning variable
    return internal_number


# Defining function
def set_internal_number():
    """
    This function overwrites the internal_number variable into a random number between internal_lower_limit and
    internal_upper_limit using the random module's import randint.

    :return: None
    """
    # Importing variables from global scope
    global internal_number
    global internal_lower_limit
    global internal_upper_limit
    # Redefining variable
    internal_number = random.randint(internal_lower_limit, internal_upper_limit)


# Defining function
def get_internal_lower_limit():
    """
    This function retrieves the internal_lower_limit variable from global variable
    and return it.

    :return: internal_lower_limit: The low limit of the scope
    """
    # Importing variable from global scope
    global internal_lower_limit
    # Returning variable
    return internal_lower_limit


# Defining function
def set_internal_lower_limit(new_lower_limit):
    """
    This function overwrites the internal_lower_limit variable into the new_lower_limit parameter

    :param new_lower_limit : The new modified lower limit
    :return: None
    """
    # Importing variable from global scope
    global internal_lower_limit
    # Redefining variable
    internal_lower_limit = new_lower_limit


# Defining function
def get_internal_upper_limit():
    """
    This function retrieves the internal_upper_limit variable from global variable

    :return: internal_upper_limit: The high limit of the scope
    """
    # Importing variable from global scope
    global internal_upper_limit
    # Returning variable
    return internal_upper_limit


# Defining function
def set_internal_upper_limit(new_upper_limit):
    """
    This function overwrites the internal_lower_limit variable into the new_upper_limit parameter

    :param new_upper_limit: The new modified upper limit
    :return: None
    """
    # Importing variable from global scope
    global internal_upper_limit
    # Redefining variable
    internal_upper_limit = new_upper_limit


# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':
    print(
        "Default internal_number is: {0}\n"
        "Default internal_lower_limit is: {1}\n"
        "default internal_upper_limit is: {2}".format(
            get_internal_number(),
            get_internal_lower_limit(),
            get_internal_upper_limit()
        ))
    # Calling function for test
    set_internal_number()
    print(
        "Generated internal_number with default limit is: {0}".format(
            get_internal_number()
        ))

    print()

    # Calling functions for test
    set_internal_lower_limit(100)
    set_internal_upper_limit(150)
    set_internal_number()

    # Showing modified values
    print(
        "Modified internal_lower_limit is: {0}\n"
        "Modified internal_upper_limit is: {1}".format(
            get_internal_lower_limit(),
            get_internal_upper_limit()
        ))
    print(
        "Generated internal_number with modified limit is: {0}".format(
            get_internal_number()
        ))
