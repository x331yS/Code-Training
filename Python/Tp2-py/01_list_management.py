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


# Defining entry point
if __name__ == '__main__':
    # Calling function
    display_all_list()
