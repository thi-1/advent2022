f = open("input.txt", "r")

max = []
current = 0
while True:
    line = f.readline()
    if not line:
        break
    if line == "\n":
        max.append(current)
        current = 0
        continue

    line = int(line.replace("\n", ""))

    if line > 0:
        current += line

max.sort(reverse=True)

print(max[0]+ max[1]+max[2])