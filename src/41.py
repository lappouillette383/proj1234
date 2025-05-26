import random

def make_random_list(n):
    """
    Generates an n-element list of random integers.
    """
    return [random.randint(1, 100) for _ in range(n)]

if __name__ == "__main__":
    n = int(input("Enter the length of the list: "))
    print(f"Generated {n}-element list: {make_random_list(n)}")
