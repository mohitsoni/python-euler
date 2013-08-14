#!/usr/bin/env python

def name_score(word, position):
    score = 0
    for c in word:
        score += (ord(c) - 65 + 1)
    
    score = score * position

    return score

fname = 'names.txt'

f = open(fname)

names = f.read()

f.close()

names = names.split(',')

clean_names = []

for name in names:
    clean_names.append(name[1:len(name)-1])

del(names)


sorted_names =  sorted(clean_names)

score = 0

for i in xrange(len(sorted_names)):
    score += name_score(sorted_names[i], i+1)

print score
