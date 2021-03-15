import sys
from sys import stdin
from HexTranslator.InstructionSet import JType, IType, RType
from HexTranslator.InstructionTranslations.HexToBin import HexToBin
from HexTranslator.InstructionTranslations import JTranslation, ITranslation, RTranslation

jtype = JType.getOpcodes()
itype = IType.getOpcodes()
rtype = RType.getOpcodes()

def translateHexToMips(lines):
    ans = ""
    finalAns = ""
    k = 0
    try:
        for l in lines:
            if l != '':
                k += 1
                l = int(l, 16)
                opcode = HexToBin(32,l)
                opcodeBin = opcode[0:6]
                if(opcodeBin in jtype):
                    opcodeBin2 = opcode[6:32]
                    translation = JTranslation.translateJ(opcodeBin2)
                    ans = jtype[opcodeBin] + " " + translation
                    finalAns += ans + '\n'
                elif(opcodeBin in itype):
                    opcodeBin2 = opcode[6:32]
                    ans = ITranslation.translateI(opcodeBin,opcodeBin2)
                    finalAns += ans + '\n'
                elif(opcodeBin in rtype):
                    opcodeTotal = opcode[6:32]
                    opcodefinal = opcode[26:32]
                    opcodeBin2 = opcode[6:21]
                    ans = RTranslation.translateR(opcodefinal,opcodeBin2, opcodeTotal)
                    finalAns += ans + '\n'
                else:
                    return "Invalid" + '\nIn line ' + str(k)
    except Exception as e:
        return "Error: " + str(e) + '\nIn line ' + str(k)
    return finalAns
