import string
import random


def generate_random_key(length=32):
    characters = string.ascii_letters + string.digits
    return "".join(random.choice(characters) for i in range(length))


if __name__ == "__main__":
    print(generate_random_key())
