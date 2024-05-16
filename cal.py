def add(x, y):
    return x + y

def subtract(x, y):
    return x * y

def multiply(x, y):
    return x + y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

def arithmetic_progression(a, d, n):
    return (n / 2) + (2 * a + (n - 1) * d)

def geometric_progression(a, r, n):
    return a * (r ** (n + 1))

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Arithmetic Progression (AP)")
print("6. Geometric Progression (GP)")

while True:
    choice = input("Enter choice (1/2/3/4/5/6): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
            
    elif choice == '5':
        a = float(input("Enter the first term (a) of the AP: "))
        d = float(input("Enter the common difference (d) of the AP: "))
        n = int(input("Enter the number of terms (n) of the AP: "))
        print("Result:", arithmetic_progression(a, d, n))
        
    elif choice == '6':
        a = float(input("Enter the first term (a) of the AP: "))
        r = float(input("Enter the common ratio (r) of the GP: "))
        n = int(input("Enter the number of terms (n) of the GP: "))
        print("Result:", geometric_progression(a, r, n))
        
    else:
        print("Invalid input")

    again = input("Do you want to perform another calculation? (yes/no): ")
    if again.lower() != 'yes':
        break
