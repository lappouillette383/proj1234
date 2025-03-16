
import random

def proj1234(n):
    result = []
    for i in range(n):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        if x > y:
            result.append(x - y)
        else:
            result.append(y - x)
    return result