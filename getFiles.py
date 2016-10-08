import glob

def scanTarget(dir,mask):
    fileList=[]
    print dir + "/" + mask
    for name in glob.glob(dir + "/" + mask):
       fileList.append(name)
       return fileList
for retval in scanTarget(".", "*.txt"):
	print retval

	
