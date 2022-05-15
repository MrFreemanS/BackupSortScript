import os
from tempfile import tempdir
import tempfile
startpath = "C:/test"

DirAndTime = dict()

def goToDir(dirpath):
    with os.scandir(dirpath) as listOfEntries:  
        for entry in listOfEntries:
            if entry.is_file():
                tempPath = os.path.abspath(entry.path)
                #print(tempPath)
                tempTime = os.path.getctime(tempPath)
                #print(tempTime)            
                tempDirAndTime = {tempPath: tempTime}
                #print(tempDirAndTime)
                DirAndTime.update(tempDirAndTime)


gotodir(startpath)
print(DirAndTime)
