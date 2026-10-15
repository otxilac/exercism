def factors(number: int) -> list[int]:
    """Returns prime factors of a given number"""
    factor_list = []
    for i in range(1, number):
        if number % i == 0:
            factor_list.append(i)
    return factor_list

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    number = int(number)
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    aliquot = sum(factors(number))

    if number == aliquot:
        return "perfect"
    elif number < aliquot:
        return "abundant"
    else:
        return "deficient"
