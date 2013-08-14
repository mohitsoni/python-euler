#!/usr/bin/env python
import random
_mrpt_num_trials = 5

def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite

def factors(n):
    fnums = []

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            if is_probable_prime(i) == True:
                fnums.append(i)

    return fnums

fac = factors(600851475143)
#fac = factors(13195)
print fac
print "Greatest prime factor: " + str(fac[len(fac)-1])
