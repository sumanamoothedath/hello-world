import math


class PrimeList ():
    init_primes = [2, 3, 5, 7, 11, 13, 15, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
                   101, 103, 107, 109, 113, 127, 131, 137]

    def __init__(self, n):
        self.primes = PrimeList.init_primes
        self.extend(n)

    def extend(self, n):
        n = int(n)
        nextnum = self.primes[-1]
        while self.primes[-1] < n:
            nextnum += 2
            if self.check(nextnum):
                self.primes.append(nextnum)

    def check(self, n):
        n = int(n)
        limit = int(math.sqrt(n))
        return all((n % p for p in self.primes if p <= limit))

    def is_prime(self, n):
        n = int(n)
        self.extend(int(math.sqrt(n)))
        return self.check(n)

    def factors(self, n):
        n = int(n)
        x = n
        fact = dict()
        for p in self.primes:
            if p > x:
                break
            while x % p == 0:
                x = x / p
                fact[p] = fact.get(p, 0) + 1
        if x > 1:
            e = x if x != n else int(math.sqrt(n))
            self.extend(e)
            return self.factors(n)
        return sorted(fact.items())


def triangleNumber(n):
    # this function takes a number and finds the triangle number and returns it.
    return int((n * (n + 1)) / 2)


def init():
    myprimes = PrimeList(137)
    condition = False
    counter = 1
    divisorCount = 500
    while condition == False:
        triNumber = triangleNumber(counter)
        primeFactors = myprimes.factors(triNumber)
        prod = 1
        for i in range(0, len(primeFactors)):
            prod = prod * (primeFactors[i][1] + 1)

        if prod >= divisorCount:
            print(str(triNumber) + " is the first Triangle Number to have over " + str(
                divisorCount) + " divisors.")
            condition = True
        counter = counter + 1


if __name__ == "__main__":
    init()

