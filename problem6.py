#!/usr/bin/env python

'''
Idea:
(a+b+c)^2 - a^2+b^2+c^2 = 2(ab+bc+ca)
This is generalized for n variables.

One can reduce the number of calculations using above observation.

In problem's context, we have to deal with a sequence of first n numbers.
So, from 1 .. n, we need to sum the product of a number i with all i+1 .. n numbers. And, in the end, we need to double it.

This solution is blazing fast!
'''

N = 100

sum = 0
for i in range(1, N+1):
    for j in range(i+1, N+1):
        sum = sum + i*j

sum = 2 * sum
print 'Sum:' + str(sum)
