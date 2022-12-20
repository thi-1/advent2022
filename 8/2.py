import time
import numpy as np
f = open("input.txt", "r")
start_time = time.time()

def getScenicScoreOneAxis(lst):
    score = 1
    for (i, val) in enumerate(lst):
        if i==0 or i == len(lst)-1:
            continue
        if int(val) < int(lst[0]):
            score += 1
        else:
            break
    return score

def feedArr(tp):
    arr = tp[0]
    arr2 = tp[1]
    for (idxLine, line) in enumerate(arr):
        for (idxCol, val) in enumerate(line):
            arr2[idxLine,idxCol] *= getScenicScoreOneAxis(line[idxCol:])
    arr = np.rot90(arr,k=1,axes=(1,0))
    arr2 = np.rot90(arr2,k=1,axes=(1,0))
    return (arr, arr2)

lstLines = []
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")
    lstLines.append(list(line))

arr = np.array(lstLines)
arr2 = np.ones(arr.shape)
tp = (arr, arr2)

tp = feedArr(tp)
print(tp[1])
tp = feedArr(tp)
print(tp[1])
tp = feedArr(tp)
print(tp[1])
tp = feedArr(tp)

# for line in arr2:
#     for val in line:
#         print(val)
#     break

print(tp[1])
print(np.max(tp[1]))

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))