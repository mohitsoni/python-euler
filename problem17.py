#!/usr/bin/env python
nwords = dict()
nwords[1] = 'one'
nwords[2] = 'two'
nwords[3] = 'three'
nwords[4] = 'four'
nwords[5] = 'five'
nwords[6] = 'six'
nwords[7] = 'seven'
nwords[8] = 'eight'
nwords[9] = 'nine'
nwords[10] = 'ten'
nwords[11] = 'eleven'
nwords[12] = 'twelve'
nwords[13] = 'thirteen'
nwords[14] = 'fourteen'
nwords[15] = 'fifteen'
nwords[16] = 'sixteen'
nwords[17] = 'seventeen'
nwords[18] = 'eighteen'
nwords[19] = 'nineteen'
nwords[20] = 'twenty'
nwords[30] = 'thirty'
nwords[40] = 'fourty'
nwords[50] = 'fifty'
nwords[60] = 'sixty'
nwords[70] = 'seventy'
nwords[80] = 'eighty'
nwords[90] = 'ninty'
nwords[100] = 'hundred'
nwords[1000] = 'onethousand'

def toWord(n):
    if n <= 20:
        return nwords[n]
    elif n < 100:
        tens = n / 10
        tens = tens * 10
        ones = n % 10
        word = str(nwords[tens])

        if ones != 0:
            word = word + str(nwords[n%tens])
        return word
    elif n >= 100 and n < 1000:
        hundred = n / 100
        word = str(nwords[hundred])
        word = word + str(nwords[100])
        rest = n % 100
        if rest != 0:
            word = word + 'and' + toWord(rest)
        return word
    elif n >= 1000:
        # TODO: Implement later for higher numbers
        return str(nwords[n])

letter_count = 0
for n in range(1,1001):
    letter_count += len(toWord(n))

print letter_count
