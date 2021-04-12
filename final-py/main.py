#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script crypt or decrypt string
#
# Required:     - Run as Standard User.
#               - Python 3.x
#               - Sorry for the repetition, I don't get time
#
#
# Author:       LEJOSNE Florian
#
# Date:         2021.04.08
# ##############################################################################


# ==============================================================================
# IMPORTS
# ==============================================================================
import leet_speak
import crypto

# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================
def end_string():
    """"
    This function print the end symbol
    :return: None
    """
    print("\\===")
    print()


def start_string():
    """"
    This function print the start symbol
    :return: None
    """
    print("/===")


def start():
    """"
    This function start the game
    :return: None
    """
    start_string()
    # Questions simple
    print("| All the followings actions are available: ")
    print("| Q -Quit the application.")
    print("| A -Encrypt message from leet speak.")
    print("| B -Decrypt from leet speak message.")
    print("| C -Encrypt basic message.")
    print("| D -Decrypt basic message.")
    response = str(input("| Select your action: "))
    end_string()
    # Quit game letter
    while response != 'Q':
        start_string()
        # Quit game letter
        if response == 'q':
            quit_g = str(input("| Are you sure to quit ? "))
            # Quit game letter yes
            if quit_g == 'y':
                print("| You quit the application")
                return
            # Quit game letter no
            if quit_g == 'n':
                start()
            # Quit game letter yes
            if quit_g == 'Y':
                print("| You quit the application")
                return
            # Quit game letter no
            if quit_g == 'N':
                start()
            # Error typing
            else:
                print("| Please enter a correct answer")
                continue
        # Crypto game letter
        if response == 'A':
            a_quest = str(input("| What is the message to translate: "))
            crypto.crypt(a_quest)
            print("| Converted message is : {}".format(crypto.crypt(a_quest)))
            end_string()
            start()
        # Crypto game letter
        if response == 'a':
            a_quest = str(input("| What is the message to translate: "))
            crypto.crypt(a_quest)
            print("| Converted message is : {}".format(crypto.crypt(a_quest)))
            end_string()
            start()
        # Decrypto game letter
        if response == 'B':
            a_quest = str(input("| What is the message to translate: "))
            crypto.decrypt(a_quest)
            print("| Converted message is : {}".format(crypto.decrypt(a_quest)))
            end_string()
            start()
        # Decrypto game letter
        if response == 'b':
            a_quest = str(input("| What is the message to translate: "))
            crypto.decrypt(a_quest)
            print("| Converted message is : {}".format(crypto.decrypt(a_quest)))
            end_string()
            start()
        # LeetSpeak game letter
        if response == 'C':
            a_quest = str(input("| What is the message to translate: "))
            leet_speak.hacker(a_quest)
            print("| Converted message is : {}".format(leet_speak.hacker(a_quest)))
            end_string()
            start()
        # LeetSpeak game letter
        if response == 'c':
            a_quest = str(input("| What is the message to translate: "))
            leet_speak.hacker(a_quest)
            print("| Converted message is : {}".format(leet_speak.hacker(a_quest)))
            end_string()
            start()
        # LeetSpeak decrypt game letter
        if response == 'D':
            a_quest = str(input("| What is the message to translate: "))
            leet_speak.unhacker(a_quest)
            print("| Converted message is : {}".format(leet_speak.unhacker(a_quest)))
            end_string()
            start()
        # LeetSpeak decrypt game letter
        if response == 'd':
            a_quest = str(input("| What is the message to translate: "))
            leet_speak.unhacker(a_quest)
            print("| Converted message is : {}".format(leet_speak.unhacker(a_quest)))
            end_string()
            start()
        else:
            print("| Please enter a correct answer")
            start()
    quit_g = str(input("| Are you sure to quit ? "))
    if quit_g == 'y':
        print("| You quit the application")
        return
    if quit_g == 'n':
        start()
    if quit_g == 'Y':
        print("| You quit the application")
        return
    if quit_g == 'N':
            start()
    else:
        print("| Please enter a correct answer")
        end_string()
        start()


if __name__ == '__main__':
    start()
