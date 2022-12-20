import time
f = open("input.txt", "r")
start_time = time.time()


class Directory:
    def __init__(self, name, parentDir):
        self.name = name
        self.parentDir = parentDir
        self.lstDirs = []
        self.lstFiles = []
        self.size = 0

    def addFile(self, file):
        self.lstFiles.append(file)
        self.size += file.size
        
    def addDir(self, dir):
        self.lstDirs.append(dir)
        self.size += dir.size

    def cd(self, dirName):
        if dirName == "..":
            return self.parentDir

        for dir in self.lstDirs:
            if dir.name == dirName:
                return dir
        return None

    def toString(self, strSpace):
        strSpace += "   "
        ret = self.name + " - taille:" + str(self.size) + "\n"
        for fil in self.lstFiles:
            ret += strSpace + "- " + fil.toString() + "\n"
        for dir in self.lstDirs:
            ret += strSpace + "- " + dir.toString(strSpace)
        return ret

    def getSize(self):
        intSize = 0
        for fil in self.lstFiles:
            intSize += fil.size
        for dir in self.lstDirs:
            intSize += dir.getSize()
        self.size = intSize
        return intSize

    def getDirSizes(dir, lstSizes):
        if(dir.size < 100000):
            lstSizes.append(dir.size)
        for childDir in dir.lstDirs:
            lstSizes = childDir.getDirSizes(lstSizes)
        return lstSizes

    def getMinDelete(self, lstMin):
        if(self.size > 6552309):
            lstMin.append(self.size)
        for childDir in self.lstDirs:
            lstMin = childDir.getMinDelete(lstMin)
        return lstMin

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
    def __str__(self):
        return self.size + " " + self.name
    def toString(self):
        return str(self.size) + " " + self.name


line = f.readline()
currentDir = Directory("", None)
baseDir = currentDir

while True:
    line = f.readline()
    if not line or line == "\n":
        break
    
    line = line.replace("\n","")
    lstCommand = line.split(" ")

    if(lstCommand[0] == "$"):
        command = lstCommand[1]

        if command == "cd":
            currentDir = currentDir.cd(lstCommand[2])
            continue
        elif command == "ls":
            continue
    elif(lstCommand[0] == "dir"):
        currentDir.addDir(Directory(lstCommand[1], currentDir))
        continue
    else:
        currentDir.addFile(File(lstCommand[1], int(lstCommand[0])))
        continue

print(baseDir.getSize())
print(baseDir.toString(""))

lst = baseDir.getDirSizes([])
print(lst)
print(sum(lst))

print(min(baseDir.getMinDelete([])))

print("Process finished --- %s ms ---" % ((time.time() - start_time)*1000))