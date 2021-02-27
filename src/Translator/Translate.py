import sys
from sys import stdin

from Parser import clean
from InstructionSet import RType, IType, JType
from InstructionTranslations import RTranslation, ITranslation, JTranslation

itype = IType.getOpcodes()
jtype = JType.getOpcodes()
rtype = RType.getOpcodes()

def translateMIPS():
    ans = ""
    lines = clean.cleanCode(stdin.readlines())
    try:
        for l in lines:
            opcode = l[0]
            if(opcode in itype):
                translation = ITranslation.translateI(l)
                if translation != "":
                    ans += translation + '\n'
                    print(translation)
                else:
                    raise Exception
            elif(opcode in jtype and len(l) == 2):
                translation = JTranslation.translateJ(l)
                if translation != "":
                    ans += translation + '\n'
                    print(translation)
                else:
                    raise Exception
            elif(opcode in rtype):
                translation = RTranslation.translateR(l)
                if translation != "":
                    ans += translation + '\n'
                    print(translation)
                else:
                    raise Exception
            else:
                print("Invalid")
    except Exception as e:
        print("ERROR: ", e)
translateMIPS()
