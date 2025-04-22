#Progam for performing calculation taking numbers and operant
def perform_calculation():
    print("Welcome to the calculator. ")
    try:
        num1 = int(input("enter the first number: "))
        num2 = int(input("enter the second number: "))
        operation = input("enter the operation(+,-,*,/) :")
        if operation == "+":
            result = num1 + num2
            print("You are using addition of two numbers.\n {} + {} = {}".format(num1, num2, result))
            with open("history.txt", "a") as f:
                f.write(str(num1) + "+" + str(num2) + "=" + str(result) + "\n")
        elif operation == "-":
            result = num1 - num2
            print("You are using subtraction of two numbers.\n {} - {} = {}".format(num1, num2, result))
            with open("history.txt", "a") as f:
                f.write(str(num1) + "-" + str(num2) + "=" + str(result) + "\n")

        elif operation == "*":
            result = num1 * num2
            print("You are using multiplication of two numbers.\n {} * {} = {}".format(num1, num2, result))
            with open("history.txt", "a") as f:
                f.write(str(num1) + "*" + str(num2) + "=" + str(result) + "\n")

        elif operation == "/":
            try:
                result = num1 / num2
                print("You are using division of two numbers.\n {} / {} = {}".format(num1, num2, result))
                with open("history.txt", "a") as f:
                    f.write(str(num1) + "/" + str(num2) + "=" + str(result) + "\n")
            except ZeroDivisionError:
                print("You can't divide by zero")

        else:
            print("Invalid operation")
    except ValueError:
        print("You didn't enter a number")
        perform_calculation()

"""Program for history """
'''
#in this way i was reading each line as a string so i would get O/p as '[1+2=3]' '[1*8=8]' '[10-2=8]'
def view_history():
    try:
        with open("history.txt", "r") as f:
            history = f.readlines()
            if not history:
                print("No history to show")
            else:
                for line in history:
                    line = line.strip()
                    print(line)
    except FileNotFoundError:
        print(" There is no file history.txt")
'''
#in this way i read the full history.txt data as one string and i dont get a
def view_history():
    try:
        with open("history.txt", "r") as f:
            history = f.read()
            print(history)
    except FileNotFoundError:
        print(" There is no file history.txt")

def clear_history():
    with open("history.txt", "w") as f:
        f.write("This is the history of your calculation.\n")

def main_menu():
    print("welcome to the calculator")
    print("1. perform calculation")
    print("2. view history")
    print("3. clear history")
    print("4. Exit")
    try:
        select = int(input("Enter your selection: "))
        if select == 1:
            perform_calculation()
            main_menu()
        elif select == 2:
            view_history()
            main_menu()
        elif select == 3:
            print("Thank you for using calculator")
            print("cleared history")
            clear_history()
            main_menu()
        elif select == 4:
            print("Thank you for using calculator")
            quit()
        else:
            print("Invalid selection")
            main_menu()

    except ValueError:
        print("You didn't enter a number")


main_menu()
