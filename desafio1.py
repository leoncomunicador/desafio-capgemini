import statistics

# Em Python, temos o módulo statistics com diferentes funções e classes para encontrar diferentes valores estatísticos de um conjunto de dados. A função median() desta biblioteca pode ser usada para encontrar a mediana de uma lista.


def median_numbers(numbers):
    return(statistics.median(numbers))


print(median_numbers([9, 2, 1, 4, 6]))
