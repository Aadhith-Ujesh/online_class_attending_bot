from datetime import datetime

def sche():
    day = datetime.today().weekday()
    print(datetime.today().weekday())
    schedule = []
    if(day == 0):
        k = "monday.txt"
    elif(day == 1):
        k = "tuesday.txt"
    elif(day == 2):
        k = "wednesday.txt"
    elif(day == 3):
        k = "thursday.txt"
    elif(day == 4):
        k = "friday.txt"
    
    with open(k, "r") as file:
        data = file.readlines()
        for line in data:
            word = line.split("=")
            print(word)
            j = word[0]
            j = j.strip()
            word[0] = j
            k = word[1]
            k = k.strip()
            word[1] = k
            m = word[2]
            m = m.strip()
            word[2] = m
            schedule.append(word)
            print(schedule)
    return schedule

sche()