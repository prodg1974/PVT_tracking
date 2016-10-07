import pandas as pd
import sys
import sqlite3
import hashlib
def readHeader(fname):
    with open(fname,'r') as f:
        header=f.readline()
        f.close
        return header
def checksum(blob):
    hash_obj = hashlib.md5(blob)
    return hash_obj.hexdigest()
