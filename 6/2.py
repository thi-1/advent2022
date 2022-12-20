import time
f = open("input.txt", "r")
start_time = time.time()

line = f.readline()
line = line.replace("\n","")

for (index, letter) in enumerate(line):
    setQuatre = {line[index]}
    for val in range(14):
         setQuatre.add(line[index + val])

    if len(setQuatre) == 14:
        break

print(index+14)

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))