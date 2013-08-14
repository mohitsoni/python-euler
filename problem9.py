#!/usr/bin/env python
import itertools

def isTriple(a,b,c):
    assert a < b < c

    return (c*c == a*a + b*b)


def isTripleSum(a,b,c,sum):
    t = isTriple(a,b,c)
    tsum = (a+b+c)
    s = (sum == tsum)

    if t == True:
        print a,b,c,t,tsum

    return t and s

def generateTriple(sum):
    for k in itertools.count(3, step=1):
        for j in xrange(2,k):
            for i in xrange(1,j):
                if isTripleSum(i,j,k,sum) == True:
                    return (i,j,k)
                
triple = generateTriple(1000)
if triple == None:
    print 'Failed'
else:
    print reduce(lambda a,b: a*b, triple)
