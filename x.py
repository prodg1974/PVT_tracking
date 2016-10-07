import fileIO

header=fileIO.readHeader('./test.txt')
hash=fileIO.checksum(header)
print hash

