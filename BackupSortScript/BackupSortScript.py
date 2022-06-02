import shutil,os,time,datetime

#SRC DIR
#startpath = os.path.abspath(os.curdir)

#DST DIR
#DayDir=startpath+"\Day"
#WeekDir=startpath+"\Week"
#MonthDir=startpath+"\Month"
#YearDir=startpath+"\Year"


#dirsfortest
startpath = "E:/Backups/"
DayDir="E:/Backups/Day"
WeekDir="E:/Backups/Week"
MonthDir="E:/Backups/Month"
YearDir="E:/Backups/Year"

#create dict for all files in source dir
DirAndTime = dict()

#dict for remove files that were not selected
markedForRemoval = dict()

#now time in UNIX timestamp
now = time.time()

#Single day in seconds
SingleDay=86400

#collect data about files in dictionary
def ScanAllDirs(dirpath):
    if not os.path.exists(dirpath):
        print("DST DIR NOT EXISTS")
        exit()
    #go around files and dirs
    with os.scandir(dirpath) as listOfEntries:  
        #key for dict is abs path like a D:/test
        #value is file creation time in UNIX timestamp
        for entry in listOfEntries:
            if entry.is_file():
                tempPath = os.path.abspath(entry.path)
                tempTime = os.path.getmtime(tempPath)
                tempDirAndTime = {tempPath: tempTime}
                DirAndTime.update(tempDirAndTime)
            if entry.is_dir():
                tempPath = os.path.abspath(entry.path)
                ScanAllDirs(tempPath) #RECURSION!
 
#Analog ScanAllDirs but without RECURSION
#for remove files
def ScanSRCDir(dirpath):
    if not os.path.exists(dirpath):
        print("DST DIR NOT EXISTS")
        exit()
    #go around files and dirs
    with os.scandir(dirpath) as listOfEntries:  
        #key for dict is abs path like a D:/test
        #value is file creation time in UNIX timestamp
        for entry in listOfEntries:
            if entry.is_file():
                tempPath = os.path.abspath(entry.path)
                tempTime = os.path.getmtime(tempPath)
                tempDirAndTime = {tempPath: tempTime}
                markedForRemoval.update(tempDirAndTime)

def YearSort():
    for key, value in DirAndTime.items():
        dt_c = datetime.datetime.fromtimestamp(value)
        if dt_c.month == 12 and dt_c.day == 31:
            MovingFiles(key,YearDir)

def DaySort():
    for key, value in DirAndTime.items():
        if (now-value)<=SingleDay:   
            MovingFiles(key,DayDir)

def WeekSort():
    for key, value in DirAndTime.items():
        if  ((now-value) >=86400) & ((now-value) <= 604800) : 
            MovingFiles(key,WeekDir)

def MonthSort():
    #convert UNIX time stamp to datatime
    dt_now = datetime.datetime.fromtimestamp(now)

    for key, value in DirAndTime.items():
        dt_c = datetime.datetime.fromtimestamp(value)
        #if selected file date is 25th day of this month and this year
        if dt_c.day == 25 and dt_c.year == dt_now.year:
            MovingFiles(key,MonthDir)

def DeleteSRCDir():
    #scan start path and delete them all
    ScanSRCDir(startpath)
    for key, value in markedForRemoval.items():
        os.remove(key)


def MovingFiles(key,dstdir):
    pathName = os.path.basename(key)
    try:
        shutil.move(key,dstdir)
        print (key + " to " + dstdir)
    except:
        return


ScanAllDirs(startpath)

if not os.path.exists(YearDir):
    os.mkdir(YearDir)

if not os.path.exists(DayDir):
    os.mkdir(DayDir)

if not os.path.exists(WeekDir):
    os.mkdir(WeekDir)

if not os.path.exists(MonthDir):
    os.mkdir(MonthDir)


WeekSort()
DaySort()


ScanAllDirs(startpath)

YearSort()
MonthSort()

DeleteSRCDir()