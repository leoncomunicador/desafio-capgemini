from itertools import combinations


def difference_pairs(array, difference):
    temp = combinations(array, 2)
    arranjos = [item for item in temp]
    result = [abs(x - y) for x, y in arranjos]
    return result.count(difference)


print(difference_pairs([1, 5, 3, 4, 2], 2))
