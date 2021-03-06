import os

def getRegisters():
    registers = dict()
    cur_path = os.path.dirname(__file__)
    path = cur_path + '/Instructions/Registers.txt'
    with open(path, 'r') as f:
        instructions = f.read().split('\n')
    for i in instructions:
        currentIns = i.split()
        registers[currentIns[1]] = currentIns[0]
    return registers
