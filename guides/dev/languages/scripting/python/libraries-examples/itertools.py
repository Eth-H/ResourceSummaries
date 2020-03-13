# package for iterator operations
from itertools import *
l = []

##infinate
#count
#EG count(10) --> 10 11 12 13 14 ..., 
# params(start, step)
count(l)
#cycle()
# EG cycle('ABCD') --> A B C D A B C D ... 
cycle(l)
#repeat()
# params (elem, n)
# repeat same elem
repeat()

#Iterators terminating on the shortest input sequence

#accumulate()
#p [,func]
accumulate([1,2,3,4,5]) --> 1 3 6 10 15

#chain()
chain('ABC', 'DEF') --> A B C D E F
#chain.from_iterable()
chain.from_iterable(['ABC', 'DEF']) --> A B C D E F

#compress()
compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F

#dropwhile()
#pred, seq
dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1

#filterfalse()
#pred, seq
#elements of seq where pred(elem) is false
filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8

#groupby()
iterable[, key]
#sub-iterators grouped by value of key(v)

#islice()
#seq, [start,] stop [, step]
#elements from seq[start:stop:step]
islice('ABCDEFG', 2, None) --> C D E F G

#starmap()

func, seq

func(*seq[0]), func(*seq[1]), …

starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000

#takewhile()

pred, seq

seq[0], seq[1], until pred fails

takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4

#tee()

it, n

it1, it2, … itn splits one iterator into n

#zip_longest()

p, q, …

(p[0], q[0]), (p[1], q[1]), …

zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
