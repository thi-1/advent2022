import time
import numpy as np
f = open("input.txt", "r")
start_time = time.time()

commands = {
    "U" : np.array([0,1]),
    "D" : np.array([0,-1]),
    "L" : np.array([-1,0]),
    "R" : np.array([1,0])
}
setTailPositions = {(0,0)}

def move (strCommand, headPosition, tailPosition):
    lstCommand = strCommand.split(" ")
    command = lstCommand[0]
    count = int(lstCommand[1])

    while count > 0:
        headPosition += commands[command]
        tailPosition = computeTail(headPosition, tailPosition)
        setTailPositions.add((tailPosition[0],tailPosition[1]))
        count-=1
    return (headPosition, tailPosition)

def computeTail (headPosition, tailPosition):
    diff = headPosition - tailPosition
    if(diff[0] > 1):
        tailPosition += np.array([1,diff[1]])
    elif(diff[0] < -1):
        tailPosition += np.array([-1,diff[1]])
    if(diff[1] > 1):
        tailPosition += np.array([diff[0],1])
    elif(diff[1] < -1):
        tailPosition += np.array([diff[0],-1])
    return tailPosition

headPosition = np.array([0,0])
tailPosition = np.array([0,0])
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")
    move(line, headPosition, tailPosition )

print(setTailPositions)
print(len(setTailPositions))


print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))