import random
import string


def random_string(length=5):
    return ''.join((random.choice(string.ascii_letters) for i in range(length)))