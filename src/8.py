import random

def get_random_code():
    code = ''
    for _ in range(12):
        code += str(random.randint(0, 9))
    return code
