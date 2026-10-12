def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

def calculate_percentage(part, total):
    if total == 0:
        return "Error: Cannot calculate percentage with a total of zero."
    return (part / total) * 100

def main():
    while True:
        print("\nSuggested Menu")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break
            
        if choice in ['1', '2', '3', '4', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numerical values.")
                continue
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"Result: {result}")
            elif choice == '6':
                result = calculate_percentage(num1, num2)
                if isinstance(result, str):
                    print(result)
                else:
                    print(f"Result: {result}%")
                    
        elif choice == '5':
            try:
                num = int(input("Enter an integer to check: "))
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
                continue
            print(f"Result: The number is {check_even_odd(num)}")
            
        else:
            print("Invalid choice! Please select an option between 1 and 7.")

if __name__ == "__main__":
    main()0

