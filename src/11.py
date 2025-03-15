
import random

def random_python(length):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    code = ""
    for i in range(length):
        code += random.choice(alphabet)
    return code