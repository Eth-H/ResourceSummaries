# notes

usual unix symbol signs

regex/patturn (ptn): within / / usual regex symbols, cmd letters lose their meaning
## how
    matching lines put into the patturn space for processing
    files/stdout processed line by line in a pattern space buffer
    the other buffer is called the hold space

# stuff
## substitution flags
    d: del
    p: print line
    w [file]: output to file
    n: The numbered instance of pattern match in the line to substitute
    g: Run substitution on all instances of pattern match (instead of just first)
## cmds
    $: Last line
    n: Read next line into pattern space
    N: Appends next line into the pattern space (creating a multi-line pattern space)
    :[name] : Create a label
    b[label]: Branch, or jump, to a label
    !: invert an addresses match
    h: Copy ptn space to hold space
    H: Append ptn space to hold space
    g: Copy hold space to ptn space
    G: Append hold space to ptn space
## ptn symbols
    & — References the text matched by the pattern
    \([regex]\) — Mark pattern for referencing
    \1, \2, \3… — Reference marked pattern

# examples
```bash
    #-n: suppres auto printing of patturn space
        sed {}?... "query"
        # where [x] is any value of set x, and ? means previous option may/maynot be present, | means or
            #ptn addressing query: "/[query]/[anotherCmd | subFlag]"
            #line addressing query: "[num1][rangeSpecifier][num2][subFlag]"
            #substitution ptn query: "[lines]?s/[patturnToMatch]/[subFlag]"


    sed ‘1,2d’ //del lines 1 to 2
    sed -n 1,5p [file] # print lines 1 to 5
    sed -n ‘1~2p’ # print 1st line and every 2nd line onwards
    sed ‘$d’ # del last line
    # append cmd to patturn
    sed -n ‘/multi/s/-line/\ line/’ # swap multi-line with multi line
    # chain expressions, -e or ;
    sed -n ‘/multi/s/-line/\ line/;s/text/&less/’ # after 1st expr, text -> textless
    #reference matched patterns using parenthesis
    sed 's/\(text\) \(file\)/\2 \1/' test.txt # swap "file" with "text"
    sed '/^#\|^$/d' [file]
    # :a create label "a", N add nextline to patturn space, $!ba return flow to label a if not the last line
    sed ':a;N;$!ba;s/\n/, /g' test.txt  # swap newlines with ", "
    # multi line match
    sed ‘/start/,/end/’ test.txt #match line as selection beginning and match final line
    # substitution
        sed ‘s/term/replacement/flag’
        sed ‘s/y/Y/g’
        # special chars (file globbing chars) need to be escapped
        sed 's/and/\&/g;s/^I/You/g'
        sed '2s/l/?/g' # Replace all 'l's with '?' on the 2nd line
    # replace a line
        #note: sed -i is not posix standard
        sed '[targetLineNumber] cnewline [textToReplaceWith]' [fileName] 
        sed -i '[targetLineNumber]/.*/[replacementLine]/' file.txt		
        sed -i 'Ns/.*/replacement-line/' file.txt
        awk '{ if (NR == 4) print "different"; else print $0}' input_file.txt > output_file.txt
        awk 'NR==4 {$0="different"} 1' input_file.txt
        awk 'NR==4 {$0="different"} { print }' input_file.txt
```
