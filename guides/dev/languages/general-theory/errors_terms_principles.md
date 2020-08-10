# general terms
    function: stand alone section of code to be run
        mtd()
    mtd: a func that belongs to a class
        staticclass.mtd()
        objInstance.mtd()

# concepts
## Example errors
    Misspelled variable/function, unclosed parentheses/brackets/braces/quotes, mixed useage of single and double quotes, assigment operator rather then equality operator,
	forgeting opening nad closing parenthesis after a function call, paramters the wrong way, index[0] mistakes espically in for loops, (reinitializing or not, variables in loops),
	no terminal condition leads to infinate loops 
				
## Terminology
### functional programming
    in functional programming, changing or altering things is called mutation, and the outcome is called a side effect
    pure function: does not cause any side effects
    arity: Number of arguments a function requires
    Refactor: Rewrite code
    Currying a function: to convert the function of N arity into N functions of arity 1
        -(restructures a function so it takes one argument, then returns another function that takes the next argument),
        useful if you can't supply all the arguments to a function at one time
    partial application: applying a few arguments to a function at a time and returning another function that is applied to more arguments.
        
## principles
    Don't change things in functions (mutation)
    Declare dependencies explicitly (pass needed variables and don't depend on global variables)
