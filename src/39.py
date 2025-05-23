import math
def calculate_pi():
    """
    Calculate and print Pi to 7 decimal places.
    
    Example:
    >>> pi = calculate_pi()
    >>> pi
    "3.141592653589793238"
    """
    # Calculate the value of Pi using its first few terms
    numerator = 10**3 + 3*10**2 + 10
    denominator = (2*3*5)*math.factorial(4)
    
    pi_value = numerator / denominator
    
    return f"Pi: {pi_value:.7f}"
