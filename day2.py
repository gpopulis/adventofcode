from collections import Counter

list = []

with open('C:\AoC\Day2-1.txt','r') as inFile:
	for line in inFile.readlines():
		list.append(line.rstrip('\n'))

def countLine(input):
    dupes = 0
    trips = 0
    for i in input:
        counter = Counter(i)
        if sum(1 for c in counter.values() if 3 > c >= 2) > 0:
            dupes += 1
        if sum(1 for c in counter.values() if 4 > c >= 3) > 0:
            trips += 1

    print dupes, trips, dupes*trips


def findBox(input):
        match = []
        for i in range(len(input)):
                a=input[i]
                for k in range(i+1,len(input)):
                        counter=0
                        common = ''
                        b=input[k]
                        for x,y in zip(a,b):
                                if x==y:
                                        common+=x
                                else:
                                        counter+=1
                        if counter==1:
                                match.append(input[i])
                                match.append(input[k])
                                match.append(common)
        print match

countLine(list)
findBox(list)
