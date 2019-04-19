import string

with open('C:\AoC\Day5.txt','r') as inFile:
    original = inFile.read()
remTable = []
alphabet = string.ascii_lowercase
#original = 'dabAcCaCBAcCcaDA'

def reducePolymer(input):
    for i in range(len(input))[:-1]:
        a = input[i]
        b = input[i+1]
        if (a == b.lower() and a!=b) or (b == a.lower() and b!=a):
            pattern = str(a)+str(b)
            remTable.append(pattern)
    for r in remTable:
        input = input.replace(str(r),'')
    retLength = len(input)
    return input,retLength

for x in range(len(alphabet)):
    input = original
    input = input.replace(str(alphabet[x]),'')
    input = input.replace(alphabet[x].upper(),'')
    length = len(input)
    retLength = -1
    while length!=retLength:
        length = retLength
        input, retLength = reducePolymer(input)
    print alphabet[x], len(input)
    
#    for i in range(len(input))[:-1]:
#        a = input[i]
#        b = input[i+1]
#        if (a == b.lower() and a!=b) or (b == a.lower() and b!=a):
#            pattern = str(a)+str(b)
#            input = input.replace(str(r),'')
#            remTable.append(pattern)
#    for r in remTable:
#        input = input.replace(str(r),'')
