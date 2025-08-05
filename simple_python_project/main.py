#!/usr/bin/env python3
"""
Calculator Demo - Main Module

This script demonstrates how to use the calculator functions
with various examples and an interactive mode.
"""

# Import our calculator functions
from calculator import add, subtract


def demonstrate_addition():
    """Show examples of the add function."""
    print("\n--- Addition Examples ---")
    
    # Example 1: Adding positive numbers
    num1, num2 = 10, 5
    result = add(num1, num2)
    print(f"Adding {num1} + {num2} = {result}")
    
    # Example 2: Adding negative numbers
    num1, num2 = -3, -7
    result = add(num1, num2)
    print(f"Adding {num1} + {num2} = {result}")
    
    # Example 3: Adding decimals
    num1, num2 = 3.14, 2.86
    result = add(num1, num2)
    print(f"Adding {num1} + {num2} = {result}")


def demonstrate_subtraction():
    """Show examples of the subtract function."""
    print("\n--- Subtraction Examples ---")
    
    # Example 1: Subtracting positive numbers
    num1, num2 = 20, 8
    result = subtract(num1, num2)
    print(f"Subtracting {num1} - {num2} = {result}")
    
    # Example 2: Result is negative
    num1, num2 = 5, 10
    result = subtract(num1, num2)
    print(f"Subtracting {num1} - {num2} = {result}")
    
    # Example 3: Subtracting negative numbers
    num1, num2 = 15, -5
    result = subtract(num1, num2)
    print(f"Subtracting {num1} - ({num2}) = {result}")


def interactive_calculator():
    """Run an interactive calculator session."""
    print("\n--- Interactive Calculator ---")
    print("Enter 'q' to quit at any time.\n")
    
    while True:
        # Get the operation from the user
        operation = input("Choose operation (add/subtract) or 'q' to quit: ").lower()
        
        if operation == 'q':
            print("Thanks for using the calculator!")
            break
        
        if operation not in ['add', 'subtract']:
            print("Invalid operation. Please choose 'add' or 'subtract'.")
            continue
        
        try:
            # Get the numbers from the user
            first = float(input("Enter first number: "))
            second = float(input("Enter second number: "))
            
            # Perform the calculation
            if operation == 'add':
                result = add(first, second)
                print(f"Result: {first} + {second} = {result}")
            else:  # operation == 'subtract'
                result = subtract(first, second)
                print(f"Result: {first} - {second} = {result}")
            
            print()  # Empty line for readability
            
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")
        except Exception as e:
            print(f"An error occurred: {e}\n")


def main():
    """Main function to run all demonstrations."""
    print("=" * 50)
    print("Welcome to the Simple Calculator Demo!")
    print("=" * 50)
    
    # Run the demonstrations
    demonstrate_addition()
    demonstrate_subtraction()
    
    # Ask if user wants to try interactive mode
    print("\n" + "=" * 50)
    response = input("\nWould you like to try the interactive calculator? (yes/no): ")
    
    if response.lower() in ['yes', 'y']:
        interactive_calculator()
    
    print("\n" + "=" * 50)
    print("Calculator demo complete!")


if __name__ == "__main__":
    # Run the main function when script is executed directly
    main()