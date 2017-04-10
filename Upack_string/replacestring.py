#   Назначение: Замена строк в тех блоке на строку с переводом

fileTranslated = 'TranslatedFileDialog.txt'
fileToTransl = 'outP.txt'
fileOriginal = 'Dialog.txt'

#   Считывание из файла из пути
def readFile(filename):
    data = []
    infile = open(filename, 'r', encoding='UTF8')
    for line in infile:
        line = line.rstrip()
        data.append(line)
    return data

def readFileP(filename):
    data = []
    infile = open(filename, 'r', encoding='UTF8')
    for line in infile:
        line = line.replace('\r', '')
        line = line.replace('\n', '')
        data.append(line)
    return data

def isSameSize(position, orig, string):
    i = position
    size = 0
    while (orig[i] != '\"' or orig[i+1] != ','):
        size+=1
        i+=1
    i-=1
    while (orig[i] == ' '):
        size-=1
        i-=1
    if (size == len(string)):
        return True
    else:
        return False

def HaveRightPrefix(position, data):
    if (data[(position - len("\"name\":\"left\",\"value\":\"")):position] == "\"name\":\"left\",\"value\":\""):
        return True
    elif (data[(position - len("\"name\":\"right\",\"value\":\"")):position] == "\"name\":\"right\",\"value\":\""):
        return True
    elif (data[(position - len("\"name\":\"top\",\"value\":\"")):position] == "\"name\":\"top\",\"value\":\""):
        return True
    return False


dataOriginal = readFileP(fileOriginal)
dataTransl = readFile(fileTranslated)
dataToTransl = readFile(fileToTransl)
dataResult = []

j = 0
while (j < len(dataToTransl)):
    i = 0
    while (i < len(dataOriginal)):
        position = dataToTransl[j].find(dataOriginal[i])
        if ((position > 0) and isSameSize(position, dataToTransl[j], dataOriginal[i])):
            if HaveRightPrefix(position, dataToTransl[j]):
                dataToTransl[j] = dataToTransl[j].replace(dataOriginal[i], dataTransl[i])
        i+=1
    dataToTransl[j] +='\n'
    j+=1

outfile = open("Dialogresult.txt", 'w', encoding="UTF8")
outfile.writelines(dataToTransl)