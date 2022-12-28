import time
f = open("input.txt", "r")
start_time = time.time()

def signal(idx):
    return tab[idx] * idx

count = 1
value = 1
tab = [1,1]
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



print(signal(20) + signal(60) + signal(100) + signal(140) + signal(180) + signal(220))


print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))