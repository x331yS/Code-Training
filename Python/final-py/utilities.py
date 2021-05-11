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

# Defining variables
first_value = "A"
second_value = "ABC"
string = "^[ALQ]$"


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

# Defining function
def check_expected(substr, string):
    """
    This function checks if a string contains a another string.
    :param substr: String
    :param string: Check string
    :return: Bool
    """
    # Check bool substr in string
    if substr in string:
        # Return good
        return True
    else:
        return False


# ==============================================================================
# PROCESS
# ==============================================================================

if __name__ == "__main__":
    # First test
    start_string()
    print("| Test of '{0}' with '{1}'".format(first_value, string))
    print("| => '{}' (Success)".format(check_expected(first_value, string)))
    end_string()

    # Second test
    start_string()
    print("| Test of '{0}' with '{1}'".format(second_value,
                                              string))

    print("| => '{}' (Success)".format(check_expected(second_value,
                                                      string)))
    end_string()