"""Functions for finding documents from configuration database
"""
#import pandas as pd
import sqlite3
import hashlib
import sys


def getheader(fname):
    """ returns the first line of filename
   Args:
         A valid path to a file
    """
    with open(fname, 'r',encoding='utf-8') as myfile:
        header = myfile.readline().encode('utf-8')
        #myfile.close
        return header


def checksum(blob):
    """ Returns checksum of passed text. Uses hashlib md5
    Args:
        item to be hashed
    """
    hash_obj = hashlib.md5(blob)
    return hash_obj.hexdigest()
