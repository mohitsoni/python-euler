#!/usr/bin/env python

N = 20

divisors = range(1, N+1)
print 'Calculating smallest multiple for divisors:'
print divisors

num = N

while True or num <= 0:
    num = num + 1
    flag = True
    if num % 100000 == 0:
        print num
    for i in divisors:
        flag = (num % i == 0)
        if flag == False:
            break

    if flag == True:
        break

print 'Smallest multiple: ' + str(num)
