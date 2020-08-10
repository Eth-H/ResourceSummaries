# get file type (via magic bytes)
    file [file]

# convert files
    to convert html to text:
        lynx -dump -stdin
    many formats
        pandoc inpF --from [filetype] --to [filetype] outF
        EG
    pandoc README.md --from markdown --to docx -o temp.docx

# handle different file formats
    xmlstarlet #xml
    jq  #JSON
    jid and jiq #JSON, interactive use
    shyaml #YAML
    csvkit pkg: in2csv, csvcut, csvjoin, csvgrep #Excel, CSV
    binary files
        hd, hexdump, xxd #hex dumps 
        bvi, hexedit, biew #binary editing
        strings #extract strings
        xdelta3 #binary diffs
    iconv, uconv #convert text/unicode encodings
        #EG
            # Displays hex codes or actual names of characters (useful for debugging):
            uconv -f utf-8 -t utf-8 -x '::Any-Hex;' < input.txt
            uconv -f utf-8 -t utf-8 -x '::Any-Name;' < input.txt
            # Lowercase and removes all accents (by expanding and dropping them):
            uconv -f utf-8 -t utf-8 -x '::Any-Lower; ::Any-NFD; [:Nonspacing Mark:] >; ::Any-NFC;' < input.txt > output.txt


