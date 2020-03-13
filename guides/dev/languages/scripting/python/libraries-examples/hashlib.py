import hashlib
hasher = hashlib.md5()
with open('hashme.txt', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(hasher.hexdigest())