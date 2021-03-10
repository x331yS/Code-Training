from random import randint

internal_number = None
internal_upper_limit = 1000
internal_lower_limit = 0
main_question = "Aim of this game is to find a randomize number as:"
lower_question = "Give me the new lower limit: "
upper_question = "Give me the new upper limit: "
try_number = 0
count_display = "Sucess in '{0}' attemps".format(try_number)
good_answer = "Yes. It is! You win!"
bad_lower_answer = "No. It's lower..."
bad_upper_answer = "No. It's upper..."


def set_internal_number(x):
    internal_number = x


def get_internal_number():
    return internal_number


def set_internal_upper_limit(x):
    internal_upper_limit = x


def get_internal_upper_limit():
    return internal_upper_limit


def set_internal_lower_limit(x):
    internal_lower_limit = x


def get_internal_lower_limit():
    return internal_lower_limit


def start_the_finder():
    print()


def ask_the_number_to_user():
    print()


def check_the_number():
    print()


def limits_modify():
    print(lower_question, end="")
    set_internal_lower_limit(int(input()))
    print(upper_question, end="")
    set_internal_upper_limit(int(input()))


def congrats_user():
    print(good_answer)


if __name__ == "__main__":
    limits_modify()
    print(main_question)
    print("- Lower or equal to '{0}".format(get_internal_lower_limit()))
    print("- Upper or equal to '{0}".format(get_internal_upper_limit()))
