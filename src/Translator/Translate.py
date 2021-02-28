import sys
from sys import stdin

from Translator.Parser import clean
from Translator.InstructionSet import RType, IType, JType
from Translator.InstructionTranslations import RTranslation, ITranslation, JTranslation

itype = IType.getOpcodes()
jtype = JType.getOpcodes()
rtype = RType.getOpcodes()

def translateMIPS(lines):
    lines = clean.cleanCode(lines)
    ans = ""
    try:
        for l in lines:
            if len(l) == 0:
                return ""
            opcode = l[0]
            if(opcode in itype):
                translation = ITranslation.translateI(l)
                if translation != "":
                    ans += translation + '\n'
                else:
                    return l + " is not a valid instruction."
            elif(opcode in jtype and len(l) == 2):
                translation = JTranslation.translateJ(l)
                if translation != "":
                    ans += translation + '\n'
                else:
                    return l + " is not a valid instruction."
            elif(opcode in rtype):
                translation = RTranslation.translateR(l)
                if translation != "":
                    ans += translation + '\n'
                else:
                    return l + " is not a valid instruction."
            else:
                return "INVALID"
    except Exception as e:
        return "ERROR: " + str(e)
    return ans
