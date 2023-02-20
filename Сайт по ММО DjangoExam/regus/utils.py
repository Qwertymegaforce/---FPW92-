import random


def random_create_token():
    i = []
    for cycle in range(0, 12):
        s = random.randint(0, 9)
        i.append(str(s))
    token = ''.join(i)

    return token
