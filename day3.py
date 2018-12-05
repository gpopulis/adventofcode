import os
import numpy as np

list=[]
with open('C:\AoC\Day3.txt','r') as inFile:
    for line in inFile.readlines():
        list.append(line.rstrip('\n'))

nOverlaps=[]
z = np.zeros((1200,1200),dtype=int)
for l in list:
    cID = int(l.split(' ')[0].lstrip('#'))
    Left = int(l.split(' ')[2].split(',')[0])
    Top = int(l.split(' ')[2].split(',')[1].rstrip(':'))
    W = int(l.split(' ')[3].split('x')[0])
    H = int(l.split(' ')[3].split('x')[1])
    print cID, Left, Top, W, H
    temp = np.zeros((1200,1200),dtype=int)
    tempOnes = np.ones((H,W),dtype=int)
    temp[Top:Top+H,Left:Left+W]=tempOnes
    z+=temp

#check for overlaps
for l in list:
    cID = int(l.split(' ')[0].lstrip('#'))
    Left = int(l.split(' ')[2].split(',')[0])
    Top = int(l.split(' ')[2].split(',')[1].rstrip(':'))
    W = int(l.split(' ')[3].split('x')[0])
    H = int(l.split(' ')[3].split('x')[1])
    print cID, Left, Top, W, H
    temp = np.zeros((1200,1200),dtype=int)
    tempOnes = np.ones((H,W),dtype=int)
    temp[Top:Top+H,Left:Left+W]=tempOnes
    if np.array_equal(temp[Top:Top+H,Left:Left+W],z[Top:Top+H,Left:Left+W]):
        nOverlaps.append(cID)

print (z>1).sum()
print nOverlaps
