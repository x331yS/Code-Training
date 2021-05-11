#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display math helper solution.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "04_math_helper.py"
#               - Créer une fonction "multiplication_op" qui réalise
#                 les actions suivantes
#                 - Prendre 1 argument en entrée
#                   - "input_base", un chiffre
#                 - Utilisation de la "Structure de contrôle" FOR
#                   de 1 à 10 compris
#                   - Faire le calcul de la multiplication
#                     "input_base" par l’élément en cours
#                   - Affiche la multiplication avec les chiffres de gauche
#                     sur 2 caractères et l’égalité avec le résultat
#                   - "XX * YY = [résultat]"
#                   - Essayez de mettre en forme vos résultats pour
#                     qu’ils soient ordonnés
#               - Dans la fonction "main"
#                 - Utiliser la "structure de contrôle" FOR de 1 à 10 compris
#                   - Afficher le multiplicateur en cours "Table of ‘[current]’"
#                   - Appeler la fonction "multiplication_op" avec l’élément
#                     courant comme paramètre
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
    This function print the 10 result of multiplication with
      the input_base number.

    :param input_base: Number - The number to use in multiplication.
    :return: None
    """

    for current_multiple in range(1, 11):
        print("{0:0=2d} * {1:0=2d} = {2: =3d}".format(
            input_base,
            current_multiple,
            input_base * current_multiple
        ))


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':

    for current_run in range(1, 11):

        print("\nTables of '{0:0=2d}'\n==============".format(current_run))

        multiplication_op(current_run)
