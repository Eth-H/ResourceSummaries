 open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)¶


Character Meaning
'r': open for reading (default)
'w': open for writing, truncating the file first
'x': open for exclusive creation, failing if the file already exists
'a': open for writing, appending to the end of the file if it exists

'b': binary mode
't': text mode (default)  // rt = r

'+'open for updating (reading and writing)

syntax 
    [r|w|x|a][ |+][t|b]
