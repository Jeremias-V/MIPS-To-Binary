import os

def getOpcodes():
    opcodes = dict()
    cur_path = os.path.dirname(__file__)
    path = cur_path + 'Instructions/RType.txt'
    with open(path, 'r') as f:
        instructions = f.read().split('\n')
    for i in instructions:
        currentIns = i.split()
        opcodes[currentIns[0]] = currentIns[1]
    return opcodes
