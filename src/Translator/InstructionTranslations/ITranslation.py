from Translator.InstructionTranslations.Complements import IntToBin, HexToBin, isHex, twosComplement
import sys
sys.path.append("..")
from Translator.InstructionSet import Registers, IType

registers = Registers.getRegisters()
itype = IType.getOpcodes()
zeros = ['$0', '$zero']
invalid = ['$k0', '$k1']
itype_rt_rs = ['addi', 'addiu', 'andi', 'lui', 'ori', 'slti', 'sltiu']
itype_load = ['lw', 'lh', 'lhu', 'lb', 'lbu', 'll']
itype_store = ['sw', 'sh', 'sb', 'sc']
itype_rs_rt = ['beq', 'bne']

def getITypeParams(s):
    inmediate = ""
    register = ""
    i = 0
    while(i < len(s) and s[i] != "("):
        inmediate += s[i]
        i += 1
    if(s[i] == "("):
        i += 1
        while(i < len(s) and s[i] != ")"):
            register += s[i]
            i += 1
        if(s[i] == ")"):
            return [inmediate, register]
        else:
            return []
    else:
        return []

def translateI(line):
    ans = ""
    opcode = line[0]
    if(opcode in itype_rt_rs):
        rs = line[2][:-1]
        rt = line[1][:-1]
        inmediate = line[3]
    elif(opcode in itype_rs_rt):
        rs = line[1][:-1]
        rt = line[2][:-1]
        inmediate = line[3]
    elif(opcode in itype_load or opcode in itype_store):
        #lw      $t0, 0($s2)
        params = getITypeParams(line[2])
        inmediate = params[0]
        rs = params[1]
        rt = line[1][:-1]
    else:
        return ans
    if(rs in registers and rt in registers and rs not in invalid and rt not in invalid):
        # check if is a valid register missing to check $0
        rs = registers[rs]
        rt = registers[rt]
    else:
        return ans
    if(isHex(inmediate)):
        tmp = HexToBin(16, int(inmediate, 16))
        if(int(tmp,2).bit_length() <= 16):
            # Inmediate is <= to 16 bits and rs_rt type
            ans = itype[opcode] + rs + rt + tmp
        else:
            return ans
    elif(inmediate[0] != '-'):
        # Address is positive decimal
        tmp = IntToBin(16, int(inmediate))
        if(int(tmp,2).bit_length() <= 16):
            ans = itype[opcode] + rs + rt + tmp
        else:
            return ans
    elif(inmediate[0] == '-'):
        # Address is negative decimal
        number = int(inmediate)
        if(number.bit_length() > 16):
            return ans
        tmp = twosComplement(16, number)
        ans = itype[opcode] + rs + rt + tmp
    else:
        return ans
    return ans
