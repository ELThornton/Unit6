# Elena Thornton
# prime_factors.py
# 11/17/2017
# this programs makes a list of numbers and gets the prime factors out of it.


def prime_factor_number():
    """
    this get the number that the program with get the prime factors out of
    :return: number
    """
    user_number = input("please put the number in that you wish to get the prime factors of in:",)
    number = int(user_number)

    return number


def list_for_prime_factor_number(a):
    """
    this program appends the numbers to a list so that they can be systematical gone through and deleted
    :param a: this is the number from the last function.
    :return:list_of_numbers
    """
    list_of_number = []

    for x in range(2, a+1):
        list_of_number.append(x)

    return list_of_number


def factor_out_non_primes(b):
    """
    in this fucntion the non-prime numbers are factored out.
    :param b:this is the list of numbers from the last function.
    :return:this returns nothing.
    """

    p = []

    while len(b) > 0:
        number1 = b[0]
        p.append(number1)
        for factor in b:
            if factor % number1 == 0:
                b.remove(factor)
    print(p, "are your prime factors.")


def main():
    a = prime_factor_number()
    b = list_for_prime_factor_number(a)
    factor_out_non_primes(b)


main()
