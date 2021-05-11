# Defining function
def multiplication_op(input_base: int):
    # Iterative control structure
    for multiple in range(1, 11):
        # Defining variable
        multiplication_result = input_base * multiple
        # Displaying result
        print("{0:0=2d} * {1:0=2d} = {2:=3d}".format(
            input_base,
            multiple,
            multiplication_result
        ))


# Defining entry point
if __name__ == '__main__':
    # Iterative control structure
    for current in range(1, 11):
        # Printing newline
        print("\n")
        # Displaying string
        print("Table of '{0}'".format(
            current
        ))
        # Calling function
        multiplication_op(current)
