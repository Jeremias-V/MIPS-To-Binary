import sys
sys.path.append("..")

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
