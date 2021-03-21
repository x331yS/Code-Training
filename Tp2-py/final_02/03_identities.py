#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display messages with dictionary content.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "03_identities.py"
#               - Créer 1 dictionnaire "all_identity"
#               - Créer une fonction "set_identity" qui réalise
#                 les actions suivantes
#                 - Créer 1 dictionnaire "current_identity"
#                 - Demander à l’utilisateur son prénom, puis son nom.
#                 - Sauvegarder les deux données dans
#                   le dictionnaire "my_identity"
#                   - Clé "id_f_name" avec le prénom
#                   - Clé "id_l_name" avec le nom de famille
#                 - Générer un identifiant "unique_id" entre 0 et 5
#                 - Convertir cet identifiant en chaine de caractère
#                   sur 2 caractères
#                 - Tant que l’identifiant existe en tant que
#                   clé de "all_identity", relancer la génération
#                 - Affecter le dictionnaire "current_identity",
#                   contenant les informations du nouvel utilisateur,
#                   dans le dictionnaire "all_identity",
#                   en l’associant à la clé "unique_id"
#                 - Retourner un Tuple contenant "unique_id" et
#                   un bouléen qui indique si la génération a du être
#                   relancée au moins une fois.
#               - Dans la fonction "main"
#                 - Utiliser la "structure de contrôle" FOR
#                   - Faire 3 appels à la fonction "set_identity"
#                   - Afficher le message "New user ‘[prénom] [nom de famille]’
#                     have been created" en utilisant les informations
#                     de l’utilisateur fraichement créé
#                   - Dans le cas ou la génération a été relancé
#                     - Afficher une alerte par le message
#                       "/!\ Take care ID need to be re-created /!\"
#                 - Afficher le contenu du dictionnaire "all_identity"
# 
#               - Avez-vous reçu l’alerte ?
#               - Essayer avec 7 appels
#                 - Que se passe t il ?
#
# Author:       DESTOMBES Matthieu
#
# Date:         2021.02.22
# ##############################################################################

# ==============================================================================
# IMPORTS
# ==============================================================================

import random


# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

all_identities = {}


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def set_identity():
    """
    This function tell to User First name and Last name.
    A number will be generated and distinct is check from the main dictionary.
    If already exist, it will be regenerated.
    Finally set the new identity with distinct ID.

    :return: Tuple - The unique Ident and
                     a boolean with True if regeneration is needed.
    """

    global all_identities

    current_identity = {
        'id_f_name': input("What is the first name of the user: "),
        'id_l_name': input("What is the last name of the user: ")
    }

    id_generation_is_already_used = False

    unique_id = "{0:0=2d}".format(
        random.randint(0, 5)
    )

    while unique_id in all_identities.keys():
        unique_id = "{0:0=2d}".format(
            random.randint(0, 5)
        )
        id_generation_is_already_used = id_generation_is_already_used | True

    all_identities[unique_id] = current_identity

    return unique_id, id_generation_is_already_used


# ==============================================================================
# PROCESS
# ==============================================================================

# Main function
if __name__ == '__main__':

    for current_run in range(3):
        print("\n/---")
        ident_key, relaunched = set_identity()

        print("New user ‘{0} {1}’ have been created".format(
            all_identities[ident_key]['id_f_name'],
            all_identities[ident_key]['id_l_name']
        ))

        if relaunched:
            print("/!\\ Take care ID need to be re-created /!\\")
        print("\\---")

    print("\n{0}".format(all_identities))
