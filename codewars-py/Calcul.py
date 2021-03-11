def calculator(x, y, op):
    if type(x) == int:
        if type(y) == int:
            if op == '+':
                return x + y
            if op == '*':
                return x * y
            if op == '-':
                return x - y
            if op == '/':
                return x / y
    return "unknown value"
