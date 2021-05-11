# Importing module
import random

# Defining variable
all_identity = {}


# Defining function
def set_identity():
    # Importing variable
    global all_identity

    # Defining dictionary
    current_identity = {
        "id_f_name": input("First name: "),
        "id_l_name": input("Last name: ")
    }

    id_already_used = False

    # Generating variable
    unique_id = "{0:0=2d}".format(
        random.randint(0, 5)
    )

    # Iterative control structure
    while unique_id in all_identity.keys():
        # Generating variable
        unique_id = "{0:0=2d}".format(
            random.randint(0, 5)
        )

        # Redefining variable
        id_already_used = id_already_used | True

    # Adding item to dictionary
    all_identity[unique_id] = current_identity

    # Returning variables
    return unique_id, id_already_used


if __name__ == '__main__':

    # Iterative control structure
    for current_run in range(3):

        # Defining variables
        ident_key, relaunched = set_identity()

        # Printing variables
        print("New user '{0} {1}' have been created".format(
            all_identity[ident_key]['id_f_name'],
            all_identity[ident_key]['id_l_name']
        ))

        if relaunched:
            print("/!\ Take care ID needs to be re-generated /!\\")

        # Printing newline
        print()

    # Printing dictionary
    print("{0}".format(
        all_identity
    ))
