import time
import numpy as np
f = open("input.txt", "r")
start_time = time.time()

def viewOneAxis(arr,arr2):
    for (idxLine, line) in enumerate(arr):
        minLine = 0
        for (idxCol, val) in enumerate(line):
            if (int(val) > minLine or idxCol == 0):
                arr2[idxLine,idxCol] = 1
                minLine = int(val)
            if minLine == 9:
                break
    arr = np.rot90(arr,k=1,axes=(1,0))
    arr2 = np.rot90(arr2,k=1,axes=(1,0))
    return (arr,arr2)

lstLines = []
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")
    lstLines.append(list(line))

arr = np.array(lstLines)
arr2 = np.zeros(arr.shape)
tp = (arr,arr2)

tp = viewOneAxis(tp[0],tp[1])
tp = viewOneAxis(tp[0],tp[1])
tp = viewOneAxis(tp[0],tp[1])
tp = viewOneAxis(tp[0],tp[1])

print(np.sum(tp[1]))

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))