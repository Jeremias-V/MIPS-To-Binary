from Translator.InstructionTranslations.Complements import IntToBin, HexToBin, isHex, twosComplement
import sys
sys.path.append("..")
from Translator.InstructionSet import Registers, RType, Functions

registers = Registers.getRegisters()
functions = Functions.getFunctions()
rtype = RType.getOpcodes()
zeros = ['$0', '$zero', '$gp']
invalid = ['$k0', '$k1']
rtype_rd_rs_rt = ['add', 'addu', 'and', 'nor', 'or', 'slt', 'sltu', 'sub', 'subu']
rtype_rd_rt_sh = ['sll', 'srl', 'sra']
rtype_move_rd = ['mfhi', 'mflo']
rtype_rs_rt = ['div', 'divu', 'mult', 'multu']

def translateR(line):
    ans = ""
    opcode = line[0]
    funct = opcode
    shamt = "0"
    if(opcode == "jr"):
        rs = line[1]
        rt = "$0"
        rd = "$0"
    elif(opcode in rtype_rd_rs_rt):
        rs = line[2][:-1]
        rt = line[3]
        rd = line[1][:-1]
        if(rd in zeros):
            return ans
    elif(opcode in rtype_rd_rt_sh):
        rs = '$0'
        rt = line[2][:-1]
        rd = line[1][:-1]
        shamt = line[3]
        if(rd in zeros):
            return ans
    elif(opcode in rtype_move_rd):
        # mfhi mflo? rd
        rs = '$0'
        rt = '$0'
        rd = line[1]
        if(rd in zeros):
            return ans
    elif(opcode in rtype_rs_rt):
        rs = line[1][:-1]
        if(rs in zeros):
            return ans
        rt = line[2]
        rd = '$0'
    else:
        return ans
    if(rs in registers and rt in registers and rd in registers and
       rs not in invalid and rt not in invalid and rd not in invalid):
       # check for $0
       rs = registers[rs]
       rt = registers[rt]
       rd = registers[rd]
    else:
        return ans
    if(isHex(shamt)):
        tmp = HexToBin(5, int(shamt, 16))
        if(int(tmp,2).bit_length() <= 5):
            # shamt is <= to 5 bits
            ans = rtype[opcode] + rs + rt + rd + tmp + functions[funct]
    elif(shamt[0] != '-'):
        # can't be negative
        tmp = IntToBin(5, int(shamt))
        if(int(tmp,2).bit_length() <= 5):
            # shamt is <= to 5 bits
            ans = rtype[opcode] + rs + rt + rd + tmp + functions[funct]
    return ans
