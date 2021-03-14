import os
import sys
sys.path.append("..")

def cleanCode(lines):
    k = 1
    tagAddress = {}
    lineAddress = {}
    pos = int(0x00400000)
    final = list()
    cur_path = os.path.dirname(__file__)
    path = cur_path + '/instructions.txt'
    lines = lines.split('\n')
    with open(path, 'r') as f:
        instructions = f.read().split()
    for line in lines:
        originalLine = list(line.split('\n'))
        line = list(line.split())
        print(line)
        if(line and len(line[0]) > 1 and line[0][-1] == ':'):
            tag = line[0][:-1]
            tagAddress[tag] = pos
        if not line or line[0] == '#' or line[0][0] == '.' or (line[0] not in instructions):
            pass
        else:
            tmp = ' '.join(originalLine)
            ans = tmp.split("#", 1)
            final.append(ans[0].split())
            lineAddress[k] = pos
            k+= 1
            pos += 4
    print(tagAddress, lineAddress, sep='\n')
    return [final, tagAddress, lineAddress]
