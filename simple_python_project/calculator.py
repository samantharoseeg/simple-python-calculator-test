"""
Simple Calculator Module

This module provides basic mathematical operations.
It demonstrates clean code with proper documentation.
"""


def add(first_number, second_number):
    """
    Add two numbers together.
    
    Args:
        first_number (float): The first number to add
        second_number (float): The second number to add
    
    Returns:
        float: The sum of the two numbers
    
    Raises:
        TypeError: If either argument is not a number
    
    Examples:
        >>> add(2, 3)
        5
        >>> add(-1, 1)
        0
        >>> add(2.5, 1.5)
        4.0
        >>> add(0, 0)
        0
    """
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError(f"Both arguments must be numbers. Got {type(first_number).__name__} and {type(second_number).__name__}")
    
    return first_number + second_number


def subtract(first_number, second_number):
    """
    Subtract the second number from the first number.
    
    Args:
        first_number (float): The number to subtract from
        second_number (float): The number to subtract
    
    Returns:
        float: The difference between the two numbers
    
    Raises:
        TypeError: If either argument is not a number
    
    Examples:
        >>> subtract(10, 3)
        7
        >>> subtract(5, 5)
        0
        >>> subtract(-1, -1)
        0
        >>> subtract(2.5, 0.5)
        2.0
    """
    if not isinstance(first_number, (int, float)) or not isinstance(second_number, (int, float)):
        raise TypeError(f"Both arguments must be numbers. Got {type(first_number).__name__} and {type(second_number).__name__}")
    
    return first_number - second_number