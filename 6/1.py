import time
import numpy as np
f = open("input.txt", "r")
start_time = time.time()

line = f.readline()
line = line.replace("\n","")

intCount = 0
for (index, letter) in enumerate(line):
    setQuatre = {line[index+3], line[index+2], line[index+1], line[index]}

    if len(setQuatre) == 4:
        break

print(line[index] + line[index+1] + line[index+2] + line[index+3])
print(index+4)

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))