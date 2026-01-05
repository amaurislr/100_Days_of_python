
import calculartor_art

print(calculartor_art.calculator_ascii)

def add (n1, n2):
    return n1 + n2

def sustrab (n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

operations ={
    "+": add,
    "-": sustrab,
    "*": multiply,
    "/": division,
}


def calculator():
    num1 = float(input("What's the first number?: "))

    should_continue = True
    while should_continue:

        for symbols in operations:
            print(symbols)

        operations_symbols = input("Pick an operations: ")
        num2 = float(input("What's the next number: "))

        result = operations[operations_symbols](num1, num2)

        print(f"{num1} {operations_symbols} {num2} = {result}")

        choice_continue = input ("Type 'Y' to continue calculating wih 0.0, or type  'N' to start a new calculation: ").lower()

        if choice_continue == "y":
            num1 = result
        else:
            should_continue = False
            print("\n" * 20)
            calculator()

calculator()

