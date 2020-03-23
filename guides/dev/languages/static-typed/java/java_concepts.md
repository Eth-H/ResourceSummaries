# Constuctors  
	//same name as class
	//can have two constuctors (one needs a different num of params)
	//auto generated if not produced 
	
	public class MyClass {
	   
        private int num;
        private int width;
        private String theString;

        public MyClass(int width, String theString) {
            //attribute not passed as a param, so not used by this classes new objects
            num = 100;
            //if passing parameter to class instance with a different name, no this.
prefex needed
            newWidth = width
            this.theString = theString            
            //declare new variable
            int gaya = yaya
        }
        //second constructor has different number of parameters
        MyClass(){
            num = 100;
        }
    }

    //If class isn't present in current package import it
    import [packagePath].ExternalClass
    public class MyClass2 {
        //create external objects using the constructor
	    private ExternalClass externalObject1;
        private ExternalClass externalObject2;
	    public MyClass2(){
            //if new instance variable is the same
            externalObject1 = new ExternalClass()
	        
	    }
        //declare object outside constructor
        public void method(){
            ExternalClass localVariableExternalObject = new ExternalClass()
        } 
	}
# condition/decision 
    if(cond){
    }else if(cond){
    }else{}

    //tentiray/conditional operator
    condition ? value1 : value2
    switch (month) {
                case 1:  monthString = "January";
                         break;
                case 2:  monthString = "February";
                         break;
                default: monthString = "Invalid month";
                         break;
            }

# loops
    loopMethod(stringList){
        double total = 0;
        //equal to i<=(stringList.length-1)
        for (int i = 0; i < stringList.length; i++) {
            total += stringList[i];
        }   
        //foreach version, use to iterate entire list
        for (String stringItem: stringList){
            System.out.println(stringItem)
        }
        stringList.forEach((stringItem) -> {
                System.out.println(stringItem);
        });
        //while, iterate some of the list
            int index = 0;
            while(index < files.size()) {
                String filename = files.get(index);
                System.out.println(filename);
                index++;
            }           
    }

   
# arrays
## basic arr 
for primative data types, cant grow more than initial size
    public class ArrayClass(){
        public void static main(){  
        int arraySize = 8 
        //declare array variable, then create array and assign
        int[] intList = new int[arraySize]        
        //or
        String[] stringList = {"element0", "element2"}     
        numbers = new int[] { 
            3, 15, 4, 5
        }; 
        //accessArray
        //get last element
        system.out.println(stringList[stringList.length-1])                
        }
    }
    //iterate array 
        for(int i = 0; i < numbers.length; i++) {
            System.out.println(i + ": " + numbers[i]);
        }
       for(Iterator<Track> it = tracks.iterator(); it.hasNext(); ) {
            Track track = it.next();
            if(track.getArtist().equals(artist)) {
                it.remove();
            }
        }
## arr utility methods
generally apply to any array implementation
    list.size()
    list.get(index)
        list.indexOf(element)
    list.add(element)
        //insert at specific index, (after that index, doesnt replace)
        list.add(index, element)                
        //add all elements in a list (not as a nested list)
        list.addAll(list2); list.addAll(index, list2)
        list.set(index, element)
    list.remove(index); list.remove(element)
        list.removeAll(list2)
        list.removeRange(fromIndex, toIndex)
    list.clear()       
    list.isEmpty()
    list.clone()
    array.binarySearch(), array.fill(), array.sort()
    arrayList.toArray()
# group objects
## lists for obj (collections) 
    //using java.util.ArrayList
       import java.util.ArrayList;
        public class MusicOrganizer{
            //If java >=7 can omit the class data type and get it automatically
            private ArrayList<String> files;
            public MusicOrganizer(){
                files = new ArrayList<>();
            }
        } 

## iterate collections
    //use generic for, foreach, while loop
        
    //iterator obj, java.util.Iterator (provides sequential obj access) 
    //remove objects from list while iterating 
        Iterator<StudentLoan> it = loans.iterator();
        while(it.hasNext()){
            StudentLoan loan = it.next();
            if(loan.getName.equals(targetName){
            it.remove();
        }        

## linked list
    //vs ArrayList
        //faster, implements list and queue (ArrayList just list)
        //better for manipulating data
    import java.util.LinkedList
    LinkedList loansLl = new LinkedList();
    loansLl.add(loan);

## Hash set
    //no duplicates  
        import java.util.HashSet;
        HashSet<String> mySet = new HashSet<>();
## Hash map
    //contain pair of objects, key and value
    HashMap <String, String> contacts = new HashMap<>();
    contacts.put("Charles Nguyen", "(531) 9392 4587");
    String number = contacts.get("Lisa Jones");
    //hash map methods  
        //add
        hashMap.put(key, value);
        //get keys or values  
        hashMap.keySet()
        hashMap.values()
        hashMap.containsKey()
        hashMap.containsValue()
    //get keys that match a specific value
        for (String name: contactsList.keySet()){
            if (searchNum.equals(contactsList.get(name))){
                collectionName.add(name)
            }
        }
    //swap keys and values
        Map<String, Character> myNewHashMap = new HashMap<>();
        for(Map.Entry<Character, String> entry : myHashMap.entrySet()){
            myNewHashMap.put(entry.getValue(), entry.getKey());
        }

## store primative types in a collection
    //wrap Pt into obj,
    //type -> wrapper class: int -> Integer, float -> Float, char -> Character
    int i = 18; 
    Integer iwrap = new Integer(i);  
    int value = iwrap.intValue();
    //under the hood autoboxing and unboxing occurs
        private ArrayList<Integer> markList; 
        int firstMark = markList.remove(0);

# manipulating strings
    Object.toString();
    String.endsWith(suffix); String.startsWith(prefix);
    //remove trail and whitespace
    String.trim();
    String.toLowerCase(); String.toUpperCase();
    String.indexof(char, indexToStartAt);
    String.substring(beginIndex, endIndex)
    Sring.compareTo();
    String.length
    System.out.printf("The value of the float variable is " +
                      "%f, while the value of the integer " +
                      "variable is %d, and the string " +
                      "is %s", floatVar, intVar, stringVar);
    //convert str to charArray
    private static final char[] ALPHABET = 
                "abcdefghijklmnopqrstuvwxyz ".toCharArray();

# read from stdin (read terminal input while active)
    //Scanner, 
        import java.util.Scanner
        Scanner in = new Scanner(System.in);
        String s = in.inputLine();
        int a = in.nextInt();
        float b = in.nextFloat();
    //DataInputStream (.readline() method is depreciated)
        DataInputStream dis = new DataInputStream(System.in)
        String str = dis.readline();
    //Buffered reader
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

# enums
    //enumerated values
    //fixed number of instances
    //internal constructor needs to be private
    public enum Coin {
        ONE_PENNY(1), TWO_PENCE(2), FIVE_PENCE(5);
        private int value;
        private Coin(int value){
            this.value = value;
        }
        public int getValue(){
            return value;
        }
        public String toString(){
            switch(this){
                case ONE_PENNY:
                    return "one penny";
                case TWO_PENCE:
                    return "two pence";
                case FIVE_PENCE:
                    return "five pence";
                default:
                    return "what";
            } 
        }
    //create new object
        Coin.ONE_PENNY();
    //iterate over all values
        Coin.values();
    //use getter to access enumerated value
        Coin.getValue();

# useful libraries
## java.util.Collections 
    //sort alphanumerically
    Collections.sort(arrayList);
## java.util.Map
    //entrySet, get set view of mappings into HashMap
    Iterator it = map.entrySet().iterator();
    while (it.hasNext()) {
        Map.Entry pair = (Map.Entry)it.next();
        System.out.println(pair.getKey() + " = " + pair.getValue());
        it.remove(); // avoids a ConcurrentModificationException
    }

## Random
    import java.util.Random;
    Random rand = new Random();
    int num = rand.nextInt();
    int value = 1 + rand.nextInt(100);
    //random list index
    int index = rand.nextInt(list.size());
    //return random number within rage
    rand.nextInt((max - min) + 1) + min

## Math 
    Math.max(x, y)
    Math.min(x, y)
    Math.sqrt(64);
    //convert to absolute var (+ve)
    Math.abs(-4.7);
    Math.random();

## further generic implimencations
    //anonymous obj
        Lot furtherLot = new Lot(…);
        lots.add(furtherLot); 
        //obj immediately used, so name is unecessary
        lots.add(new Lot(…)); 
    //chaining method calls, immediatey call method on returned obj
        lot.getHighestBid().getBidder() 

# functional stuff 
## lambdas
    //anonymous methods with no associated obj, pass as param 
        (param) -> {System.out.println(param)}
        
        collection.forEach((param) -> {system.out.println(param.getName())})
        collection.forEach(param -> system.out.println(param.getName()))

## streams 
    //alternative iteration, pipeline of operations  
    //fixed order, no index as only sequential access 
    //arraylist is a stream method that creates a stream of cotents
    //pipeline list: source -> outputed stream (Os)-> Os -> ... -> terminal operation               
    //Filter: select items from the input stream to pass on to the output stream (via true/false)
        arrayList.stream().filter(obj -> obj==newObj)    
    //Map: replace items from the input stream with different items in the output stream.
        arrayList.stream().map(obj -> obj.getName()).forEach(params -> System.out.println(param))    
    //Reduce: collapse the multiple elements of the input stream into a single element
        //acc passed to next method, start = first acc 
    reduce(start, (acc, element) -> acc + element) 
    sightings.stream()
        .filter(sighting -> animal.equals(sighting.getAnimal())
        .map(sighting -> sighting.getCount())
        .reduce(0, (total, count) -> total + count); 
    sightings.removeIf(sighting -> sighting.getCount() == 0);

    //parallel stream is processed using multiple processes as quickly as
possible
    int sumOfWeights = widgets.parallelStream()
       .filter(b -> b.getColor() == RED)
       .mapToInt(b -> b.getWeight())
       .sum();
    //java convert stream
        Stream<String> tokenStream = Arrays.asList("A", "B", "C", "D").stream();	//stream
        List<String> tokenlist = tokenStream.collect(Collectors.toCollection(LinkedList::new)); 	//list

# Java data types
## terms
    integral: whole numbers, EG int
    floating point: handle fractional parts, EG float double

## Primitive Data Types
    //unsigned and sign size differences
        //(-1s are to include 0)
        //unsigned: (2^8)-1 to 255, signed: (-2^7) = -128, (2^7)-1 = 127
            //0 to 255, -128 to 127
    //sizes
        (2^16)-1 = 65535, (2^32)-1 = 4294967296, (2^64)-1 = 2*9,223,372,036,854,775,807  
 
    //byte
        //8 bit signed two's complement (TC) int, -2^7 to 2^7-1
        //save space in arrays
    //short, 16 bit signed TC int, 2^7
    //int, 32 bit signed TC int, 2^31
    //long, 64 bit signed TC, 2^63, Default value (DV) = 0L
    //float, single-precision 32-bit IEEE 754 floating point, 1 sign bit/8 bit exp/23 bit mantissa, DV = 0.0f 
    //double, double-precision 64-bit IEEE 754 floating point, 1 sign bit/ 11 bit exp/ 52 bit mantissa, DV = 0.0d  
    //boolean, 1 bit, DF = false
    //char, 16 bit unicode character, \u0000 to \uffff
    
    //null, indicates no object
    null
### literals
    //source code repersentation of a fixed value, literals are repersented straight in code as they are build into the language
    //primative types are literals

#### numreric literals
    can use _ as separator inbetween middle nums (java SE7+)
    EG: long bytes = 0b11010010_01101001_10010100_10010010;

##### int literals
    use to create: byte, short, int, long
    //use prefixes to refer to other num systems
        int normalDecimal = 100;
        int binary = 0b11010; 
        int octal = 0144; int hex =  0x64;
##### floating point literals
    use to create: float, double
    EG
        double d1 = 123.4;
        //d1 in scientific notation
        double d2 = 1.234e2;
        float f1  = 123.4f;
#### char and str literals
    may contain any Unicode (UTF-16) characters
    char literal 'a'
    str literal "a"
    EG
        "Se\u00F1or" = Sí Señor
    escape seqs
        \b (backspace), \t (tab), \n (line feed), \f (form feed), \r (carriage return), \" (double quote), \' (single quote), and \\ (backslash)

#### null literal
    cant be assigned to val of primitive type

#### class literal
    refers to obj that repersents the type itself
    typeName.class
    EG
        String.class


### convert between 
    Integer.parseInt(string);
    Integer.toString(int);
    Integer.parseLong(str);  
    //double -> float -> long -> int -> short -> byte 
        //explicit (type casting)
            double d; long l; short s; 
            long l = (long)d 
            int i = (int)d 
                byte b = (byte)i 

# oop elements
## encapsulation
    //Private elements are accessible only to objects of the same class.
    //info hiding
        //obj have different class instances -> increase level of indepedance

    //class vairables
        //owned by class and shared between class instances,
        //access via class name (className.variable)
        public static int anInt = 10;
    //constant
        final int SIZE = 10;
    //combine
        //constants good for public class variables
            public static final int BOILING_POINT = 100; 
    //class methods
        public static int getDaysThisMonth() 
        Calendar.getDaysThisMonth();
        //dis adv
            //cant access instance fields or call instance methods within their class


## inheritance keywords
    public class SubClass extends SuperClass
        public SubClass (){
            super(param)
        }
        public otherMethod(){
            super.overridenMethod()
        }
## substitution
    //subtyping
        Object v = new Vehicle();
        Vehicle v1 = new Vehicle();
        Vehicle v2 = new Car();
    //asign supertype to subtype
        Vehicle v; Car c = new Car();
        v = c; //correct
        c = v; // compile-time err
    //casting
        c = (Car) v;

# documentation
## parameterized classes
    //docs include provsion for param type, these types are placeholders 
    //EG ArrayList<E> -> .add(E e)
## comments (javadoc style)
```java
    //class
        //class name, comment summary (purpose, function), version, authors', doc for cons and methods
        /**
        * description
        * @author
        * @version
        */
        //constructor, method
            //name, return type, param (names and types), summary for method,
    //parameter and returned value
            /**
             * Read a line of text from standard input (the text
             * terminal), and return it as a set of words.
             *
             * @param  prompt  A prompt to print to screen.
             * @return A set of strings, where each String is
             *         one of the words typed by the user
             */
            public HashSet<String> getInput(String prompt) 
```
## debugging 
    //syntax err -> compiler spot them 
    //logic errors (bugs), no immediate manifestation
    //reduce chance 
        //technique like encasulation 
        //attention to cohesion, coupling 
    //imorove detection
        //practices
            //modularization (support indepdant concurrent dev, +integration), documentation
    //testing -> search for err presence 
    //debugging -> search for err source 
## Eg methods 
### unit testing
    //test each unit (method, class, module)
    //do in development 9lower costs and build test suite)
    //unit contract (what to do, find violations, +-ve tests)
    //test boundaries (zero, one, full; search empty, remove/search
one, add to full)
    //bluej, Objects of individual classes can be created. Individual methods can be invoked. Inspectors provide an up-to-date view of an object’s state.
### automate tests            
    //test framework (for automation of repetitive regression)
        //Junit: test cases (methods), test classes, assertions
(expected mtd results), fixures (support multiple tests)
//manual walkthrough
    //tabulate values of key fields and document state changes 
    //verbal walkthrough, with someone else 
//print statements
    //large output, right methods need to be documented
//debugging, use supporting tools (debuggers) 
    //bluej 
        //breakthroughs, step n step-into exe, call seq (stack), obj state 
        //peek into pipeline of operations 
            peek(s -> System.out.println(s))

//Eg projects online-shop-junit, calculator-engine
