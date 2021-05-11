#!/usr/bin/env python3
# coding: utf-8
# ##############################################################################
# Description:  This script crypt or decrypt string
#
# Required:     - Run as Standard User.
#               - Python 3.x
#
#
# Author:       LEJOSNE Florian
#
# Date:         2021.04.08
# ##############################################################################

# ==============================================================================
# IMPORTS
# ==============================================================================


# ==============================================================================
# GLOBAL VARIABLE
# ==============================================================================

first_mess = 'Welcome in Crypto World'
second_mess = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'


# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def test():
    """
    This function try to code and decode with first and second message

    :return: None
    """
    # First test
    start_string()
    print("| Original Crypto Message: '{}'".format(
        first_mess
    ))
    end_string()
    # Encrypted first test
    start_string()
    print("| Encrypted Crypto Message: '{}'".format(
        crypt(first_mess)
    ))
    end_string()
    # Decryptes first test
    start_string()
    print("| Decrypted Crypto Message: '{}'".format(
        decrypt(crypt(first_mess))
    ))
    end_string()
    # Second test
    start_string()
    print("| Original Crypto Message: '{}'".format(
        second_mess
    ))
    end_string()
    # Encrypted Second test

    start_string()
    print("| Encrypted Crypto Message: '{}'".format(
        crypt(second_mess)
    ))
    end_string()
    # Decrypted Second test

    start_string()
    print("| Decrypted Crypto Message: '{}'".format(
        decrypt(crypt(second_mess))
    ))
    end_string()


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


def decrypt(decrypt_mess):
    """"
    This function decrypt the message


    :param: decrypt_mess
    :return: decrypted_message
    """
    decrypted_message = ""
    if decrypt_mess:
        for char in decrypt_mess:
            # If Alphabet
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                # If Upper
                if 65 <= ord(char) <= 90:
                    if ord(char) + 13 > 90:
                        char = chr(ord(char) + 13 - 90 + 65 - 1)
                    else:
                        char = chr(ord(char) + 13)
                else:
                    if ord(char) + 13 > 122:
                        char = chr(ord(char) + 13 - 122 + 97 - 1)
                    else:
                        char = chr(ord(char) + 13)
            decrypted_message += char
    return decrypted_message


def crypt(encrypt_mess):
    """"
    This function encrypt the message


    :param: encrypt_mess
    :return: encrypted_message
    """
    encrypted_message = ""
    if encrypt_mess:
        for char in encrypt_mess:
            # If Alphabet
            if 65 <= ord(char) <= 90 or 97 <= ord(char) <= 122:
                # If Upper
                if 65 <= ord(char) <= 90:
                    if ord(char) + 13 > 90:
                        char = chr(ord(char) + 13 - 90 + 65 - 1)
                    else:
                        char = chr(ord(char) + 13)
                else:
                    if ord(char) + 13 > 122:
                        char = chr(ord(char) + 13 - 122 + 97 - 1)
                    else:
                        char = chr(ord(char) + 13)
            encrypted_message += char
    return encrypted_message


# ==============================================================================
# PROCESS
# ==============================================================================
if __name__ == '__main__':
    test()
