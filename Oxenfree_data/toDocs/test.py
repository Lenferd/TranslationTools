import re

from Modules.FilesOperation import readFile
from Modules.FilesOperation import writeFile

data = readFile.read_file_rstrip("res2.txt")
outdata = []

i = 0

templine = ''
while i < len(data):
    if re.search(r"^[' ']*[A-Z][A-Z]+[' ']*[A-Z]+[' ']*$", data[i]) is not None:
        if templine == '':
            templine = data[i] + '\t'
        else:
            outdata.append(templine)
            templine = data[i] + '\t'
        i += 1
    else:
        if templine == '':
            templine += '\t'
        templine += data[i]
        i += 1
        outdata.append(templine)
        templine = ''

writeFile.write_list(outdata, 'res2WithoutNames2')