from challenges.desafio2 import difference_pairs


def test_difference_pairs():
    array = [1, 5, 3, 4, 2]
    diff = 2

    array2 = [4, 6, 1, 5, 9]
    diff2 = 2

    assert 3 == difference_pairs(array, diff)
    assert 1 == difference_pairs(array2, diff2)
