"""
Safe Division Module

This module provides a safe division function that prevents division by zero errors.
"""


def safe_division(a, b):
    """
    Safely divide two numbers, preventing division by zero.
    
    Args:
        a (float or int): The numerator (dividend)
        b (float or int): The denominator (divisor)
    
    Returns:
        float or None: The result of a/b if b is not zero, None if b is zero
    
    Examples:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        None
        >>> safe_division(7, 3)
        2.3333333333333335
    """
    if b == 0:
        return None
    return a / b
