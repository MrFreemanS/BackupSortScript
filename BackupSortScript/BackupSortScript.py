
import shutil
import os
import time
import datetime

#source dir
startpath = "C:/test"
#target dir
dstpath = "C:/dstTest"

DayDir="C:/Day"

#create dict for all files in source dir
DirAndTime = dict()

now = time.time()
dt_now = datetime.datetime.fromtimestamp(now)
SingleDay=86400
SingleMonth=2629743
SingleYear=31556926


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
        #dt_c = datetime.datetime.fromtimestamp(value)
       # if dt_c.month == 12 and dt_c.day == 31:
        print (value)
        #if (dt_c.day & dt_c.month & dt_c.year) == (dt_now.day & dt_now.month & dt_now.year) : 
         #   print (dt_c)
        #if dt_c.day == 28 :
         #   print (dt_c)
        #if
        
        #if (value-now)<=SingleDay:
            
        

        
        if (now-value)<=SingleDay:
            shutil.move(key,DayDir)
            print(now-value)
                   
            



            




goToDir(startpath)



print(now)
print (dt_now.day)
YearSort()
