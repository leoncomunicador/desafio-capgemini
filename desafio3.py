from more_itertools import random_permutation
import math


def grid_string(str):
    replace = str.replace(' ', '')
    permutation = ''.join(random_permutation(replace))
    size_string = len(permutation)
    square = math.ceil(math.sqrt(size_string))

    for i in range(len(permutation)):
        if i % square == 0:
            sub = permutation[i:i+square]
            lst = []
            for j in sub:
                lst.append(j)
            print(' '.join(lst))


grid_string('ola mundo')
