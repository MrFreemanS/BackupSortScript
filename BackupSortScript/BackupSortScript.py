import os
import time
import datetime

#source dir
startpath = "C:/test"
#target dir
dstpath = "C:/dstTest"

#create dict for all files in source dir
DirAndTime = dict()

#collect data about files in dictionary
def goToDir(dirpath):
    #go around files
    with os.scandir(dirpath) as listOfEntries:  
        for entry in listOfEntries:
            if entry.is_file():
                tempPath = os.path.abspath(entry.path)
                tempTime = os.path.getctime(tempPath)
                tempDirAndTime = {tempPath: tempTime}
                DirAndTime.update(tempDirAndTime)
            if entry.is_dir():
                tempPath = os.path.abspath(entry.path)
                goToDir(tempPath)


def YearSort():
    for key, value in DirAndTime.items():
        dt_c = datetime.datetime.fromtimestamp(value)
        if dt_c.month == 12 and dt_c.day == 31:
            print(dt_c)

goToDir(startpath)

now = time.time()
YearSort()