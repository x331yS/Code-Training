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
# GLOBAL VARIABLE
# ==============================================================================

first_leetspeak_message = 'Welcome in Leet Speak world'
second_leetspeak_message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# ==============================================================================
# SUB FUNCTIONS
# ==============================================================================

def hacker(text):
    """"
    This function encrypt the message


    :param: text : The string input
    :return: text : The string input after change
    """
    # Range of all letter
    for ch in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u',
               'v', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T',
               'V', 'X', 'Y', 'Z']:
        if ch in text:
            # Replace all letter
            text = text.replace('a', '/-\\').replace('b', '|3').replace('c', '(').replace('d', '...').replace('e',
                                                                                                              '[-').replace(
                'f', '|=').replace('h', '#').replace('i', '!').replace('j', '_|').replace('k', '|<').replace('l',
                                                                                                             '|_').replace(
                'm', '/\/\\').replace('n', '|\|').replace('o', '[]').replace('p', '|>').replace('r',
                                                                                                '/2').replace(
                's', '$').replace('v', '|/').replace(
                'y', '`/').replace('z', '7_').replace('A', '1').replace('W', '84').replace('S', '74').replace('D',
                                                                                                              '¨¨').replace(
                'I', '&&').replace('N', '44')
    return text


def unhacker(text):
    """"
    This function uncrypt the message


    :param: text : The string input
    :return: text : The string input after change
    """
    # Range of all letter
    for ch in ['/-\\', '|3', '(', 'D', '[-', '|=', '(_+', '#', '!', '_|', '|<', '|_', '/\/\\', '|\|', '[]', '|>',
               '(_,)', '/2', '$', '|_|',
               '|/', ')(', '`/', '7_', 'A', 'B', 'C', 'F', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T',
               'V', 'X', 'Y', 'Z']:
        if ch in text:
            # Replace all letter
            text = text.replace('/-\\', 'a').replace('|3', 'b').replace('(', 'c').replace('...', 'd').replace('[-',
                                                                                                              'e').replace(
                '|=', 'f').replace('#', 'h').replace('!', 'i').replace('_|', 'j').replace('|<', 'k').replace('|_',
                                                                                                             'l').replace(
                '/\/\\', 'm').replace('|\|', 'n').replace('[]', 'o').replace('|>', 'p').replace('/2',
                                                                                                'r').replace(
                '$', 's').replace('|/', 'v').replace(
                '`/', 'y').replace('7_', 'z').replace('1', 'A').replace('84', 'W').replace('74', 'S').replace('¨¨',
                                                                                                              'D').replace(
                '&&', 'I').replace('44', 'N')
    return text

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

# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == '__main__':
    # First test
    start_string()
    print("| Original LeetSpeak Message: '{}'".format(
        first_leetspeak_message
    ))
    end_string()
    # Encrypted first test
    start_string()
    print("| Encrypted LeetSpeak Message: '{}'".format(
        hacker(first_leetspeak_message)
    ))
    end_string()
    # Decryptes first test
    start_string()
    print("| Encrypted LeetSpeak Message: '{}'".format(
        unhacker(hacker(first_leetspeak_message))
    ))
    end_string()
    # Second test
    start_string()
    print("| Original LeetSpeak Message: '{}'".format(
        second_leetspeak_message
    ))
    end_string()
    # Encrypted Second test

    start_string()
    print("| Encrypted LeetSpeak Message: '{}'".format(
        hacker(second_leetspeak_message)
    ))
    end_string()
    # Decrypted Second test
    start_string()
    print("| Encrypted LeetSpeak Message: '{}'".format(
        unhacker(hacker(second_leetspeak_message))
    ))
    end_string()
