import os
import numpy as np

list = []
with open('C:\AoC\Day4.txt','r') as inFile:
    for line in inFile.readlines():
        list.append(line.rstrip('\n'))
        
list.sort()
guard = 0
Time = 0
Date = ''

def getGuard(line):
    if line[19:24] == 'Guard':
        guard = int(l.split('#')[1].split(' ')[0])
        temp = []
        return guard, temp

def getTime(line):
    Time = int(line[15:17])
    return Time
    
for l in list:
    temp = []
    timeList = []
    nDate = l[6:11]
    Time = int(l[15:17])
    
    if l[19:24] =='Guard':
        guard = int(l.split('#')[1].split(' ')[0])
    else:
        if nDate == Date:
            
        if l[19:24] =='falls':
            
        elif l[19:24] =='wakes':
            w = Time
            
        temp.append(l[6:11])
        Time = l[15:17]
        temp.append(guard)
        if l[19:24] =='falls':
            f = Time
        elif l[19:24] =='wakes':
            w = Time
        
        for i in range(60):
            if i < Time:
                t = '.'
            elif f <= i < w:
                t = '#'
            else:
                t = '.'
            timeList.append(t)
        temp.append(guard)
        temp.append(timeList)
                
            

        print temp
        #elif l[19:24 == 'wakes':
        #    state = 'w'
        #elif l[19:24] == 'falls':
        #    state = 'f'
        #else:
        #    print "something went wrong"
        #if l[19:24] == 'wakes':
        #    State = 'Wakes Up'
        #if l[19:24] == 'falls':
        #    State = 'Falls asleep'

        

