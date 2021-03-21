#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display math helper solution.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "05_math_helper.py"
#               - Reprendre le principe de la fonction "multiplication_op"
#                 et faire de même pour les opérations suivantes
#                 - La division dans une fonction "divide_op"
#                 - L’addition dans une fonction "plus_op"
#                 - La soustraction dans une fonction "minus_op"
#               - Dans la fonction "main"
#                 - Utiliser la "structure de contrôle" FOR de 1 à 10 compris
#                   - Afficher le dénominateur commun "Tables of ‘[current]’"
#                   - Appeler la fonction "multiplication_op" avec l’élément
#                     courant comme paramètre
#                   - Appeler la fonction "divide_op" avec l’élément
#                     courant comme paramètre
#                   - Appeler la fonction "plus_op" avec l’élément
#                     courant comme paramètre
#                   - Appeler la fonction "minus_op" avec l’élément
#                     courant comme paramètre
#               - Faites en sorte que les résultats des 4 fonction soient
#                 affichée sur la même ligne, pour chaque occurrence
#                   - "XX * YY = [résultat] | XX / YY = [résultat] |
#                      XX + YY = [résultat] | XX - YY = [résultat]"
#
# Author:       DESTOMBES Matthieu
#
# Date:         2021.02.22
# ##############################################################################


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def multiplication_op(input_base):
    """
    This function return the 10 result of multiplication with
      the input_base number.

    :param input_base: Number - The number to use in multiplication.
    :return: List - The 10 string result of processing.
    """

    multiplication_result_process = []

    for current_multiple in range(1, 11):
        multiplication_result_process.append(
            "{0:0=2d} * {1:0=2d} = {2: =3d}".format(
                input_base,
                current_multiple,
                input_base * current_multiple
            )
        )

    return multiplication_result_process


def divide_op(input_base):
    """
    This function return the 10 result of division with
      the input_base number.

    :param input_base: Number - The number to use in division.
    :return: List - The 10 string result of processing.
    """

    division_result_process = []

    for current_multiple in range(1, 11):
        division_result_process.append(
            "{0:0=2d} / {1:0=2d} = {2: =5.2f}".format(
                input_base,
                current_multiple,
                input_base / current_multiple
            )
        )

    return division_result_process


def plus_op(input_base):
    """
    This function return the 10 result of addition with
      the input_base number.

    :param input_base: Number - The number to use in addition.
    :return: List - The 10 string result of processing.
    """

    plus_result_process = []

    for current_multiple in range(1, 11):
        plus_result_process.append(
            "{0:0=2d} + {1:0=2d} = {2: =2d}".format(
                input_base,
                current_multiple,
                input_base + current_multiple
            )
        )

    return plus_result_process


def minus_op(input_base):
    """
    This function return the 10 result of subtraction with
      the input_base number.

    :param input_base: Number - The number to use in subtraction.
    :return: List - The 10 string result of processing.
    """

    minus_result_process = []

    for current_multiple in range(1, 11):
        minus_result_process.append(
            "{0:0=2d} - {1:0=2d} = {2: =3d}".format(
                input_base,
                current_multiple,
                input_base - current_multiple
            )
        )

    return minus_result_process


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':

    print("\nMultiplication table")

    for current_run in range(1, 11):

        print("\nTables of '{0:0=2d}'\n==============".format(current_run))

        multiplication_return = multiplication_op(current_run)
        division_return = divide_op(current_run)
        plus_return = plus_op(current_run)
        minus_return = minus_op(current_run)

        for current_display in range(0, 10):

            print("{0} | {1} | {2} | {3}".format(
                multiplication_return[current_display],
                division_return[current_display],
                plus_return[current_display],
                minus_return[current_display]
            ))
