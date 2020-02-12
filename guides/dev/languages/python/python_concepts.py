# python concepts

# basic terminal input
# read from system.in
input("input")
# params
sys.args


# data types
# convert
int()
str()
float()


# strings
strName.upper()
strName.lower()


# lists
list = [1, 2, 5, 4, 3]
list.append(6)
list.sort(key=int, reverse=True)
for i in list[1:-1]:
    print(i)


# functional methods
result = map(func, list)
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)

# unpack items
## unpack lists
unpackedList = *list
## unpack dict keywords
unpackedDict = **dict

# lambda expressions, small anonymous func
def make_incrementor(n):
    return lambda x: x + n

#python annotions, similar to javadoc comments, linters dont like
def kinetic_energy(m:'in KG', v:'in M/S')->'Joules':
    return 1/2*m*v**2
kinetic_energy.__annotations__
# {'return': 'Joules', 'v': 'in M/S', 'm': 'in KG'}

# low level
# decimal -> ASCII 
char = chr(num)
# ASCII -> decimal 
dec = ord(char)

#Perform bitwise XOR operation on two strings> ----------------
def sxor(s1,s2):    
    # convert strings to a list of character pair tuples
    # go through each tuple, converting them to ASCII code (ord)
    # perform exclusive or on the ASCII code
    # then convert the result back to ASCII (chr)
    # merge the resulting array of characters as a string
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(s1,s2))


# regex
# A regular expression or regex for short is a way of searching text
# for a pattern. 
import re
html = """
<html>
<head>
    <title>Regex Demo</title>
</head>
<body>
    <div class='firstDiv'>Hello</div>
    <div class='secondDiv'>Hello</div>
</body>
</html>
"""
#Match class names
pattern = "class='(.*)'"
#arr of matches
if re.findall(pattern, html):
    print("Found match!")
data = re.findall(pattern, text)
#Print the first match
print(data[0]) 


# itertools library
# get all combinations of elements
import itertools
# list, numOfElemToInclude, only works on even num of integers
list(itertools.combinations(alist, len(alist)))
list(itertools.chain.from_iterable(itertools.combinations(alist, r) for r in range(len(alist)+1)))

# get all permutations
perms = list(itertools.permutations(aList))
