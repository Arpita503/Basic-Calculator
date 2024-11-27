print(
"""
Welcome to the pytohn Calclator!
Select an opereation:
1. Addition(+)
2. Subtraction(-)
3. Multiplication(*)
4. Division(/)
5. Modulus(%)
6. Power(^)
7. Exit(q)

"""
)

def Calculator(choice, n1, n2):
    result = None
    operation = ' '

    if choice == '1':
        result =  n1 + n2
        operation = '+'
    elif choice == '2':
        result =  n1 - n2
        operation = '-'
    elif choice == '3':
        result =  n1 * n2
        operation = '*'
    elif choice == '4':
        if n2 == 0:
            print("Zero by division erroe")
            return
        result =  n1 / n2
        operation = '/'
    elif choice == '5':
        result =  n1 % n2
        operation = '%'
    elif choice == '6':
        result =  n1 ** n2
        operation = '^'
    elif choice == '7':
        print("Exiting the calculator")
        return
    else:
        print("Enter a Valid Operation!!")

    if result is not None:
        print(f"result: {n1} {operation} {n2}  = {result}")


choice = input("Enter your choice: ")
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
Calculator(choice, n1, n2)

another_choice = input("Do you want to perform another calculation? (yes/No): ")
while another_choice == 'yes':
    choice =input("Enter your choice: ")
    n1 = int(input("Enter the First Number: "))
    n2 = int(input("Enter the second number: "))

    Calculator(choice, n1, n2)
    

if another_choice == 'no':
    print("Exit!!")