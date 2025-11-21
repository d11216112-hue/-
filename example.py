"""
Example usage of the safe_division function.

This script demonstrates how to use the safe_division function
to prevent division by zero errors.
"""

from safe_division import safe_division


def main():
    """Demonstrate safe_division usage"""
    print("=== Safe Division Function Demo ===\n")
    
    # Example 1: Normal division
    print("Example 1: Normal division")
    result = safe_division(10, 2)
    print(f"  safe_division(10, 2) = {result}\n")
    
    # Example 2: Division by zero (prevented)
    print("Example 2: Division by zero (prevented)")
    result = safe_division(10, 0)
    if result is None:
        print(f"  safe_division(10, 0) = {result}")
        print("  Error prevented! Division by zero returns None.\n")
    
    # Example 3: Practical usage with error handling
    print("Example 3: Practical usage with error handling")
    numerator = 100
    denominator = 0
    result = safe_division(numerator, denominator)
    
    if result is None:
        print(f"  Cannot divide {numerator} by {denominator}")
        print("  Reason: Division by zero is not allowed.\n")
    else:
        print(f"  {numerator} / {denominator} = {result}\n")
    
    # Example 4: Valid division
    print("Example 4: Valid division")
    numerator = 100
    denominator = 4
    result = safe_division(numerator, denominator)
    
    if result is None:
        print(f"  Cannot divide {numerator} by {denominator}")
    else:
        print(f"  {numerator} / {denominator} = {result}\n")


if __name__ == "__main__":
    main()
