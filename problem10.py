#!/usr/bin/env python

def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}  

    # The running integer that's checked for primeness
    q = 2  

    while True:
        
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            # 
            yield q        
            D[q * q] = [q]
            
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next 
            # multiples of its witnesses to prepare for larger
            # numbers
            # 
          
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            
            del D[q]

        q += 1

pg = gen_primes()

sum = 0
limit = 2 * 1000 * 1000
#limit = 10
for i in pg:
    if (i >= limit):
        break
    sum = sum + i

print 'Sum: ', sum
