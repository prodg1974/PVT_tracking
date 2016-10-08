import pandas as pd
import sys
import sqlite3
import hashlib
def getHeader(fname):
    """ returns the first line of filename
    Args:
         A valid path to a file
    """
    with open(fname,'r') as f:
        header=f.readline()
        f.close
        return header


def checksum(blob):
    """ Returns checksum of passed text. Uses hashlib md5
    Args:
        item to be hashed
    """
    hash_obj = hashlib.md5(blob)
    return hash_obj.hexdigest()
