"""Performs globbing functions
"""
import glob

def scantarget(directory, filemask):
    """Builds lists of files
       Args: directory -- directory or directories in [] format
             filemask -- one or more masks for filenames
    """
    filelist = []
    #print dir + "/" + mask
    for curdir in directory:
        for mask in filemask:
            for name in glob.glob(curdir + "/" + mask):
                filelist.append(name)
    return filelist
#for retval in scanTarget([".", "../"], ["*.txt", "*.py"]):
#    print retval
