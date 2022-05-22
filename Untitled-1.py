# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.


def IsPrime(num):
    for n in range(2, int(num**0.5) + 1):
        if num % n == 0:
            return False
    return True


def SumOfPrimes(num):
    a_set = set()
    for i in range(num):
        if IsPrime(i):
            a_set.add(i)
    return sum(a_set) - 1
