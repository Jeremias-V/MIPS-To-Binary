import sys
from sys import stdin

from Translator.Parser import clean
from Translator.InstructionSet import RType, IType, JType
from Translator.InstructionTranslations import RTranslation, ITranslation, JTranslation
from Translator.InstructionTranslations.Complements import isTag

itype = IType.getOpcodes()
jtype = JType.getOpcodes()
rtype = RType.getOpcodes()

def translateMIPS(lines):
    tmp = clean.cleanCode(lines)
    lines = tmp[0]
    tags = tmp[1]
    address = tmp[2]
    ans = ""
    k = 1
    try:
        for l in lines:
            if len(l) == 0:
                return ""
            opcode = l[0]
            if(opcode in itype):
                if(len(l) == 4 and isTag(l[3])):
                    l[3] = str(int((tags[l[3]] - address[k])/4))
                translation = ITranslation.translateI(l)
                if translation != "":
                    ans += translation + '\n'
                else:
                    return l + " is not a valid instruction."
            elif(opcode in jtype and len(l) == 2):
                if(isTag(l[1])):
                    l[1] = str(int(tags[l[1]]/4))
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
            k += 1
    except Exception as e:
        return "ERROR: " + str(e)
    return ans
