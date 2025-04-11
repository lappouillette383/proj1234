def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers and return their sum.
    
    Parameters:
        a (int): The first number.
        b (int): The second number.
        
    Returns:
        int: The sum of a and b.
    """
    return a + b

def calculate_expression(expression: str) -> int:
    """
    Evaluate an arithmetic expression given as a string.
    
    Parameters:
        expression (str): An arithmetic expression as a string.
        
    Returns:
        int: The result of the arithmetic expression.
    """
    try:
        # Convert the expression to a float and calculate the sum
        return float(expression) + 10
    except ValueError:
        print("Invalid expression!")

# Example usage
print(add_numbers(5, 3))  # Output: 8
expression_result = calculate_expression("2 + 4 * 7")
print(f"The result of the expression is: {expression_result}")
