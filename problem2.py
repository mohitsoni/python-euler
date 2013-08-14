#!/usr/bin/env python

def fib_sum(ub):
    a = 1
    b = 2
    
    num = [b]
    next = 0
    while (next < ub):
        next = a + b
        a = b
        b = next
        if (next < ub and next % 2 == 0):
            num.append(next)

    return num

print sum(fib_sum(4 * 1000 * 1000))
