from Operations.addition import add
from Operations.subtraction import subs
from Operations.multiplication import multiply
from Operations.division import div
from Operations.user_input import take_user_input

def calculate():
    """does the calculate logic."""
    num1, num2, operation = take_user_input()

    if operation == "+":
        answer = add(a=num1, b=num2)
    elif operation == "-":
        answer = subs(a=num1, b=num2)
    elif operation == "*":
        answer = multiply(a=num1, b=num2)
    elif operation == "/":
        answer = div(a=num1, b=num2)
    else:
        answer = "I dont know what to do!!!"

    print(answer)

    return answer