import time
f = open("input.txt", "r")
start_time = time.time()

def isContained(line):
    tab = line.split(",")
    sect1 = tab[0].split("-")
    sect2 = tab[1].split("-")

    if(int(sect1[0]) <= int(sect2[0]) and int(sect1[1]) >= int(sect2[0])):
        return 1
    elif(int(sect2[0]) <= int(sect1[0]) and int(sect2[1]) >= int(sect1[0])):
        return 1

    return 0

intResult = 0
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")

    intResult += isContained(line)


print(intResult)
print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))