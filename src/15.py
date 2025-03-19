import random

def get_random_code(length=8):
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    code = ''
    for _ in range(length):
        code += random.choice(characters)
    return code
