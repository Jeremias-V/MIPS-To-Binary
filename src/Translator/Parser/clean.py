import os

def cleanCode(lines):
    final = list()
    cur_path = os.path.dirname(__file__)
    path = cur_path + '/instructions.txt'
    lines = lines.split('\n')
    with open(path, 'r') as f:
        instructions = f.read().split()
    for line in lines:
        originalLine = list(line.split('\n'))
        line = list(line.split())
        if not line or line[0] == '#' or line[0][0] == '.' or (line[0] not in instructions):
            pass
        else:
            tmp = ' '.join(originalLine)
            ans = tmp.split("#", 1)
            final.append(ans[0].split())
    return final
