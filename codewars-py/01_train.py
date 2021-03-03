def make_negative(number):
    result = 0 - number
    if number <= 0:
        return number
    return result


def multiply(a, b):
    c = a * b
    return c


def _if(bool, func1, func2):
    if bool:
        func1()
    else:
        func2()


def truthy():
    print("True")


def falsey():
    print("False")

    # _if(True, truthy, falsey)


def unusual_five():
  print(unusual_five())


unusual_five(), 5, "lol"