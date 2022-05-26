import shutil,os,time,datetime

#SRC DIR
#startpath = os.path.abspath(os.curdir)

#DST DIR
#DayDir=startpath+"\Day"
#WeekDir=startpath+"\Week"
#MonthDir=startpath+"\Month"
#YearDir=startpath+"\Year"


#dirsfortest
startpath = "C:/test"
DayDir="C:/test/Day"
WeekDir="C:/test/Week"
MonthDir="C:/test/Month"
YearDir="C:/test/Year"

#create dict for all files in source dir
DirAndTime = dict()

#now time in UNIX timestamp
now = time.time()

#Single day in seconds
SingleDay=86400

#collect data about files in dictionary
def goToDir(dirpath):

    #go around files and dirs
    with os.scandir(dirpath) as listOfEntries:  
        #key for dict is abs path like a D:/test
        #value is file creation time in UNIX timestamp
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
              shutil.move(key,YearDir)
              #DirAndTime.pop(key)


def DaySort():
    for key, value in DirAndTime.items():
        if (now-value)<=SingleDay:     
                shutil.move(key,DayDir)
                #dict.pop(key)


def WeekSort():
    for key, value in DirAndTime.items():
        if  ((now-value) >=580775) & ((now-value) <= 753695) : 
            shutil.move(key,WeekDir)
            #dict.pop(key)

def MonthSort():
    #convert UNIX time stamp to datatime
    dt_now = datetime.datetime.fromtimestamp(now)

    for key, value in DirAndTime.items():
        dt_c = datetime.datetime.fromtimestamp(value)
        if dt_c.day == 25 and dt_c.year == dt_now.year:
            if os.path.exists(MonthDir):
                shutil.move(key,MonthDir)
                #dict.pop(key)
            else:
                os.mkdir(MonthDir)
                shutil.move(key,MonthDir)
               # dict.pop(key)



goToDir(startpath)


if not os.path.exists(YearDir):
    os.mkdir(YearDir)

YearSort()

if not os.path.exists(DayDir):
    os.mkdir(DayDir)

DaySort()

if not os.path.exists(WeekDir):
    os.mkdir(WeekDir)
WeekSort()

if not os.path.exists(MonthDir):
    os.mkdir(MonthDir)

MonthSort()