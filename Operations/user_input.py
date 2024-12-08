def take_user_input():
    """Take input from user"""
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    operation = input("Please choose any one from '+ - * /': ")
    return a, b, operation