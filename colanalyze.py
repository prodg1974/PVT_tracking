#import pandas as pd

def showunique(pds,topx):
    topuniques = pds.value_counts().head(topx)
    return topuniques
def countuniques(pds):
    numuniques=pds.nunique()
    return numuniques

