import random
import string


def random_string(length=5):
    return ''.join((random.choice(st
                    ring.ascii_letters) for i in range(length)))