"""
Calculator Application - Main entry point
"""

from calculator import Calculator


def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*50)
    print("SIMPLE CALCULATOR")
    print("="*50)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulo (Remainder)")
    print("6. Power")
    print("7. Square Root")
    print("8. View Result")
    print("9. Clear")
    print("0. Exit")
    print("="*50)


def get_numbers(operation_name=""):
    """Get two numbers from user"""
    try:
        num1 = float(input(f"Enter first number: "))
        num2 = float(input(f"Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return None, None


def get_single_number():
    """Get a single number from user"""
    try:
        num = float(input("Enter a number: "))
        return num
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return None


def main():
    """Main calculator application"""
    calc = Calculator()
    
    print("Welcome to the Simple Calculator!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (0-9): ").strip()
        
        if choice == '0':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        elif choice == '1':
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                result = calc.add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
        
        elif choice == '2':
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                result = calc.subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
        
        elif choice == '3':
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                result = calc.multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
        
        elif choice == '4':
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                try:
                    result = calc.divide(num1, num2)
                    print(f"\n{num1} / {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
        
        elif choice == '5':
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                try:
                    result = calc.modulo(num1, num2)
                    print(f"\n{num1} % {num2} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
        
        elif choice == '6':
            num1, num2 = get_numbers()
            if num1 is not None and num2 is not None:
                result = calc.power(num1, num2)
                print(f"\n{num1} ** {num2} = {result}")
        
        elif choice == '7':
            num = get_single_number()
            if num is not None:
                try:
                    result = calc.square_root(num)
                    print(f"\n√{num} = {result}")
                except ValueError as e:
                    print(f"\nError: {e}")
        
        elif choice == '8':
            result = calc.get_result()
            print(f"\nCurrent result: {result}")
        
        elif choice == '9':
            calc.clear()
            print("\nCalculator cleared!")
        
        else:
            print("\nInvalid choice! Please try again.")


if __name__ == "__main__":
    main()
