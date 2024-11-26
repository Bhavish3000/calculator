"""_Calculator_
    """
import art
def addition(n1, n2):
    """_summary_

    Args:
        n1 (_float_): _first number_
        n2 (_float_): _second number_

    Returns:
        _float_: _result of addition_
    """
    return n1 + n2

def subtraction(n1, n2):
    """_summary_

    Args:
        n1 (_float_): _first number_
        n2 (_float_): _second number_

    Returns:
        _float_: _result of subtraction_
    """
    return n1 - n2

def multiplication(n1, n2):
    """_summary_

    Args:
        n1 (_float_): _first number_
        n2 (_float_): _second number_

    Returns:
        _number_: _result of multiplication_
    """
    return n1 * n2

def division(n1, n2):
    """_summary_

    Args:
        n1 (_float_): _first number_
        n2 (_float_): _second number_

    Returns:
        _float_: _quotient of division_
    """
    return n1 / n2

def modules(n1, n2):
    """_summary_

    Args:
        n1 (_float_): _first number_
        n2 (_float_): _second number_

    Returns:
        _float_: _remainder of division_
    """
    return n1 % n2


operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "%": modules}
def calculator():
    print(art.cal)
    num1= float(input("Enter the first numbr: "))
    SHOULD_ACCUMULATE= True
    while SHOULD_ACCUMULATE:

        for symbol in operations:
            print(symbol)
        operations_symbol= input("Choose an operator: ")
        num2= float(input("Enter the second number: "))
        answer= operations[operations_symbol](n1=num1, n2=num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")
        choice= input(f"Type y to continue calculating with {answer} or Type n to start a new calculation: ")
        if choice == "y":
            num1= answer
        else:
            SHOULD_ACCUMULATE = False
            print("\n" * 40)
            calculator()
calculator()
