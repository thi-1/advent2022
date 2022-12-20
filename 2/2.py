f = open("input.txt", "r")

dicWin = {
    "X":-1,
    "Y":0,
    "Z":1
}

dicPoints = {
    "X": 1,
    "A": 1,
    "Y": 2,
    "B": 2,
    "Z": 3,
    "C": 3
}

lstPoints = [1,2,3]

def computePoints(a, b):
    a = dicPoints[a]
    index = a-1+dicWin[b]
    if(index>2):
        index = 0
    b = lstPoints[index]

    if(a == b):
        return 3 + b
    if((a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1)):
        return 6 + b
        
    return b


total = 0
while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","").split(" ")

    total += computePoints(line[0],line[1])

print(total)

