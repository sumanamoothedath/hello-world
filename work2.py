import math


def numfunc(num):
    return sum([i for i in range(1, num + 1)])


j = 0
"""j represents the jth triangle number"""
num = 0
""" num is the triangle number corresponding to j"""
count = 0
""" Sets the number of divisors for triangle number n"""

while count <= 500:

    """resets the number of divisors so as to check a new triangle number"""
    count = 0
    j += 1
    """every triangle number such as the first,second etc are passed through this by adding 1"""
    num = numfunc(j)
    """set num as the next triangle number"""

    """checks and counts the number of divisors"""
    i = 1
    while i <= math.sqrt(num):
        """finds the square root of the current sum """
        if num % i == 0:
            count += 1
            """counts the number of divisors"""

        i += 1

    """since a number from 1 to the square root holds exactly the half of the divisors"""
    """We multiply it twice to get the other half and thus the full set of divisors"""
    count *= 2

print("the first triangle number to have over 500 divisors is:")
print(num)
print("the number of divisors:")
print(count)
print("and it occurs in the:")
print(j)
