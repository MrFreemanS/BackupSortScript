import shutil,os,time,datetime

#source dir
startpath = "C:/test"
DayDir="C:/Day"
WeekDir="C:/Week"
MonthDir="C:/Month"
YearDir="C:/Year"
#create dict for all files in source dir
DirAndTime = dict()

#Время в настоящий момент в юникс
now = time.time()
# Юникс время за 1 день
SingleDay=86400

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
              shutil.move(key,YearDir)
        
      
def DaySort():
    for key, value in DirAndTime.items():
        if (now-value)<=SingleDay:     # Сравнение разницы времени в реалтайм со временем создания файла с временем на 1 день в юникс формате
                shutil.move(key,DayDir)  # Перемещение файла в папку дневные отчеты "Day"


def WeekSort():
    for key, value in DirAndTime.items():
        if  ((now-value) >=580775) & ((now-value) <= 753695) : 
            shutil.move(key,WeekDir)  # Перемещение файла в папку недельные отчеты "Week"
            # Сравнение разницы времени в реалтайм  времени создания файла с временем на 7 Дней в юникс формате
          # Перемещение файла в папку недельные отчеты "Week"

def MonthSort():
    for key, value in DirAndTime.items():
        if  ((now-value) >=2417393.5280878544) & ((now-value) <= 2503552.6705605984) :
            shutil.move(key,MonthDir)  # Перемещение файла в папку недельные отчеты "Month"
            # Сравнение разницы времени в реалтайм  времени создания файла с временем на 28 Дней в юникс формате
          # Перемещение файла в папку недельные отчеты "Month" 2503552.6705605984    2417393.5280878544  вплоть до 23:59 с 00:00
        


goToDir(startpath)
YearSort()
DaySort() # Вызов функции 
WeekSort()
MonthSort()

# тоже самое с днями и месяцами