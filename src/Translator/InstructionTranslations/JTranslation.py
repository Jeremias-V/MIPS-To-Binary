from Translator.InstructionTranslations.Complements import HexToBin, IntToBin, isHex
import sys
sys.path.append("..")
from Translator.InstructionSet import Registers, JType

registers = Registers.getRegisters()
zeros = ['$0', '$zero']
invalid = ['$k0', '$k1']
jtype = JType.getOpcodes()

def translateJ(line):
    """
    Check for valid address (26 bits) and translate
    to binary no matter if its decimal or hex.
    """
    ans = ""
    opcode = line[0]
    address = line[1]
    ans += jtype[opcode]
    if(isHex(address)):
        # Address is hex
        tmp = HexToBin(26, int(address, 16))
        if(int(tmp,2).bit_length() <= 26):
            # Address is <= to 26 bits
            ans += tmp
        else:
            return ""
    elif(address[0] != '-'):
        # Address is non negative decimal
        tmp = IntToBin(26, int(address))
        if(int(tmp,2).bit_length() <= 26):
            ans += tmp
        else:
            return ""
    else:
        return ""
    return ans
