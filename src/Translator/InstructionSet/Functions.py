import os

def getFunctions():
    functions = dict()
    cur_path = os.path.dirname(__file__)
    path = cur_path + '/Instructions/Functions.txt'
    with open(path, 'r') as f:
        instructions = f.read().split('\n')
    for i in instructions:
        currentIns = i.split()
        functions[currentIns[0]] = currentIns[1]
    return functions
