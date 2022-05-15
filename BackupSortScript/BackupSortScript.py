
import os
# определение текущей рабочей директории
path = "C:/test"

DirAndTime = dict()

# чтение записей
with os.scandir(path) as listOfEntries:  
    for entry in listOfEntries:
        # печать всех записей, являющихся файлами
        if entry.is_file():
            tempPath = os.path.abspath(entry.name)
            print(tempPath)
            tempTime = os.path.getctime(tempPath)
            print(tempTime)
            tempDirAndTime = {tempPath: tempTime}
            print(tempDirAndTime)
            #DirAndTime={tempDirAndTime}
print(DirAndTime)
