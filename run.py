from scheduleparser import *
import datetime
from bot import *
from screenrecord import *
import time

schedule = sche()
for i in range(len(schedule)):
    now = datetime.datetime.now()
    cur = now.strftime("%H:%M")
    arr1 = cur.split(":")
    arr1 = list(map(int,arr1))
    t1 = (arr1[0]*3600) + (arr1[1]*60)

    arr2 = schedule[i][0].split(":")
    arr2 = list(map(int,arr2))
    t2 = (arr2[0]*3600) + (arr2[1]*60)

    arr3 = schedule[i][2].split(":")
    arr3 = list(map(int,arr3))
    t3 = (arr3[0]*3600) + (arr3[1]*60)

    print("current time:",t1,arr1)
    print("class time:",t2,arr2)
    print(t2-t1)
    if(t2>t1 or t2<t3):
        if(t2>t1):
            time.sleep(t2-t1)
        driver = extension()
        attender(schedule[i][1],driver,t3)
        driver.close()
        driver.quit() 
    else:
        continue
