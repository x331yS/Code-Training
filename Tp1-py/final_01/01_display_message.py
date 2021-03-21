#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script display messages with defined variables.
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:      - Dans un fichier python nommé "display_messages.py"
#               - Créer une variable "my_first_name" avec
#                 votre prénom
#               - Créer une variable "my_last_name" avec
#                 votre nom de famille
#               - Afficher le message "Hello world!"
#               - Afficher le message "My name is ‘[prénom] [nom de famille]’"
#                 en utilisant les variables précédentes
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


# ==============================================================================
# PROCESS
# ==============================================================================

# Display messages
print("Hello world!")
print(
    "My name is ‘{0} {1}’".format(
        my_first_name,
        my_last_name
    )
)
