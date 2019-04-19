import numpy as np

list=[]
maxX = 0
maxY = 0


#with open('C:\AoC\Day6.txt','r') as inFile:
#    for line in inFile.readlines():
#        list.append(line.rstrip('\n'))
list = ['1, 1', '1, 6', '8, 3', '3, 4', '5, 5', '8, 9']
def getCoords(value):
    x = int(value.split(',')[0])
    y = int(value.split(',')[1].strip(' '))
    return x,y

for i,value in enumerate(list):
    pID = i
    x, y = getCoords(value)
    if x > maxX:
        maxX = x
    if y > maxY:
        maxY = y
map = np.zeros((maxY+1,maxX+1))


for i,value in enumerate(list):
    x,y = getCoords(value)
    print i, x, y
    map[y,x] = i
    print map[y,x]
print map

#print maxX, maxY
    
