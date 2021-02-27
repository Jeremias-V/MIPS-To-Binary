import sys
from sys import stdin

from Parser import clean
from InstructionSet import Registers, IType, JType, RType, Functions

zeros = ['$0', '$zero']
invalid = ['$k0', '$k1']
itype_rt_rs = ['addi', 'addiu', 'andi', 'lui', 'ori', 'slti', 'sltiu']
itype_load = ['lw', 'lh', 'lhu', 'lb', 'lbu', 'll']
itype_store = ['sw', 'sh', 'sb', 'sc']
itype_rs_rt = ['beq', 'bne']
rtype_rd_rs_rt = ['add', 'addu', 'and', 'nor', 'or', 'slt', 'sltu', 'sub', 'subu']
rtype_rd_rt_sh = ['sll', 'srl', 'sra']
rtype_move_rd = ['mfhi', 'mflo']
rtype_rs_rt = ['div', 'divu', 'mult', 'multu']
registers = Registers.getRegisters()
itype = IType.getOpcodes()
jtype = JType.getOpcodes()
rtype = RType.getOpcodes()
functions = Functions.getFunctions()

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
            return ""
    else:
        return ""

def twosComplement(bits, n):
    if n < 0:
        n = ( 1<<bits ) + n
    ans = '{:0%ib}' % bits
    return ans.format(n)

def IntToBin(f, n):
    return "{:0>{}b}".format(n,f)

def IntToHex(f, n):
    return "{0:#0{1}x}".format(n,f+2)

def HexToInt(h):
    return int(h)

def HexToBin(f, n):
    return IntToBin(int(f), HexToInt(n))

def isHex(s):
    if(len(s) > 1 and s[0] == '0' and s[1] == 'x'):
        return True
    else:
        return False

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
        return '*'
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
    if ans == "": return '*'
    return ans

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
    elif(opcode in rtype_rd_rt_sh):
        rs = '$0'
        rt = line[2][:-1]
        rd = line[1][:-1]
        shamt = line[3]
    elif(opcode in rtype_move_rd):
        # mfhi mflo? rd
        rs = '$0'
        rt = '$0'
        rd = line[1]
    elif(opcode in rtype_rs_rt):
        rs = line[1][:-1]
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

def translateMIPS():
    ans = ""
    lines = clean.cleanCode(stdin.readlines())
    try:
        for l in lines:
            opcode = l[0]
            if(opcode in itype):
                #print("I",opcode, itype[opcode])
                traduction = translateI(l)
                if traduction != "":
                    ans += traduction + '\n'
                    print(traduction)
                else:
                    raise Exception
            elif(opcode in jtype and len(l) == 2):
                #print("J",opcode, jtype[opcode])
                traduction = translateJ(l)
                if traduction != "":
                    ans += traduction + '\n'
                    print(traduction)
                else:
                    raise Exception
            elif(opcode in rtype):
                traduction = translateR(l)
                if traduction != "":
                    ans += traduction + '\n'
                    print(traduction)
                else:
                    raise Exception
                #print("R",opcode, rtype[opcode], functions[opcode])
            else:
                print("Invalid")
    except Exception as e:
        print("ERROR: ", e)
translateMIPS()
