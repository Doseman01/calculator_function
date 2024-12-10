# main.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b

def divide(a, b):
    """Returns the quotient of two numbers. Raises an exception if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Basic Calculator:")
    print("Addition of 2 and 3:", add(2, 3))
    print("Subtraction of 5 from 10:", subtract(10, 5))
    print("Multiplication of 4 and 6:", multiply(4, 6))
    print("Division of 6 by 2:", divide(8, 2))

