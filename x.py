import polling 
#So Far So Good
header==polling.getHeader('./test.txt')
hash=polling.checksum(header)
print hash

