from art import logo

# add
def add (n1 ,n2):
    return n1 + n2
# subtraction
def sub (n1 ,n2):
    return n1 - n2
# multiply
def mul (n1 ,n2):
    return n1 * n2
# divicion
def div (n1 ,n2):
    return n1 / n2

oprations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculater():
    print(logo)

    num1 = float(input("What is the first number ?: "))
    for symbol in oprations:
        print(symbol)
    should_continue = True

    while should_continue :
        operation_symbol = input("Pike an operation : ")
        num2 = float(input("What is the next number ?: "))
        function = oprations[operation_symbol]
        answer = function (num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        user_continue = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if user_continue == "y":
            num1 = answer

        else:
            should_continue = False
            calculater()

calculater()
