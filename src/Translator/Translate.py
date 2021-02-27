import sys
from sys import stdin

from Parser import clean
from InstructionSet import Registers, IType, JType, RType, Functions

invalid = ['$k0', '$k1']
rt_rs = ['addi', 'addiu', 'andi', 'lui', 'ori', 'slti', 'sltiu']
registers = Registers.getRegisters()
itype = IType.getOpcodes()
jtype = JType.getOpcodes()
rtype = RType.getOpcodes()
functions = Functions.getFunctions()

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
    if(opcode in rt_rs):
        rs = line[2][:-1]
        rt = line[1][:-1]
        if(rs in registers and rt in registers):
            rs = registers[rs]
            rt = registers[rt]
        else:
            return ""
        inmediate = line[3]
        if(isHex(inmediate)):
            tmp = HexToBin(16, int(inmediate, 16))
            if(int(tmp,2).bit_length() <= 16):
                # Inmediate is <= to 16 bits and rs_rt type
                ans = itype[opcode] + rs + rt + tmp
            else:
                return ""
        elif(inmediate[0] != '-'):
            # Address is positive decimal
            tmp = IntToBin(16, int(inmediate))
            if(int(tmp,2).bit_length() <= 16):
                ans += itype[opcode] + rs + rt + tmp
            else:
                return ""
        elif(inmediate[0] == '-'):
            # Address is negative decimal
            number = int(inmediate)
            if(number.bit_length() > 16):
                return ""
            tmp = twosComplement(16, number)
            ans += itype[opcode] + rs + rt + tmp
        else:
            return ""
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
    return

def translateMIPS():
    ans = ""
    lines = clean.cleanCode(stdin.readlines())
    try:
        for l in lines:
            opcode = l[0]
            if(opcode in itype):
                print("I",opcode, itype[opcode])
                traduction = translateI(l)
                if traduction != "":
                    ans += traduction + '\n'
                    print(traduction)
                else:
                    raise Exception
            elif(opcode in jtype and len(l) == 2):
                print("J",opcode, jtype[opcode])
                traduction = translateJ(l)
                if traduction != "":
                    ans += traduction + '\n'
                    print(traduction)
                else:
                    raise Exception
            elif(opcode in rtype):
                print("R",opcode, rtype[opcode], functions[opcode])
            else:
                print("Invalid")
    except Exception as e:
        print("ERROR: ", e)
translateMIPS()
