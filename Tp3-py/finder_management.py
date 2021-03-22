#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script is the main part of the riddle game
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:
#               Objectifs :
#                               • Définir 8 variables internes au programme:
#                                       • Message de la question principale
#                                       • Message de la question pour limite inférieur
#                                       • Message de la question pour limite supérieur
#                                       • Message indiquant la bonne réponse
#                                       • Message indiquant que la valeur est supérieur
#                                       • Message indiquant que la valeur est inférieur
#                                       • Message indiquant le succès et le nombre de tentative
#                               • Le nombre de tentative
#                               • Utilisation de 5 fonctions permettant:
#                                       • L’initialisation de la partie
#                                           • Le nom de la partie est donné en argument
#                                       • La demande à l’utilisateur d’un nombre
#                                           • La réponse de l’utilisateur doit être retournée par la
#                                             fonction au format « String » (Chaîne de caractère)
#                                       • La comparaison du nombre donné par l’utilisateur au
#                                         nombre interne
#                                       • Le nombre donné par l’utilisateur est en argument
#                                       • La modification des limites supérieur et inférieur
#                                       • Les nouvelles limites sont données en argument
#                               • Valeur par défaut 100 et 200
#                               • Félicitation de l’utilisateur et fin de partie
#
#                               • Un programme de test dans le fichier qui permet de vérifier que
#                                 les fonctions fonctionnent correctement en lançant 5 parties
#                               • Process commun entre les parties
#                               • Affichage du nom de la partie
#                               • Affichage des limites
#                               • Demande du nombre à l’utilisateur jusqu’à obtention du bon nombre
#                               • Affichage du résultat de la comparaison
#                               • Affichage de la réussite
#                               • Affichage du nombre de tentative
#                               • Partie 1 avec valeurs par défaut
#                               • Partie 2 avec valeurs limites modifiées (Valeurs par défaut)
#                               • Partie 3 avec valeur limite inférieur modifiée en demandant à l’utilisateur
#                                               valeur limite supérieur par défaut
#                               • Partie 4 avec valeur limite supérieur modifiée en demandant à l’utilisateur
#                                               valeur limite inférieur par défaut
#                               • Partie 5 avec valeurs limites inférieur et supérieur
#                                 modifiées en demandant à l’utilisateur
#
#
#               Contraintes :
#                               • Fichier python nommé « finder_management.py »
#                               • Les 8 variables globales doivent être nommées
#                                       • « main_question »
#                                       • « lower_question »
#                                       • « upper_question »
#                                       • « good_answer »
#                                       • « count_display »
#                                       • « bad_lower_answer »
#                                       • « bad_upper_answer »
#                                       • « try_number »
#                               • Les 5 fonctions doivent être nommées
#                                       • « start_the_finder »
#                                       • « ask_the_number_to_user »
#                                       • « check_the_number »
#                                       • « limits_modify »
#                                       • « congrats_user »
#                                   • La quasi-totalité de la mise en forme faite avec
#                                     des « print » doit être contenue dans les fonctions
#
#                                   • Fonction « main » avec le programme de test
#                                   • Ne doit pas s’exécuter si le fichier est importé
#                                   • Toutes les affectations, modifications des variables internes
#                                     doivent utiliser les fonctions définies à cet effet
#                                   • Seule la partie mise en forme faite avec des « print » pour la
#                                     demande de modification des limites doit-être contenue dans le
#                                     programme de test
#
#
# Author:       LEJOSNE Florian
#
# Date:         2021.03.21
# ##############################################################################


# ==============================================================================
# IMPORTS
# ==============================================================================

import randomize_management
import roman

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

win = False
try_number = 0
set_top_space = "/======================================"
set_end_space = "\\======================================"
set_middle_space = "|======================================"
main_question = "| Aim of this game is to find a randomize number as:\n" \
                "| - Lower or equal to '{0}':\n" \
                "| - Upper or equal to '{1}':"
lower_question = "| Give me the new lower limit: "
upper_question = "| Give me the new upper limit: "
good_answer = "| Yes. It is! You win!"
count_display = "| Success in '{0}' attempt(s)."
bad_lower_answer = "| No. It's lower..."
bad_upper_answer = "| No. It's upper..."
wrong_answer = "| Please, give a numeral input in the limits"
game_number = 1
game = "| Game"


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

# Defining function
def ask_the_number_to_user():
    """
    This function send a message for the user and retrieves an int into the variable user_num

    :return: None
    """
    # Importing variable from global scope
    global try_number

    # Retrieving number from user
    user_num = int(input("| Give me a number: "))
    if type(user_num) == str:
        print(wrong_answer)
        printer_top()
    check_the_number(user_num)


# Defining function
def check_the_number(user_num):
    """
    This function check if the user number is less than , equal or greater than the internal_number

    :param user_num : The number of the user
    :return: None
    """
    # Importing variable from global scope
    global win

    # Check user_num in limits
    if user_num < randomize_management.internal_lower_limit or user_num > randomize_management.internal_upper_limit:
        print(wrong_answer)
        print(set_middle_space)
    # If number is randomize, bool is True
    else:
        if user_num > randomize_management.internal_number:
            # If superior
            print(bad_lower_answer)
            print(set_middle_space)
        elif user_num < randomize_management.internal_number:
            # If inferior
            print(bad_upper_answer)
            print(set_middle_space)
        else:
            print(good_answer)
            win = True


# Defining function
def limits_modify(new_lower_limit, new_upper_limit):
    """
    This function overwrites the internal_lower_limit variable into the new_lower_limit parameter
    and it overwrites the internal_upper_limit variable into the new_upper_limit parameter

    :param new_lower_limit : The new modified lower limit
    :param new_upper_limit : The new modified upper limit
    :return: None
    """

    randomize_management.set_internal_lower_limit(new_lower_limit)
    randomize_management.set_internal_upper_limit(new_upper_limit)


# Defining function
def congrats_user():
    """
    This function print the attempts number

    :return: None
    """
    print(count_display.format(try_number))
    printer_end()


# Defining function
def start_the_finder():
    """
    This function print the main_question with the limits and the game number,
    and set attempts

    :return: None
        """
    # Importing variables from global scope
    global win
    global try_number
    global game_number

    # Convert int to roman int
    printer_top()
    print(game, roman.toRoman(game_number))
    game_number += 1

    # Main question
    print(set_middle_space)
    print(main_question.format(
        randomize_management.get_internal_lower_limit(),
        randomize_management.get_internal_upper_limit()
    ))
    print(set_middle_space)
    # Calling function
    randomize_management.set_internal_number()
    # Iterative control structure
    while not win:
        # Calling function
        ask_the_number_to_user()
        # Incrementing variable
        try_number += 1
    # Congrats
    congrats_user()
    # Resetting variable
    win = False
    try_number = 0


def printer_top():
    print(set_top_space)


def printer_end():
    print(set_end_space)
    print()


# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':
    # Calling function for Game I
    start_the_finder()

    # Modifying limits for Game II
    limits_modify(100, 200)
    # Calling function for Game II
    start_the_finder()

    # Modifying limits for Game III
    printer_top()
    limits_modify(int(input(lower_question)), 200)
    printer_end()
    # Calling function for Game III
    start_the_finder()

    # Modifying limits for Game IV
    printer_top()
    limits_modify(100, int(input(upper_question)))
    printer_end()
    # Calling function for Game IV
    start_the_finder()

    # Modifying limits for Game V
    printer_top()
    limits_modify(int(input(lower_question)), int(input(upper_question)))
    printer_end()
    # Calling function for Game V
    start_the_finder()
