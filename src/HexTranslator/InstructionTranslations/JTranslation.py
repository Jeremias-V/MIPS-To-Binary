import sys
from HexTranslator.InstructionTranslations.HexToBin import HexToBin, HexToInt
from HexTranslator.InstructionSet import Registers, JType
sys.path.append("..")
registers = Registers.getRegisters()
zeros = ['$0', '$zero']
invalid = ['$k0', '$k1']
jtype = JType.getOpcodes()

def translateJ(line):
    aux = int(line,2)
    res = hex((aux))
    res = str(res)
    return res