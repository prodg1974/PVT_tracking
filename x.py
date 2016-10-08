import fileIO
#So Far So Good
header=fileIO.readHeader('./test.txt')
hash=fileIO.checksum(header)
print hash

