#!/usr/bin/env python
from collections import defaultdict
cache = defaultdict(int)
cache[1] = 1

def collatz(n):
    if n not in cache:
        isEven = (n % 2 == 0)
        if isEven == True:
            n = int(n / 2)
        else:
            n = 3 * n + 1
        count = 1 + collatz(n)
        cache[n] = count
    return cache[n]

million = 1000 * 1000 * 1000

longest = 0
for i in xrange(1, million + 1):
    l = collatz(i)
    if l > longest:
        longest = l
        print 'Longest length:',longest,'Number:',i
