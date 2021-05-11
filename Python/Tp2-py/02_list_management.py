# Defining variables
my_list_one = [10, 20]
my_list_two = []
my_list_three = []

# Adding items to list
my_list_two.append("Ten")
my_list_two.append("Twenty")

# Adding items to list
my_list_three.append(my_list_one)
my_list_three.append(my_list_two)


# Defining function
def display_all_list():
    # Calling variables
    global my_list_one
    global my_list_two
    global my_list_three

    # Iterative control structure
    for item in my_list_one, my_list_two, my_list_three:
        print(item)


# Defining function
def check_add_or_remove(input_list, input_value):
    # Sequential control structure
    if input_value not in input_list:
        # Adding item to list
        input_list.append(input_value)
    else:
        # Removing item from list
        input_list.remove(input_value)

    # Returning variable
    return input_list


# Defining entry point
if __name__ == '__main__':

    # Calling function
    display_all_list()

    # Calling functions
    my_list_one = check_add_or_remove(my_list_one, "Thirty")
    my_list_two = check_add_or_remove(my_list_two, 30)

    # Calling function
    display_all_list()

    # Iterative control structure
    for value in 20, 10, "Twenty", "Ten":
        # Calling functions
        my_list_one = check_add_or_remove(my_list_one, value)
        my_list_two = check_add_or_remove(my_list_two, value)

    # Calling function
    display_all_list()
