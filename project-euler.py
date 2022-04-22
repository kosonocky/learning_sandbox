from decimal import DivisionByZero
from re import L
import math
import numpy as np


def problem_1(limit):
    """
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    """

    total = 0
    for i in range(limit):
        if (i % 3 == 0) | (i % 5 == 0):
            total += i
    return total


def problem_2(limit):
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    total = 0
    prev = 1
    current = 1
    while current <= limit:
        if current % 2 == 0:
            total += current
        current += prev
        prev = current - prev

    return total


def problem_3(number):
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    factored = False
    largest_prime = 0
    while factored is False:
        loop_completed = True
        for i in range(2, int(np.sqrt(number)+1)):
            # Check if i is prime
            i_is_prime = True
            for j in range(2, int(np.sqrt(i)+1)):
                if i % j == 0:
                    i_is_prime = False
                    break

            if i_is_prime is True:
                if number % i == 0:
                    if i > largest_prime:
                        largest_prime = i
                    print(f'{number} is disivisble by {i}')
                    number = int(number / i)
                    loop_completed = False
                    break
        if loop_completed is True:
            if number > largest_prime:
                largest_prime = number
            factored = True
    return largest_prime


def problem_4():
    """
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def palindromic(number):
        string_number = str(number)
        palindromic = True
        for i in range(0, len(string_number)//2):
            if string_number[i] != string_number[-(i+1)]:
                palindromic = False
                break
        return palindromic

    largest_palindrome = 0
    for i in range(999, 1, -1):
        for j in range(999, 1, -1):
            if (palindromic(i*j) is True) and (i*j > largest_palindrome):
                largest_palindrome = i*j
    return largest_palindrome


def problem_5_method_1(upper_bound):
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """
    number = upper_bound
    divisible = False
    while divisible is False:
        divisible = True
        number += 1
        for i in range(1, upper_bound + 1):
            if number % i != 0:
                divisible = False
                break
    return number


def problem_5_method_2(upper_bound):
    number = 1
    for i in range(1, upper_bound + 1):
        number *= i // math.gcd(i, number)
    return number


def problem_6(limit):
    sum_1 = 0
    sum_2 = 0
    for i in range(1, limit+1):
        sum_1 += i**2
        sum_2 += i
    answer = abs(sum_1 - (sum_2**2))
    return answer


def is_prime(number):
    for i in range(2, int(np.sqrt(number))+1):
        if number % i == 0:
            return False
    return True


def problem_7(limit):
    primes_found = 0
    i = 0
    while primes_found <= limit:
        i += 1
        if is_prime(i) is True:
            primes_found += 1
    return i


def problem_8(number_adjascent_digits):
    number_str = str(7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
    largest_product = 0
    for i in range(0, len(number_str)-number_adjascent_digits + 1):
        current_product = 1
        for j in range(i, i+number_adjascent_digits):
            current_product *= int(number_str[j])
        if current_product > largest_product:
            largest_product = current_product
            largest_product_sequence = number_str[i:i+number_adjascent_digits]
    return f'Largest Product: {largest_product} made from adjascent digits: {largest_product_sequence}'


def problem_9():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a2 + b2 = c2
    For example, 32 + 42 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """

    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - (a + b)
            if c > 0:
                if (c**2) == (a**2 + b**2):
                    return f"Pythagorean Triplet Found with a={a}, b={b}, c={c}.  abc = {a*b*c}"


def problem_10(upper_bound):
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    total_sum = 0
    for i in range(2, upper_bound+1):
        if is_prime(i) is True:
            total_sum += i
    return total_sum


def problem_11():
    def update_largest_product(largest_product, current_product):
        if largest_product < current_product:
            return current_product
        else:
            return largest_product

    largest_product = 0
    current_product = 1
    grid = [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
            [49, 49, 99, 40, 17, 81, 18, 57, 60, 87,
                17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
            [81, 49, 31, 73, 55, 79, 14, 29, 93, 71,
                40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
            [52, 70, 95, 23, 4, 60, 11, 42, 69, 24,
                68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
            [22, 31, 16, 71, 51, 67, 63, 89, 41, 92,
                36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
            [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33,
                53, 78, 36, 84, 20, 35, 17, 12, 50],
            [32, 98, 81, 28, 64, 23, 67, 10, 26, 38,
                40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
            [67, 26, 20, 68, 2, 62, 12, 20, 95, 63,
                94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
            [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78,
                78, 96, 83, 14, 88, 34, 89, 63, 72],
            [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35,
                14, 0, 61, 33, 97, 34, 31, 33, 95],
            [78, 17, 53, 28, 22, 75, 31, 67, 15, 94,
                3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
            [16, 39, 5, 42, 96, 35, 31, 47, 55, 58,
                88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
            [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44,
                37, 44, 60, 21, 58, 51, 54, 17, 58],
            [19, 80, 81, 68, 5, 94, 47, 69, 28, 73,
                92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
            [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57,
                32, 16, 26, 26, 79, 33, 27, 98, 66],
            [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33,
                67, 46, 55, 12, 32, 63, 93, 53, 69],
            [4, 42, 16, 73, 38, 25, 39, 11, 24, 94,
                72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
            [20, 69, 36, 41, 72, 30, 23, 88, 34, 62,
                99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
            [20, 73, 35, 29, 78, 31, 90, 1, 74, 31,
                49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
            [1, 70, 54, 71, 83, 51, 54, 69, 16, 92,
                33, 48, 61, 43, 52, 1, 89, 19, 67, 48],
            ]
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if (i + 3) < len(grid):
                if (j + 3) < len(grid[0]):
                    current_product = grid[i][j] * grid[i +
                                                        1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                    largest_product = update_largest_product(
                        largest_product, current_product)
                if (j - 3) >= 0:
                    current_product = grid[i][j] * grid[i +
                                                        1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
                    largest_product = update_largest_product(
                        largest_product, current_product)
            if (i - 3) >= 0:
                if (j + 3) < len(grid):
                    current_product = grid[i][j] * grid[i -
                                                        1][j+1] * grid[i-2][j+2] * grid[i-3][j+3]
                    largest_product = update_largest_product(
                        largest_product, current_product)
                if (j - 3) >= 0:
                    current_product = grid[i][j] * grid[i -
                                                        1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
                    largest_product = update_largest_product(
                        largest_product, current_product)
    return largest_product


def main():
    # print(problem_1(1000))
    # print(problem_2(4000000))
    # print(f'Largest prime factor is {problem_3(600851475143)}')
    # print(problem_4())
    # print(problem_5_method_2(20))
    # print(problem_6(100))
    # print(problem_7(10001))
    # print(problem_8(13))
    # print(problem_9())
    # print(problem_10(2000000))
    print(problem_11())
    pass


if __name__ == '__main__':
    main()
