from challenges.desafio3 import grid_string


def test_grid_string():
    string = 'olá mundo'
    string2 = 'bora estudar na Capgemini'
    x = print(string)
    y = print(string2)

    assert x == grid_string(string)
    assert y == grid_string(string2)
