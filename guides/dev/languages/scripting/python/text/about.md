# meta
    general purpose, dynamic, high-level
    interpreted: debugging
    expressive syntax: readable
    cross-platform/portable
    opensource
    language integration and extension: generally C C++

    high-level data structures
    simple syntax,dynamic typing,interpreted: fits scripting and rapid application development

# 2 vs 3
    py2
        print "word"
        raw_input("") //only string
        implicit string type is ASCII
        xrange() //returns java-like obj
    py3
        print("word")
        input("") //guess type (though can cast)
        implicit string type is unicode
        range() //returns list
        need to use as in exception handling

# identifier naming
    first char alphabet or underscore
    All chars except first may be an alphabet of lower-case(a-z), upper-case (A-Z), underscore or digit (0-9)
    no white-space or special character (!, @, #, %, ^, &, *)
    avoid keywords defined in the language
    EG : a123, _n, n_9, etc.
    EG: 1a, n%4, n 9, etc.

# tokens
    puncutation, reserved words, individual statements
## keywords
    True	False	None	and	as
    asset	def	class	continue	break
    else	finally	elif	del	except
    global	for	if	from	import
    raise	try	or	return	pass
    nonlocal	in	not	is	lambda
## identifiers
## literals
    data given in a var or constant
    ./data_types.md
## operators
### arithmetic
    + - / *
    % //remainder
    ** exponent
    // //florr division
### comparison
    == != <= >= > <
### assignment
    = += -= *= %= **= //=
### bitwise
    & (binary and) 	If both the bits at the same place in two operands are 1, then 1 is copied to the result. Otherwise, 0 is copied.
    | (binary or) 	The resulting bit will be 0 if both the bits are zero otherwise the resulting bit will be 1.
    ^ (binary xor) 	The resulting bit will be 1 if both the bits are different otherwise the resulting bit will be 0.
    ~ (negation) 	It calculates the negation of each bit of the operand, i.e., if the bit is 0, the resulting bit will be 1 and vice versa.
    << (left shift) 	The left operand value is moved left by the number of bits present in the right operand.
    >> (right shift)

### logical
    and or not
### membership
    in
    not in
### Identity Operators
    is
    not is



