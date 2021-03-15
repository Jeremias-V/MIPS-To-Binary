import sys
from HexTranslator.InstructionTranslations.HexToBin import HexToBin, HexToInt
from HexTranslator.InstructionSet import Registers, IType
sys.path.append("..")
registers = Registers.getRegisters()
zeros = ['$0', '$zero']
invalid = ['$k0', '$k1']
itype_rt_rs = ['001000', '001001', '001100', '001111', '001101', '001010', '001011']
itype_load = ['100011', '100101', '100100', '110000']
itype_store = ['101011', '101001', '101000', '111000']
itype_rs_rt = ['000100', '000101']
itype = IType.getOpcodes()

def twos_comp(val, bits):
    if (val & (1 << (bits - 1))) != 0:
        val = val - (1 << bits)        
    return val                         

def translateI(line, line1):
    arregloSalida = [[],[],[]]
    if(line in itype_rs_rt):
        rs = line1
        auxrs = rs[0:5]
        if(auxrs in registers):
            rsSalida = registers[auxrs]
            arregloSalida[0].append(rsSalida)
        rt = line1
        auxrt = rt[5:10]
        bintohex =line1
        auxbin = bintohex[10:26]
        if(auxrt in registers):
            rtSalida = registers[auxrt]
            arregloSalida[1].append(rtSalida)
            esComple = bintohex[10:11]
            if(esComple != '1'):
                bintohex = int(auxbin,2)
                res = hex((bintohex))
                arregloSalida[2].append(res)
            else:
                out = twos_comp(int(auxbin, 2), len(auxbin))
                out = str(out)
                arregloSalida[2].append(out)
        salida = itype[line] + "    " +arregloSalida[0][0] + ", " + arregloSalida[1][0] + ", " + arregloSalida[2][0]
        return salida
    if(line in itype_store):
        rs = line1
        auxrs =rs[0:5]
        if(auxrs in registers):
            rsSalida = registers[auxrs]
            arregloSalida[2].append(rsSalida)
        rt = line1
        auxrt = rt[5:10]
        bintohex = line1
        auxbin = bintohex[10:26]
        if(auxrt in registers):
            rtSalida = registers[auxrt]
            arregloSalida[0].append(rtSalida)
            esComple = bintohex[10:11]
            if(esComple != '1'):
                bintohex = int(auxbin,2)
                res = hex(bintohex)
                arregloSalida[1].append(res)
            else:
                out = twos_comp(int(auxbin, 2), len(auxbin))
                out = str(out)
                arregloSalida[1].append(out)
        salida = itype[line] + "    " +arregloSalida[0][0] + ", " + arregloSalida[1][0] + "(" + arregloSalida[2][0] + ")"
        return salida
    if(line in itype_load):
        rs = line1
        auxrs =rs[0:5]
        if(auxrs in registers):
            rsSalida = registers[auxrs]
            arregloSalida[2].append(rsSalida)
        rt = line1
        auxrt = rt[5:10]
        bintohex = line1
        auxbin = bintohex[10:26]
        if(auxrt in registers):
            rtSalida = registers[auxrt]
            arregloSalida[0].append(rtSalida)
            esComple = bintohex[10:11]
            if(esComple != '1'):
                bintohex = int(auxbin,2)
                res = hex(bintohex)
                arregloSalida[1].append(res)
            else:
                out = twos_comp(int(auxbin, 2), len(auxbin))
                out = str(out)
                arregloSalida[1].append(out)
        salida = itype[line] + "    " +arregloSalida[0][0] + ", " + arregloSalida[1][0] + "(" + arregloSalida[2][0] + ")"
        return salida
    if(line in itype_rt_rs):
        if(line == "001111"):
            rs = line1
            auxrs = rs[5:10]
            if(auxrs in registers):
                rsSalida = registers[auxrs]
                arregloSalida[1].append(rsSalida)
            num = line1
            auxbin = num[10:26]
            num = int(auxbin,2)
            res = str(num)
            salida = itype[line] + "    " + arregloSalida[1][0] + ", " + res
            return salida
        rs = line1
        auxrs =rs[0:5]
        if(auxrs in registers):
            rsSalida = registers[auxrs]
            arregloSalida[1].append(rsSalida)
        rt = line1
        auxrt = rt[5:10]
        bintohex = line1
        auxbin = bintohex[10:26]
        if(auxrt in registers):
            rtSalida = registers[auxrt]
            arregloSalida[0].append(rtSalida)
            esComple = auxbin[10:11]
            if(esComple != '1'):
                bintohex = int(auxbin,2)
                res = str(bintohex)
                arregloSalida[2].append(res)
            else:
                out = twos_comp(int(auxbin, 2), len(auxbin))
                out = str(out)
                arregloSalida[2].append(out)
        salida = itype[line] + "    " +arregloSalida[0][0] + ", " + arregloSalida[1][0] + ", " + arregloSalida[2][0]      
        return salida
    return "Codigo invalido"