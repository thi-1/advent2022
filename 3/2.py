import time
f = open("input.txt", "r")
start_time = time.time()

lstVal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getBadge(tab):
    lstCommon = []
    for letter in tab[1]:
        if letter in tab[0]:
            lstCommon.append(letter)

    for letter in lstCommon:
        if letter in tab[2]:
            return letter

    return "&"

tab = []
count = 1
intResult = 0
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")
    tab.append(line)

    if(count < 3):
        count+=1
        continue

    badge = getBadge(tab)
    intResult += lstVal.index(badge)+1
    count = 1
    tab = []



print(intResult)
print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))