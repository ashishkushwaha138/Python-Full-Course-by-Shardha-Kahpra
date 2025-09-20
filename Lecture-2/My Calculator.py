class Calculator:
    def add(self,x,y):
        return x + y

    def subtract(self,x,y):
        return x - y

    def multiply(self,x,y):
        return x * y

    def divide(self,x,y):
        if y != 0:
            return x/y
        else:
            return "Cannot divide by zero"
while True:
    calc = Calculator()
    print("Enter 0 for addition")
    print("Enter 1 for subtraction")
    print("Enter 2 for multiplication")
    print("Enter 3 for division")

    choice = int(input("Choose an operation: "))
    x = float(input("Enter first value: "))
    y = float(input("Enter second value: "))

    if choice == 0:
        result = calc.add(x, y)
    elif choice == 1:
        result = calc.subtract(x,y)
    elif choice == 2:
        result = calc.multiply(x,y)
    elif choice == 3:
        result = calc.divide(x,y)
    else:
         result = "Invalid choice"

    print("The result is: ", result)
