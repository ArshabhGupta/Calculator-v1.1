import math
import statistics

def add(a, b):
    sum = a + b
    return sum

def subtract(a, b):
    sum = a - b
    return sum

def multiply(a, b):
    sum = a * b
    return sum

def divide(a, b):
    sum = a / b
    return sum

def exponent(a, b):
    sum = a ** b
    return sum

def root(a, b):
    sum = a ^ -b
    return sum

print("Welcome to the calculator! \n")
print("What's new?")
print("Trigonometric and Statistic Functions")

while True:
    print("Choose your operation:-")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponention")
    print("6. Roots")
    print("7. Factorial")
    print("8. HCF")
    print("9. LCM \n")
    print("New Functions")
    print("10. Sine")
    print("11. Cosine")
    print("12. Tangent")
    print("13. Arc Sine")
    print("14. Arc Cosine")
    print("15. Arc Tangent")
    print("16. Arithmetic Mean")
    print("17. Median")
    print("18. Mode")

    choice = int(input("Please enter the option number: "))
    
    if choice == 1:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(add(a, b))
    elif choice == 2:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))    
        print(subtract(a, b))
    elif choice == 3:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))    
        print(multiply(a, b))
    elif choice == 4:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))        
        print(divide(a, b))
    elif choice == 5:
        a = int(input("Enter the base: "))
        b = int(input("Enter the exponent: "))
        print(math.pow(a, b))  
    elif choice == 6:
        a = float(input("Enter a number: "))
        b = float(input("Enter a number: "))
        print(root(a, b))
    elif choice == 7:
        a = int(input("Enter a number: "))
        print(math.factorial(a))
    elif choice == 8:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(math.gcd(a, b))
    elif choice == 9:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        print(math.lcm(a, b))
    elif choice == 10:
        a = int(input("Enter the degrees"))
        math.sin(a)
    elif choice == 11:
        a = int(input("Enter the degrees"))
        math.cos(a)
    elif choice == 12:
        a = int(input("Enter the degrees"))
        math.tan(a)
    elif choice == 13:
        a = int(input("Enter the degrees"))
        math.asin(a)
    elif choice == 14:
        a = int(input("Enter the degrees"))
        math.acos(a)
    elif choice == 15:
        a = int(input("Enter the degrees"))
        math.atan(a)
    elif choice == 16:
        list = eval(input("Enter a list of number in (): "))
        print(statistics.mean(list))
    elif choice == 17:
        list = eval(input("Enter a list of number in (): "))
        print(statistics.median(list))
    elif choice == 18:
        list = eval(input("Enter a list of number in (): "))
        print(statistics.mode(list))
    else:
        print("Invalid choice!")

    x = input("Do you want to retry? (Y/N): ")
    if x == 'Y':
        continue
    else:
        break