f = open("input.txt", "r")

max = 0
current = 0
while True:
    line = f.readline()
    if not line:
        break
    if line == "\n":
        current = 0
        continue

    line = int(line.replace("\n", ""))

    if line > 0:
        current += line

    if current > max:
        max = current

print(max)