f = open("input.txt", "r")

lstVal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

intResult = 0
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")

    sli1 = slice(0,int(len(line)/2))
    sli2 = slice(int(len(line)/2),len(line))
    firstComp = line[sli1]
    lastComp = line[sli2]
    for letter in lastComp:
        if letter in firstComp:
            break

    intResult += lstVal.index(letter)+1


print(intResult)