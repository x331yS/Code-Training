#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display multiple messages with defined variables
#               by WHILE.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "03_display_messages_while.py"
#               - Créer une variable "my_first_name" avec votre prénom
#               - Créer une variable "my_last_name" avec votre nom de famille
#               - Créer une variable "my_occurrence" avec le nombre 10
#               - Créer une variable "current_occurrence" avec le nombre 0
#               - Afficher le message "Hello world (WHILE)!"
#               - Avec structure de contrôle itérative "while"
#                 - Afficher le message
#                   "([current_occurrence]): My name is ‘[prénom] [nom de famille]’"
#                   en utilisant les variable précédente
#                 - Utiliser l’incrémentation et les variables
#                   "current_occurrence" et "my_occurrence"
#                   pour afficher le message 11 fois
#
# Author:       DESTOMBES Matthieu
#
# Date:         2021.02.08
# ##############################################################################

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

my_first_name = "Matthieu"
my_last_name = "DESTOMBES"
my_occurrence = 10
current_occurrence = 0


# ==============================================================================
# PROCESS
# ==============================================================================

# Display message one time
print("Hello world (WHILE)!")

# While start to 0 until occurrence is equal to 10
while current_occurrence <= my_occurrence:

    # Display message
    print(
        "({0}): My name is ‘{1} {2}’".format(
            current_occurrence,
            my_first_name,
            my_last_name
        )
    )

    current_occurrence += 1
