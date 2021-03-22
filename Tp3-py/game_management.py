import user_management
import finder_management

id = None
user_id = 0


def create_new_user():
    global user_id
    if user_id >= user_management.all_users_information["data"]["user_max"]:
        print("Too many users")
    else:
        user_management.get_user_name()
        user_id += 1
    return


def user_selection():
    return


def range_change_proposal():
    return


def check_end_of_the_game():
    if finder_management.quit_game:
        print("Do you want to qui the game ?")
    return


def display_user_statistics():
    return


if __name__ == '__main__':
    check_end_of_the_game()
