# Program for a simple calculator that adds, subtracts, multiplies, and divides
def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y 

print("Select Operation")
print(" 1. Addition")
print(" 2. Subtraction")
print(" 3. Multiplication")
print(" 4. Division")

while True:
    # Input from user
    choice = input("Enter choice(1-4): ")
    # Confirm choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter 1st number here: "))
        num2 = float(input("Enter 2nd number here: "))

        
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")


