def generate_random_code(length):
    import random
    result = ""
    for i in range(length):
        result += chr(random.randint(65, 90))
    return result
