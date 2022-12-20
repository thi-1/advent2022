import time
import numpy as np
f = open("input.txt", "r")
start_time = time.time()

def feedPiles(lstLines):
    arr = np.array(lstLines)
    arr = np.rot90(arr,k=1,axes=(1,0))

    lstPiles = []
    for line in arr:
        if(line[0] != ' '):
            newPile = []
            for col in line:
                if(col != ' '):
                    newPile.append(col)
            lstPiles.append(newPile)
    return lstPiles

def feedCommands(line):
    line = line.replace('move ', '').replace(' from ', ' ').replace(' to ', ' ')
    return line.split(' ')

def move(lstLines, lstCommand):
    intCaisse = int(lstCommand[0])
    idx1 = int(lstCommand[1])-1
    idx2 = int(lstCommand[2])-1

    newTab = lstLines[idx1][:-intCaisse]
    newTab2 = lstLines[idx1][-intCaisse:]

    lstLines[idx1] = newTab
    lstLines[idx2].extend(newTab2)

    return lstLines


lstLines = []
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")

    lstLines.append(list(line))

lstLines = feedPiles(lstLines)

lstCommands = []
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    line = line.replace("\n","")
    
    lstCommand = feedCommands(line)
    lstLines = move(lstLines, lstCommand)

lstRet = ""
for tab in lstLines:
    lstRet+=tab[-1]

print(lstRet)

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))