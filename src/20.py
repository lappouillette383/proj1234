def fibonacci(n):
    """
    Generate a list of Fibonacci numbers up to n.
    
    Parameters:
    n (int): The upper limit for generating Fibonacci numbers.
    
    Returns:
    list: A list containing the Fibonacci sequence up to n.
    """
    if n <= 1:
        return [0]
    else:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq

# Example usage:
fibonacci_list = fibonacci(15)
print(fibonacci_list)
