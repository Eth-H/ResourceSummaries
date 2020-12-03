# vars
    x=y=z=50
    a,b,c=5,10,15

# data types
Numbers,String,List,Tuple,Dictionary
    type(var)
None 
    //compare to none
    "x" is None
## cast
    int()
    str()
    float()
    bool()
        0, "", [], {}, () evaluate to false
# decision
    if expression 1:   
        # block of statements   
      
    elif expression 2:   
        # block of statements   
    else:   
        # block of statements  
    //use like ? ternary operator
        "yay!" if 0 > 1 else "nay!"
# iteration
## for
    //based off for each
    for iterating_var in sequence:
        statement(s)
    //typical counting loop
    for i in range(10):
        # do
    //get index and item
        for i, value in enumerate(animals):
            print(i, value)

## while
    while expression:  
        statements  
    while i<=5:  
        print(i)  
        i=i+1;  
## break continue pass
    break //skip entire loop
    continue //skip current loop iteration
    pass /null operation, fill a space without an executable statement
    // carry out else after full loop, or break out prematurelly
        for i in range(0,5):  
            print(i)  
            break
        else: print("for loop completely exhausted, since there is no break."); 
## iterable
obj that knows how to create a iterator
state is saved while traversing
    our_iterable = {"a": 2, "b": 2}
    our_iterator = iter(our_iterable)
    next(our_iterator)


## basic data structures 
### tuple
//immutable
    tuple=(true,1,2,'d')
    tuple1(20,) //must have comma if one item, otherwise int
    //unpack tuples into vars
        a, b, c = (1, 2, 3); d, e, f = 4, 5, 6 
        //extended unpacking
        a, *b, c = (1, 2, 3, 4)

### lists
    list = [1, 2, 5, 4, 3]; list2=[1,2,3]
    list[-1] //access indexes from reverse end
    list+list2; list*list2
    list1<list2
    //slice
        for i in list[1:-1]:
            print(i)
        li = [1,2,4,3]
            li[1:3]   # Return list from index 1 to 3 => [2, 4]
            li[2:]    # Return list starting from index 2 => [4, 3]
            li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
            li[::2]   # Return list selecting every second entry => [1, 4]
            li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
        # Make a one layer deep copy using slices
        li2 = li[:]

#### funcs
    cmp(list1, list2)
    len(list)
    max(list); min(list)
    list(seq)
#### mtds
    list.mtd()
    //add/rm/change
        append(6)
        remove(0)
        insert(index, obj)
        pop(obj=list[-1]) //rm last elem
    clear()
    count(obj)
    extend(seq)
    index(obj)
    reverse()
    sort(key=int, reverse=True)
### set
contents must be immutable
//unordered (no index), no duplciates
    set1 = {a,b}
    set2 = set([a, b])
    set2.add(c)
    set2.discard(b) //wont throw an err if item doesnt exist (like remove)
    //union
        set1|set2
        set1.union(set2)
    //intersect
        set1&set2
        set1.intersection(set2) //returns new set with intersections
        set1.intersection_update(set2, set3) //rm items from set not in both the other sets
    //diff
        set1-set2
        set1.difference(set2)
    //immutable set
        frozenset([1,2,3,4,5])
#### mtds
    Issubset(....) another set contains this set
    Issuperset(....) this set contains anouther set
    //applicable mtds from list
        pop() remove(item)
// make a one layer deep copy
    filled_set = some_set.copy()

### dictionary
    dict={'name':'charlie','id':100,'dept':'it'}
    dict.keys()
    dict.values()
    dict.items() //key-val pairs as a tuple
    dict.has_key(key)
        dict.update(dict2)
    dict[key]
        dict.get(key); //avoid KeyError for non-existing keys
        dict.get(key, backUpKey); //get default if missing keys
    del dict[key]
//keys must be immutable
    invalid_dict = {[1,2,3]: "123"}  # => Raises a TypeError: unhashable type: 'list'
    valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.
// Check for existence of keys in a dictionary with "in"
    "one" in filled_dict  # => True


### array
contiguous mem locations
fixed size
holds one data type
    import array
    //arrayName = array(typecode, [initializers])
    a = array('i', [2, 4, 6, 8])
    a[0] = 10
    a[2:5] = array('i', [4, 6, 8])
    del a[2]


# strings
str = "abcde"
//strs immutable, hence invalid
    str[0] = "z"
r"x" //ignore escape chars and other special chars special meaning
## formatting
    print("int %d\n float %f\n str %s"%(Integer,Float,String));
    name = 10
    print(f"She said her name is {name}.")
    print("She said her name is {}.".format(name))

## mtds
    str.mtd(args...)
    //case
        upper()
        lower()
        capitalize()
        swapcase()
    //codec
        encode("codec") //default utf-8
        decode("utf-8","strict")
    expandtabs(tabsize = 8)
    //find
        startswith(str,beg=0,end=len(str))
        endswith(suffix ,begin=0,end=len(string))
        find(substring ,beginIndex, endIndex)
        index(subsring, beginIndex, endIndex) //find(), throw except if not found
    //check, if no chars most return false
        isalnum() //alphanumeric
        isalpha() //alphabet
        isdecimal(); isdigit()
        isidentifier()
        islower(); isupper()
        isspace()
    len(string)
    join(seq) //merge strs
    strip() //rm whitespace from start and end
    //pad
        ljust(width[,fillchar]) //pad from left with fillchar
        zfill(width) //pad from left with zeros
    replace(old,new[,count])
    //separator
        partition(separator) //return separator and strs on its left and right
        split(str,num=string.count(str))
        splitlines(num=string.count('\n'))
    //r prefixable mtds, prefix with r to work from reverse direction
        rsplit rstrip rpartition rjust rfind rindex
    //l prefixable mtds, prefix with l to work from left direction (if default is both directions)
        lstrip()

# functions
    func(a,b,c):
        print(a+b+c)
    func(a,b,c) //required/positional args
    func(c="C",b="B",a="A") //keyword args, any order passing
    func(a, c="C",b="B") // pass one in order, cannot have positional args after a keyword arg
    //default args
    func(a,b,c="C"): 
        print(a+b+c)
    func(a,b) //if dont pass default val used
    func(a,b,c)
    //variable num args
    func(*args):
        print(len(args))
    //variable num key args
    func(**kwargs):
    func(big="foot", loch="ness")

    //expand tuples and kwargs
        args = (1, 2, 3, 4)
        kwargs = {"a": 3, "b": 4}
        all_the_args(*args)            # equivalent to all_the_args(1, 2, 3, 4)
        all_the_args(**kwargs)         # equivalent to all_the_args(a=3, b=4)
        all_the_args(*args, **kwargs)  # equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)

    //set a global scope
        def set_global_x(num):
            global x 

    //first class func
        def create_adder(x):
            def adder(y):
                return x + y
            return adder
        add_10 = create_adder(10)
        add_10(3)   # => 13


## lambda 
    python doesnt have lambda arrow syntax
    lambda args : expression
    can pass to functional interface mtds
    //anonymous
        (lambda x: x > 2)(3)                  # => True
        (lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

### built in higher order funcs / functional mtds
    List = {1,2,3,4,10,123,22}  
    list(filter(lambda x:(x%3 == 0),List))
    list(map(lambda x:x*3,List))
       
    result = map(func, list)
    numbers = (1, 2, 3, 4)
    result = map(lambda x: x + x, numbers)

### list/dict/set comprehensions
    [add_10(i) for i in [1, 2, 3]] //map
    [x for x in "iterable" if x==5] //filter
    {x for x in 'abcddeef' if x not in 'abc'}  # => {'d', 'e', 'f'}
    {x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# files
    file = open(fileName, accessMode)
    //read mtds
        file.read(size) //read strings
        file.next() //read next line
        file.readline(size) //read line and mv fp (file pointer) to begining of new line
        file.readlines() //read until EOF, store as list
    //write mtds
        file.write(str) //write str
        file.writelines(seq) //write seq strs
    file.close()
    //exe block of statements with file and then close it
    with open(fileName, accessMode) as filePointer:  
        #do stuff
    //get byte fp is at
    file.tell()
    //move file pointer
        //offset: new pos (num bytes to mv); from: reference to mv from, 0-beginning,1-current,2-end
        //file.seek(offset,from)
        file.seek(10)

# os module
    import os
    os.rename("file2.txt","file3.txt")
    os.remove("file3.txt")
    os.mkdir("new")
    //change current working dir
    os.chdir("new")
    //get cwd
    os.getcwd()
    os.rmdir("new")
## using subproccess module
    exe script and write output
    import subprocess  
    with open("output.txt", "wb") as f:  
        subprocess.check_call(["python", "file.py"], stdout=f)  
    //name of imported os module (relative to system family)
    //'posix', 'nt', 'os2', 'ce', 'java' and 'riscos'
        os.name
    os.error
        //raises OSError in case of invalid or inaccessible file names and path
            try:   
                f = open(filename, 'rU')   
            except IOError:
            print(os.error) //<class 'OSError'>
    os.popen()
        opens a file to/from cmd given and it returns file obj connected to a pipe
    os.close()
        func closes the associated file with descriptor fd
    os.access()
        check users permissions for certain file
        //exists
        os.access("Python.txt", os.F_OK)
        //r/w/x permissions access
        os.access("Python.txt", os.R_OK)
        os.access("Python.txt", os.W_OK)
        os.access("Python.txt", os.X_OK)


# modules
    import module1,module2 //import a whole module/file as obj in separate namespaces
    import module1 as md1 //shorten the idenfifier to the separate namespace obj
    from module-name import name1,name2 //import specific module names into current namespace
    from module import * //above for all attributes
    import module1 as specificName
    //list of defined names
    dir(module)
    //reload imported module to exe top level code (though module not actually reloaded)
    reload(module)

## packages
    hierarcal structure of pkgs, sub-pkgs, modules, sub-modules
    put __init__.py in top-level pkg dir
    define import statements for all modules in __init__.py
    EG dir structure
        pkg
            __init__.py
                from module1 import name1
                from module2 import name2
            module1.py
            module2.py
            subpkg
                __init__.py
                module3.py
### use pkg
    //via __init.py__
        import pkg
        pkg.name1Item
        pkg.name2Item
    //manually
        from pkg.module1 import name1,name2 //add brackets for a multi-line list
        from pkg.subpkg.module2 import name1
        from pkg.subpkg import module3
            module3.name3

# exceptions
    try:  
        #block of code   
    except Exception1,Exception2:  
        print("err")
    else: 
        print("no exception occured")
    finally:
        print("always run regardless")
    //custom extension
        try:    
            raise ErrorInCode(errCode)
        except ErrorInCode as ae:    
            print("Received error:", ae.data)

# unpack items 
TODO
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
## mtd
    re.mtd(...)
    match: returns true if match found
    search: returns the match obj if found
        span(): tuple with start/end pos of match
        string(): string passed
        group(): matched string part
    findall: returns list of matches
    split: returns list of string items split by each match
    sub: replace >=1 matches
## supported chars
    [] \ (special seqs) . ^ $ * + {} | ()
    "[a-z]" "\r" "Ja.v." "^Java" "point" "hello*" "hello+" "java{2}" "java|point"
## supported special sequences
    \A \b \B \d \D \s \S \w \W \Z


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

# time/date
    import time;
    time.time() //since 12 AM, 1st January 1970 (unix epoch)
    time.localtime(time.time()) //time tuple
    print(time.asctime(time.localtime(time.time()))) //formatted time
    //tmp stop exe
        time.sleep(1)
    import datetime;
    //current dateime obj
    datetime.datetime.now()
    //custom datetime objs
    datetime.datetime(datetime.datetime.now().year(),12,10)

## cal dates
    import calendar;  
    cal = calendar.month(2018,12) //month
    calendar.prcal(2019) //whole year

# math
    import math
    Pie(n): 3.141592653589793
    Euler's number(e): 2.718281828459045
    math.log(math.fabs(number), 10)) //natural log to base e
    math.log10(x)
    math.exp(number)-1
    math.sqrt(x)
    math.expm1(number) //e^x -1
    angle=math.radians(angleInDegree)
    math.cos(angle)
    math.sin(angle)
    math.tan(angle)
## stats
    import statistics
    data = [5, 2, 7, 4, 2, 6, 8]
    statistics.mean(data)
    statistics.median(data)
    statistics.mode(data)
    statistics.stdev(data)
    statistics.median_low(data)
    statistics.median_high(data)

# send mail
    import smtplib
    host="gmail.com"; port=587; sender=sender@gmail.com; receiver: receiver@gmail.com
    smtpObj = smtplib.SMTP(host, port, local_hostname)
    smtpobj.login(sender,password)
    smtpObj.sendmail(sender, receiver, message)

    //if sending html at email top include
        MIME-Version:1.0 
        Content-type:text/html 

# more astract data structures
## collection module
    from collections import collectionName
    namedtuple()
        tuple refered to via name instead of index
        Point = namedtuple('Point', 'x y')
        pt1 = Point(1.0, 5.0)
        pt2 = Point(2.5, 1.5)
    OrderedDict()
        preserves the order in which the keys are inserted
        so iterating will give a specifc order
    defaultdict()
        takes first param as default dict type
        number = defaultdict(int)    
        number['one'] //=0
    Counter()
        each unique item in list mapped to its count
        helps count hashable objs
        List = [1,2,4,7,5,1,6,7,6,9,1]    
        c = Counter(list)    
    deque()
        double-ended queue
        list = ["x","y","z"]  
        deq = deque(list)
## queue
    import queue
    qu = queue.Queue(maxsize=10)
    //insert data at end
        qu.put(9)
    //takes data from head
        print(qu.get())


# random
    random.random() //0.0 to 1.0
    random.randint(lb, ub)
    random.randrange(start,stop,step)
    random.choice(seq)
    random.shuffle(list) //randomly reorder

# sys module
manipulate python runtime env
    import sys
    sys.modules //improted modules
    sys.argv //cli args
    sys.base_prefix
    sys.base_exec_prefix
    sys.byteorder //native byteorder, EG little (from little endian)
    sys.maxsize //largest int, generally 2**63
    sys.path //PYTHONPATH
    sys.stdin
    sys.getrefcount(obj)
    sys.exit //exit python
    sys.executable //absolute path to py executable
    sys.platform //platform, EG linux

# basic terminal iteraction
    # read from system.in
    input("input")
## params
    # params
    sys.argv
### getopt
    import getopt  
    import sys  
    argv = sys.argv[1:]  
    try:  
        opts, args = getopt.getopt(argv, 'hm:d', ['help', 'my_file='])  
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:  
        print('idk')  
        print 'test.py -i inputfile -o outputfile
### argparse
### docopt
    from docopt import docopt  
    args = docopt(__doc__, version='Example 1')
### fire
    import fire
    class Python(object):  
        def hello(self):  
            print("Hello")  
            def openfile(self, filename):  
                print("Open file '" + filename + "'")
    if __name__ == '__main__':  
        fire.Fire(Python)   

# magic/dunder/special mtds/attributes
attributes used by python that live in user controlled namespaces
built-in classes define magic mtds
    __init__(self)
        called by newly instialised class after __new__
        constructor for intialises instance vars / attributes
    __del__(self) //deconstructor
    obj.__str__() //get str repersentation of obj and reurn as str obj
    obj.__repr__() //get str repersentation of obj and returns machine-readable
    obj.__len__() //obj length
    obj.__call__()
    obj.__bytes__() //obj byte str repersentation
    __ge__  //>=
    __le__ //<=
    __neg__ //unary operator
    __ipow__ //exponents
    _nonzero_ //bool val of obj
    __name__
    __main__

# class
    class Human:
        # class attribute
        species = "H. sapiens"
    # constructor
    def __init__(self, name):
        self.name = name
        self._age = 0
    # instance mtd, take cls instance as param (need to create one to pass)
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # class method, shared among all instances
    # called with the calling class as the first argument
    @classmethod
    def get_num_legs(human):
        return human.legNum
    #Human.get_num_legs() #or Human.get_num_legs(Human)

    # static mtd, called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # getter, though little use
    @property
    def age(self):
        return self._age

    # setter
    @age.setter
    def age(self, age):
        self._age = age

    # deller
    @age.deleter
    def age(self):
        del self._age

# class inheritance
    class Superhero(Human):
        species = 'Superhuman'
    //parent contructor auto inherited with its params
    def __init__(self, name, movie=False, superpowers=["super strength", "bulletproofing"]):
        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # call parents overriden mtds
        super().__init__(name)
    sup = Superhero(name="Tick")
    print(Superhero.__mro__) //get class inheritance chain
    print(sup.get_species()) //calls parent mtd with own class attribute

# decorators
inject/modify code in funcs/classes
    def foo(): pass
    foo = staticmethod(foo)
    //=
    @staticmethod
    def foo(): pass

    //decorator retuned obj must be useable as a func
        //classes used as decorators must implement __call__(self)
        //funcs can just return nested funcs
    //order: decorator.__init__() run -> once func called decorator.__call__() instead
    //EG
        class myDecorator(object):
            def __init__(self, f):
                print "inside myDecorator.__init__()"
                f() # call original func
                f(*args,**kwargs) # use if you dont know num args

            def __call__(self):
                print "inside myDecorator.__call__()"
        @myDecorator
        def func():
            print "inside func"
        //func is compiled and passed to the decorator

        def outer_div(f):  
            def inner(x,y):  
                if(x<y):  
                   x,y = y,x  
                  return f(x,y)  
             return inner  
        # syntax of generator  
        @outer_div  
        def divide(x,y):  
             print(x/y)  

    built in class decorators
        @classmethod and @staticmethod //define class mtds not connected to any instance of a class
        @property //allows to treat class mtd as an attribute
    nest/stack
        @function1  
        @function2  
        func...
    args
        @repeat(num=5)
    stateful decorators
        //keep track of state, generally suits classes as they are useful to maintain state
        import functools  
        class Count_Calls:  
        def __init__(self, func):  
        functools.update_wrapper(self, func)  
        self.func = func  
        self.num_calls = 0  
        def __call__(self, *args, **kwargs):  
        self.num_calls += 1  
        print(f"Call{self.num_calls} of {self.func.__name__!r}")  
        return self.func(*args, **kwargs)  
          
# generator function
    funcs that return traversal obj used to create iterators
        allow for controlled exe via successive func calls
    if no value found in iteration, it raises StopIteration exception
    can use to optimise mem
    def simple():  
    for i in range(10):  
        if(i%2==0):  
            //pause func by saving states and yielding to caller, resumes when succesvie func called
             yield i  
    //successive func call
    for i in simple():  
        print(i)
    //succesively call via chaining .next()
    obj=simple()
    print(simple.next())  //py exes obj.__next__()
    
    //create without user-defined func
    //lambda func -> anonymous func, generator expr -> anonymous generator func
        a = (x**3 for x in list)
    //pipeline generators
        with open('sells.log') as file:  
        burger_col = (line[3] for line in file)  per_hour = (int(x) for x in burger_col if x != 'N/A')  


# working with data
## json
    data as name/value pairs: obj, record, dict, hash table, keyed/associative list
    values as ordered list: arr,vector,list,seq
### serialization (py objs to json objs)
        dict->obj,list/tuple->arr,str->string,int/float->Number,True/False->true/false,None->null

    import json
    //store serialized data to json file
        json.dump(obj,write_file)
    //store serialized data within python file (as a str)
        str = json.dumps(obj)
    //clean dict
        json.dumps(per_dict, indent = 5, sort_keys= True)
### deserializing
    //load and deserialize file
    with open("data.json", "r") as read_file:  
        json.load(read_file)  
    //deserialize json string
        json.loads(json_str)
