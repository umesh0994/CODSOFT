"""Simple Calculator with Basic Arithmetic Operations"""

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    print("\nSelect operation:\n1. Addition (+)\n2. Subtraction (-)\n3. Multiplication (*)\n4. Division (/)")
    ops = {'1': '+', '2': '-', '3': '*', '4': '/', '+': '+', '-': '-', '*': '*', '/': '/'}
    while (ch := input("Enter choice (1/2/3/4): ").strip()) not in ops:
        print("Invalid choice!")
    return ops[ch]

def calculate(a, b, op):
    funcs = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y else "Error: Division by zero!"}
    return funcs[op](a, b)

def main():
    print("=" * 40 + "\n       SIMPLE CALCULATOR\n" + "=" * 40)
    while True:
        n1, n2 = get_number("Enter first number: "), get_number("Enter second number: ")
        op = get_operation()
        result = calculate(n1, n2, op)
        print(f"\n{'=' * 40}\nResult: {result if isinstance(result, str) else f'{n1} {op} {n2} = {result}'}\n{'=' * 40}")
        if input("\nDo another? (yes/no): ").strip().lower() not in ['yes', 'y']:
            print("\nThank you! Goodbye!")
            break

if __name__ == "__main__":
    main()
