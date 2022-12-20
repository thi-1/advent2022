f = open("input.txt", "r")

dicWin = {
    "win":6,
    "draw":3,
    "lose":0
}

dicPoints = {
    "X": 1,
    "A": 1,
    "Y": 2,
    "B": 2,
    "Z": 3,
    "C": 3
}

def computePoints(a, b):
    a = dicPoints[a]
    b = dicPoints[b]

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

