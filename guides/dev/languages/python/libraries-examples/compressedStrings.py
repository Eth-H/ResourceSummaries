#Decompress strings> ---------------------------------------

import gzip
from StringIO import StringIO
data = "encrypted gzip string"
#Convert string to a file and the decompress
content = gzip.GzipFile(fileobj=StringIO(data)).read()
print(content)
