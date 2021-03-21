#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display multiple messages with defined variables
#               by FOR.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
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

# ==============================================================================
# PROCESS
# ==============================================================================

# Display message one time
print("Hello world (FOR)!")

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
