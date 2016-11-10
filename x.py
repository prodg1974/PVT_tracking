import pandas as pd
#import polling 
import colanalyze as ca
#So Far So Good
#header=polling.getheader('./test.txt')
#hash=polling.checksum(header)
#print(hash)

mydf = pd.read_csv('./data/PII/CRW_Crawford_EEFile_20160914_TEST.csv')

#print("csv:")
#print(mydf.head())
mycounts = ca.showunique(mydf.FirstName,3)
mynumuniques = ca.countuniques(mydf.FirstName)
print(mycounts)
print(mynumuniques)
