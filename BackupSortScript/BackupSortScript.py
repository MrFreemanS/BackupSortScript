
import shutil
import os
import time
import datetime

#source dir
startpath = "C:/test"
#target dir
dstpath = "C:/dstTest"
#путь для дневных бекапов
DayDir="C:/Day"

WeekDir="C:/Week"
#create dict for all files in source dir
DirAndTime = dict()

#Время в настоящий момент в юникс
now = time.time()
temp2=round(now)

#перевод юникс в нормаль
dt_now = datetime.datetime.fromtimestamp(now)
# Юникс время за 1 день
SingleDay=86400
# Юникс время за 1 месяц
SingleMonth=2629743
# Юникс время за 1 год
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
        dt_c = datetime.datetime.fromtimestamp(value)
        if dt_c.month == 12 and dt_c.day == 31:
          print (dt_c)
        
      
def DaySort():
    for key, value in DirAndTime.items():
        if (now-value)<=SingleDay:     # Сравнение разницы времени в реалтайм со временем создания файла с временем на 1 день в юникс формате
            shutil.move(key,DayDir)  # Перемещение файла в папку дневные отчеты "Day"


def WeekSort():
    for key, value in DirAndTime.items():
        temp1=round(value)
        print(temp2-temp1)
        if  ((now-value) >=580775) & ((now-value) <= 753695) : 
            shutil.move(key,WeekDir)  # Перемещение файла в папку недельные отчеты "Week"
            # Сравнение разницы времени в реалтайм  времени создания файла с временем на 7 Дней в юникс формате
          # Перемещение файла в папку недельные отчеты "Week"
          
         


goToDir(startpath)

YearSort()
DaySort() # Вызов функции 
WeekSort()

# Пофиксить баг в случае, когда дневной файл он же недельный, в случае переноса, а не копирования , перенесется только один
#