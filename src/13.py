import random
import string

def get_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    print(get_random_string(10))

if __name__ == "__main__":
    main()
