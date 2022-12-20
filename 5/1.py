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

    if(intCaisse == 0):
        return lstLines
    else:
        val = lstLines[idx1].pop(-1)
        lstLines[idx2].append(val)
        intCaisse-=1
        lstCommand[0]=intCaisse
        return move(lstLines, lstCommand)


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