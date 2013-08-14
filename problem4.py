#!/usr/bin/env python

def isNumPalindrome(n):
    nstr = list(str(n))
    for n in nstr:
        if n != nstr.pop():
            return False

    return True

lookup = {}
palindromes = []
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        multiple = sorted((i, j))
        multiple = str(multiple)
        processed = multiple in lookup.keys()
        
        if processed != None and processed == True:
            # Already processed and is multiple is not a palindrome
            continue
        val = i * j
        palindrome = isNumPalindrome(val)
        if palindrome == True:
            palindromes.append(val)
            lookup[multiple] = True

palindromes = sorted(palindromes)
print palindromes[len(palindromes) - 1]
