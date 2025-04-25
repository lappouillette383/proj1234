def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        raise ValueError("x must be non-negative")

try:
    result = square_root(-4)
    print(result)
except Exception as e:
    print(e)
