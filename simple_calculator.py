"""
    This is a simple calculator, takes in 3 integer inputs from the user:
        1. The first value to be calculated
        2. The symbol, or mathematical sign 
        3. The second value to be calculated
    It then takes the integer inputs and evaluates it according to the provided symbol, and performs a mathematical
    calculation of the provided integers.
"""

def user_input():
    """
        This function get the gets the 3 inputs from the user.
    """

    first_value = input("Please insert the first number: ")
    symbol = input("Please insert a symbol between division(/), multiplication(*), addition(+) or subtraction:")
    second_value = input("Please input the second number: ")
    print(first_value, symbol, second_value)
    return first_value, symbol, second_value


def is_int(value):
    """
        This function evaluates whether or not the provided value is an interger, if so, it returns True
        else returns False.
    """

    try:
        int(value)
        return True
    except ValueError:
        return False


def mathematical_processes(first_value, symbol, second_value):
    """
        This function evaluates whether:
            * the users input is an integer.
            * and if the symbol provided is valid.
        if all is well, it returns a calculation as per the users request and breaks.
        if not it returns 'Invalid mathematical symbol.' and the symbol, or the invalid input.
    """
    statement = "The answer is: "
    if is_int(first_value) and is_int(second_value) and symbol == "/":
        answer = int(first_value) / int(second_value)
        print(statement, answer)
    elif is_int(first_value) and is_int(second_value) and symbol == "*":
        answer =  int(first_value) * int(second_value)
        print(statement, answer)
    elif is_int(first_value) and is_int(second_value) and symbol == "+":
        answer =  int(first_value) + int(second_value)
        print(statement, answer)
    elif is_int(first_value) and is_int(second_value) and symbol == "-":
        answer = int(first_value) - int(second_value)
        print(statement, answer)
    else:
        print("Invalid mathematical symbol.", symbol)


if __name__ == '__main__':
    p = user_input()
    first_value = p[0]
    symbol = p[1]
    second_value = p[2]
    mathematical_processes(first_value, symbol, second_value)
