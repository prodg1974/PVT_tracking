"""From configuration database
"""
#import pandas as pd
import sqlite3
import hashlib
import sys
cn = sqlite3.connect('data/tracking')
#cur = cn.cursor()
cn.row_factory = sqlite3.Row
def getSQLData(fname):
    


    cur=cn.cursor()

    cur.execute('select f1.fieldname, f1.column_num as infile_index, f2.fieldname,f2.column_num as outfile_index from fields f1, fields f2, fieldMaps where fieldMaps.from_FieldID = f1.id and fieldMaps.to_FieldID = f2.id;')
    for row in cur:
            print (row["infile_index"], row["outfile_index"])

    
    cur.close()
    cn.close()

def getheader(fname):
    """ returns the first line of filename
   Args:
         A valid path to a file
    """
    with open(fname, 'r') as myfile:
        header = myfile.readline()
        #myfile.close
        return header


def checksum(blob):
    """ Returns checksum of passed text. Uses hashlib md5
    Args:
        item to be hashed
    """
    hash_obj = hashlib.md5(blob)
    return hash_obj.hexdigest()

getSQLData('tracking')
