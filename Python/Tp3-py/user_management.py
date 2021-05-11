#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script create a dictionary with user name and user statistics
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
# Deposit:
#               Objectifs :
#                               • Définition de 7 variables internes au programme
#                                   • 1 Dictionnaire contenant
#                                       • Toutes les informations utilisateurs
#                                       • Le nombre max d’utilisateur
#                                   • Message de la question pour le nom de famille
#                                   • Message de la question pour le prénom
#                                   • Message indiquant le bon chargement du fichier
#                                   • Message indiquant l’inexistence d’un fichier de sauvegarde
#                                   • Message indiquant la sauvegarde des utilisateurs
#                                   • Le nom du fichier de sauvegarde
#                                   • Utilisation de 9 fonctions permettant
#                                   • La modification du nombre maximum d’utilisateur
#                                   • La récupération du nombre maximum d’utilisateur
#                                   • L’ajout d’un nouvel utilisateur
#                                   • La récupération de la liste des utilisateurs enregistrés
#                                   • L’ajout des résultats d’une tentative d’un utilisateur
#                                   • Récupération de tous les résultats d’un utilisateur
#                                   • Récupération du nom complet d’un utilisateur
#                                   • Chargement des données utilisateurs depuis le fichier de sauvegarde
#                                   • Sauvegarde des données utilisateurs vers le fichier de sauvegarde
#
#                                   • Un programme de test dans le fichier qui permet de vérifier que les fonctions
#                                     réalisent leurs actions correctement avec le process suivant
#                                   • Récupération des anciennes statistiques
#                                   • Tentative de création de X utilisateurs(X étant le maximum d’utilisateur + 1)
#                                   • Gestion du nombre maximum d’utilisateur
#                                   • Affichage du nombre maximum en cours
#                                   • Tentative de modification à 1 utilisateur maximum
#                                   • Affichage du nombre maximum en cours
#                                   • Tentative de modification à 3 utilisateur maximum
#                                   • Affichage du nombre maximum en cours
#                                   • Ajout de statistiques aléatoires pour chaque utilisateur en mémoire
#                                   • Affichage de toutes les statistiques pour chaque utilisateur en mémoire
#                                   • Sauvegarde des statistiques
#
#                                   • Deux exécutions du programme ne produisent pas la même chose
#                                   • Exécution 1
#                                   • Recherche de fichier de sauvegarde inexistant
#                                   • Tentative de création de 3 utilisateurs
#                                   • Création de 2 utilisateurs
#                                   • Tentative de modification du nombre d’utilisateur
#                                   • Passage à 3 utilisateurs max
#                                   • Ajout de statistiques aléatoires sur les 2 utilisateurs existants
#                                   • Affichage des statistiques pour les 2 utilisateurs existants
#                                   • Sauvegarde des statistiques
#                                   • Exécution 2
#                                   • Recherche et chargement du fichier de sauvegarde existant
#                                   • Tentative de création de 4 utilisateurs
#                                   • Création de 1 utilisateur
#                                   • Tentative de modification du nombre d’utilisateur
#                                   • Ajout de statistiques aléatoires sur les 3 utilisateurs existants
#                                   • Affichage des statistiques pour les 3 utilisateurs existants
#                                   • Sauvegarde des statistiques
#
#
#
#               Contraintes :
#                                   • Les 7 variables globales doivent être initialisées dès
#                                     le début du programme et se nommer
#                                       • « all_users_information »
#                                       • « first_name_question »
#                                       • « last_name_question »
#                                       • « loading_success_message »
#                                       • « loading_failed_message »
#                                       • « saving_message »
#                                       • « statistic_file »
#                                   • Le fichier de sauvegarde doit être nommé « statistics.dat »
#                                   • Les 9 fonctions doivent être nommées
#                                       • « set_new_max_user »
#                                       • « get_max_user »
#                                       • « add_new_user »
#                                       • « get_list_of_users »
#                                       • « add_user_try_result »
#                                       • « get_user_statistics »
#                                       • « get_user_name »
#                                       • « load_statistics »
#                                       • « save_statistics »
#
#
#                                   • Fonction « set_new_max_user »
#                                       • Le nombre maximum d’utilisateur est mis à jour uniquement
#                                         dans le cas où il est supérieur au précédent
#
#                                   • Fonction « add_new_user »
#                                       • L’ajout d’utilisateur n’est possible que si le
#                                         nombre maximum n’est pas atteint
#                                       • Les informations de l’utilisateur sont associées à un identifiant unique
#                                       • L’ajout d’un utilisateur implique la création d’un dictionnaire dans le
#                                         dictionnaire principal « all_user_information » contenant:
#                                           • Clé « id_f_name » avec le prénom
#                                           • Clé « id_l_name » avec le nom de famille
#                                           • Clé « statistics » avec un dictionnaire vide pour les futures statistiques
#                                       • La fonction retourne un tuple avec
#                                         (Nouvel identifiant, Max user atteint ou pas)
#
#                                   • Fonction « get_list_of_users »
#                                       • Retourne une liste de tuples contenant
#                                         (Identifiant utilisateur, Nom complet utilisateur)
#                                       • Nom complet utilisateur veut dire « [Prénom] [Nom] »
#
#                                   • Fonction « add_user_try_result »
#                                       • Doit ajouter les statistiques suivantes à l’utilisateur donné
#                                           • Range min
#                                           • Range max
#                                           • Nombre de tentative
#                                       • La clé de l’événement est la date d’ajout au format ISO
#
#                                   • Fonction « get_user_name »
#                                       • Retourne le nom complet de l’utilisateur
#                                       • Nom complet utilisateur veut dire « [Prénom] [Nom] »
#
#                                   • Fonction « main » avec le programme de test
#                                       • Ne doit pas s’exécuter si le fichier est importé
#                                       • Toutes les affectations, modifications des variables internes
#                                         doivent utiliser les fonctions définies à cet effet
#                                       • Affichage et mise en forme
#                                       • La quasi-totalité de l’affichage avec mise en forme
#                                         faite avec des « print » doit-être contenue dans la fonction main
#                                       • Seul les affichages suivants sont fait dans les fonctions
#                                       • L’affichage des questions « Nom » / « Prénom»
#                                       • L’affichage du message de la réussite ou de l’impossibilité
#                                         du chargement (fichier de sauvegarde)
#                                       • L’affichage du message de la sauvegarde des statistiques
#
#
#
# Author:       LEJOSNE Florian
#
# Date:         2021.03.23
# ##############################################################################


# ==============================================================================
# IMPORTS
# ==============================================================================

import randomize_management
import finder_management

import ast
import datetime
import json

# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

all_users_information = {}
first_name_question = "| What is the first name of the user: "
last_name_question = "| What is the last name of the user: "
loading_success_message = "| Users statistics loaded!"
loading_failed_message = "| No previous statistics to load..."
saving_message = "| Users statistics saved!"
statistic_file = "statistics.dat"
user_id = 0
max_user_all = False


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def iterative():
    """
    This function find if the maximum user have been reached or add a new user

    :return: None
    """

    # Importing variables
    global user_id
    global max_user_all

    for user_id in range(len(all_users_information) - 1, get_max_user() + 1):
        # Sequential control structure
        if user_id >= get_max_user():
            finder_management.printer_top()
            print("| => Maximum number of user have been reached <=")
            finder_management.printer_end()
        else:
            # Call func
            finder_management.printer_top()
            new_user_properties = add_new_user()
            print("| New user '{0} {1}' have been created".format(
                all_users_information[user_id]["id_f_name"],
                all_users_information[user_id]["id_l_name"]
            ))
            print("| Default statistics set to '{0}'".format(
                all_users_information[user_id]["statistics"]
            ))
            finder_management.printer_end()
            # Redefining variables
            user_id = new_user_properties[0]
            max_user_all = new_user_properties[1]


def printer_user():
    """
    This function retrieves the number of user informations

    :return: None
    """
    finder_management.printer_top()
    print("| Previous maximum of users: '{0}'".format(get_max_user()))
    print("| New maximum of users: '{0}'".format(get_max_user()))


def add_statistics():
    """
    This function add st

    :return: None
    """

    # Importing variables
    global user_id

    finder_management.printer_top()
    for user_id in all_users_information:
        # If int
        if type(user_id) is int:
            # Displaying variables
            print("| Adding statistic for user: '{0}/{1}'".format(
                user_id,
                get_user_name(user_id)
            ))


def add_new_user():
    """
    This function adds a new user to the all_users_information dictionary and checks if user_id is equal to max_user

    :return: user_id +1 - Tuple , the number of user_id with increment
    :return: max_user_all - Tuple , bool
    """
    # Importing variables
    global user_id
    global max_user_all

    # If structure
    if user_id >= get_max_user():
        max_user_all = True

    # Defining dictionary items
    all_users_information[user_id] = {
        "id_f_name": input(first_name_question),
        "id_l_name": input(last_name_question)
    }
    all_users_information[user_id]["statistics"] = {}

    # Return tuple
    return user_id + 1, max_user_all


def set_new_max_user(new_max_user):
    """
    This function overwrites the value for the max_user item in the all_users_information dictionary.

    :param: nex_max_user
    :return: None
    """

    # Importing variable
    global all_users_information

    # If control
    if new_max_user > all_users_information["max_user"]:
        all_users_information["max_user"] = new_max_user


def get_max_user():
    """
    This functions returns the value for the max_user item in the all_users_information dictionary.

    :return: Number - Returns the value for the "max_user" key in all_users_information.
    """

    # Importing
    global all_users_information

    # Returning variable
    return all_users_information["max_user"]


# Defining function
def add_user_try_result(user_id):
    """
    This functions takes an ID number in parameter and attributes and randomly create statistics to a
    dictionary.

    :param: Number - The current user ID number
    :return: None
    """
    # Sequential control structure
    if type(user_id) is int:
        # Calling functions
        now = datetime.datetime.now().isoformat()
        randomize_management.set_internal_number()
        # Defining dictionary items
        all_users_information[user_id]["statistics"][now] = {
            "min": randomize_management.get_internal_lower_limit(),
            "max": randomize_management.get_internal_upper_limit(),
            "try": randomize_management.get_internal_number()
        }


def load_statistics():
    """
    This function loads a dictionary from the statistics.dat file and attributes it to the
    all_users_information dictionary.

    :return: loading_success_message - Returns a message if the file can be open
    :return: loading_failed_message - Returns a message if the file can't be open
    """

    # Import variable
    global all_users_information
    try:
        with open(statistic_file, "r") as file:

            # Get the variable in the file
            all_users_information = ast.literal_eval(file.read())

            # Return
            return loading_success_message
    except IOError:
        all_users_information["max_user"] = 2

        # Return
        return loading_failed_message


def get_user_name(user_id):
    """
    This function return id_f_name and id_l_name

    :param: user_id
    :return: all_users_information[user_id] with id_f_name and id_l_name keys
    """

    # Return
    return "{0} {1}".format(
        all_users_information[user_id]["id_f_name"],
        all_users_information[user_id]["id_l_name"]
    )


def save_statistics():
    """
    This functions saves the all_users_information dictionary into the statistics.dat file.

    :return: saving_message
    """

    # Importing variable
    global all_users_information

    # Open, Overwrite and Save in statistics.dat
    file = open(statistic_file, "w")
    file.write(str(all_users_information))
    file.close()
    # Return
    return saving_message


# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':

    # Calling function
    finder_management.printer_top()
    print(load_statistics())
    finder_management.printer_end()

    # Iterative struct
    iterative()
    printer_user()

    # Calling function
    set_new_max_user(3)
    print("| Last maximum of users: '{0}'".format(get_max_user()))
    finder_management.printer_end()

    # Add stat
    add_statistics()

    # Calling function
    add_user_try_result(user_id)
    finder_management.printer_end()

    # Iterative control structure
    add_statistics()

    # Print formatted dictionary
    print(json.dumps(all_users_information[user_id]["statistics"], indent=4))
    finder_management.printer_end()

    # Calling function
    finder_management.printer_top()
    print(save_statistics())
    finder_management.printer_end()
