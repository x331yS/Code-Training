# Defining function
def multiplication_op(input_base: int):
    # Defining list
    multiplication_result_process = []
    # Iterative control structure
    for multiple in range(1, 11):
        # Defining variable
        multiplication_result = input_base * multiple
        # Appending list
        multiplication_result_process.append("{0:0=2d} * {1:0=2d} = {2:=3d}".format(
            input_base,
            multiple,
            multiplication_result
        ))
    # Returning list
    return multiplication_result_process


# Defining function
def division_op(input_base: int):
    # Defining list
    division_result_process = []
    # Iterative control structure
    for multiple in range(1, 11):
        # Defining variable
        division_result = input_base / multiple
        # Appending list
        division_result_process.append("{0:0=2d} / {1:0=2d} = {2:0=2.2f}".format(
            input_base,
            multiple,
            division_result
        ))
    # Returning list
    return division_result_process


# Defining function
def addition_op(input_base: int):
    # Defining list
    addition_result_process = []
    # Iterative control structure
    for multiple in range(1, 11):
        # Defining variable
        addition_result = input_base + multiple
        # Appending list
        addition_result_process.append("{0:0=2d} + {1:0=2d} = {2:=3d}".format(
            input_base,
            multiple,
            addition_result
        ))
    # Returning list
    return addition_result_process


# Defining function
def subtraction_op(input_base: int):
    # Defining list
    subtraction_result_process = []
    # Iterative control structure
    for multiple in range(1, 11):
        # Defining variable
        subtraction_result = input_base - multiple
        # Appending list
        subtraction_result_process.append("{0:0=2d} - {1:0=2d} = {2:=3d}".format(
            input_base,
            multiple,
            subtraction_result
        ))
    # Returning list
    return subtraction_result_process


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

        # Calling functions
        multiplication = multiplication_op(current)
        division = division_op(current)
        addition = addition_op(current)
        subtraction = subtraction_op(current)

        # Iterative control structure
        for display in range(0, 10):
            # Displaying result
            print("{0} | {1} | {2} | {3}".format(
                multiplication[display],
                division[display],
                addition[display],
                subtraction[display]
            ))
