from challenges.desafio1 import median_numbers
import statistics


def test_median_numbers():
    values = [9, 2, 1, 4, 6, 23]
    values2 = [15, 2, 19, 25, 13, 10, 7]
    values3 = [21, 14, 5, 1, 8, 12, 9, 3, 99]

    x = median_numbers(values)
    y = median_numbers(values2)
    z = median_numbers(values3)
    assert x == statistics.median(values)
    assert y == statistics.median(values2)
    assert z == statistics.median(values3)
