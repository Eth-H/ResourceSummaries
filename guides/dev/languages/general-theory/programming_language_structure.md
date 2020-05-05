# langauge by group
    interpretation
        python
    compilation
        Just-in-time compilation
            java
    dynamicly or statically typed         
        dynamicly (type checking at run time)
            python, perl, ruby, php, js
        static (type of variable is known at compile time)
            java, c, go

# building blocks
    type system
        rule set that assigns type to various constructs of computer program 
        compiler automated type system
            more rules imposed by the compiler cause a strongly typed langauge
            adv
                compile time optimisation
                safety: detect invalid code, stronger typing = more safety

        programmer specified type system
            adv
                abstract types from bianry data, making it easier for programmers to think higher level
                types serve as documentation verifying intent
        type checking
            verifying and enforcing type constrainsts
            static
                occurs at compile time, analysis source
                depending on strength of typing
                    optimisation and smaller binary size (skip runtime checks if program safe)
                generally uses some dynamic checking for its features

            dynamic
                occurs at runtime
                link runtime obj to type tag
                    can use type to dynamic dispatch, late binding, downcasting, reflection 
        polymorphism and types
            code can act of values of multiple types, or different instances of same data structure to contain elements of different types
            re-use code
            duck typing
                mtd called on an obj doesnt rely on its declared type, only that the obj supplies implementation of mtd called at runtime




# elements
    decision
        if/else 
        case
        teritray operator
    loop
        control flow
            for
            for each
            while
        iterator
        recursion
    functional
        stream methods
            map, filter, reduce, sort
        list comprehensions (python)
        functional interface
            lambda expression implement/instantiate

    data structure
        [datastructures and algorithms](./algorithms.txt)

    standard lib
        os/system features
        data
            json
            csv
            yaml
            database
                sql
        math 
        http

# features
    var ownership
        static (tied to class (noy obj))
        top level (EG main())
    OOP
        encapsulation
            access modifiers
        polymorphism
            mtd overloading (same name, different param)
            mtd overriding (child mtd overload parents)

        constructor
        obj
        inheritance
        interfaces and abstract classes
            default mtds
        mixins
        generics

    functional
        first class functions: can be assigned to a variable, passed into another function, or returned from another function
        higher order functions: take a func as an arg or return a func

        anouymous func
            no name func
            are declared before they are called (unlike normal funcs)
            define func expressions
                var outName = function (name){consolg.log(name);}
            Immediately Invoked Function Expressions (IIFE)
                (function (name) {console.log(name);})("Tom") 
        lambda expressions
            lambda: a func that is passed into another func or returned from one
            EG with java functional interfaces
            can name in some languages
        func params
        tail calls
            callbacks
                funcs are slipped/passed into another func to decide the invocation of that function
    others
        docs
        packaging
        cli tool
            compiler, interpreter
            package manager
