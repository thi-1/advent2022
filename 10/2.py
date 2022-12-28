import time
f = open("input.txt", "r")
start_time = time.time()


def printLine(idx):
    str = ""
    for i in range(idx-39,idx):
        if tab[i-1] == i%40 or tab[i] == i%40 or tab[i+1] == i%40:
            str += "#"
        else:
            str += "."
    print(str)
    pass

count = 1
value = 1
tab = [0,1]
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")
    lstLine = line.split(" ")


    if lstLine[0] == "noop":
        count += 1
    else:
        tab.append(value)
        value += int(lstLine[1])

    tab.append(value)


for x in range(1,6):
    printLine(x*40)

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))