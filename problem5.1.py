#!/usr/bin/env python

def RangeLCM(first, last):
    factors = range(first, last+1)
    for i in range(0, len(factors)):
        if factors[i] != 1:
            n = first + i
            for j in range(2*n, last+1, n):
                factors[j-first] = factors[j-first] / factors[i]
    return reduce(lambda a,b: a*b, factors, 1)

def RangeLCM2(last):
    factors = range(last+1)
    print '1: ', factors
    result = 1
    for n in range(last+1):
        if factors[n] > 1:
            result *= factors[n]
            for j in range(2*n, last+1, n):
                factors[j] /= factors[n]
        print '2: ', 'n:', n, 'factors[n]:',factors[n], 'result:',result, factors
    return result

#print RangeLCM(1, 20)
print RangeLCM2(20)
