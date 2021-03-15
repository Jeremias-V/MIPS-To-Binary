import sys
from HexTranslator.InstructionTranslations.HexToBin import HexToBin, HexToInt
from HexTranslator.InstructionSet import Registers, RType, Functions

registers = Registers.getRegisters()
functions = Functions.getFunctions()
zeros = ['$0', '$zero']
invalid = ['$k0', '$k1']
jra = ['001000']
rtype_rd_rs_rt = ['100000', '100001', '100100', '100111', '100101', '101010', '101011', '100010', '100011']
rtype_rd_rt_sh = ['000000', '000010', '000011']
rtype_move_rd = ['010000', '010010']
rtype_rs_rt = ['011010', '011011', '011000', '011001']
rtype = RType.getOpcodes()


def translateR(line, line1, line2):
    arregloSalida = [[],[],[]]
    if(line in jra):
        salida = "jr $ra"
        return salida
    if(line in rtype_rd_rs_rt):
        rs = line1
        auxrs = rs[0:5]
        if(auxrs in registers):
            rsSalida = registers[auxrs]
            arregloSalida[1].append(rsSalida)
        rt = line1
        auxrt = rt[5:10]
        if(auxrt in registers):
            rtSalida = registers[auxrt]
            arregloSalida[2].append(rtSalida)
        rd = line1
        auxrd = rd[10:15]
        if(auxrd in registers):
            rdSalida = registers[auxrd]
            arregloSalida[0].append(rdSalida)
        salida = functions[line] + " " + arregloSalida[0][0] + ", " + arregloSalida[1][0] + ", " + arregloSalida[2][0]
        return salida
    if(line in rtype_rd_rt_sh):
        rs = line2
        auxrs =rs[5:10]
        if(auxrs in registers):
            rsSalida = registers[auxrs]
            arregloSalida[1].append(rsSalida)
        rt = line2
        auxrt = rt[10:15]
        if(auxrt in registers):
            rtSalida = registers[auxrt]
            arregloSalida[2].append(rtSalida)
        num = line2
        auxnum = num[15:20]
        bintodec = int(auxnum,2)
        salida = functions[line] + " " + arregloSalida[2][0] + ", " + arregloSalida[1][0] + ", " + str(bintodec)
        return salida
    if(line in rtype_move_rd):
        r = line1
        auxr = r[10:15]
        if(auxr in registers):
            rSalida = registers[auxr]
            arregloSalida[0].append(rSalida)
        salida = functions[line] + " " + arregloSalida[0][0]
        return salida
    if(line in rtype_rs_rt):
        first = line1
        auxfirst = first[0:5]
        if(auxfirst in registers):
            fSalida = registers[auxfirst]
            arregloSalida[0].append(fSalida)
        second = line1
        auxSecond = second[5:10]
        if(auxSecond in registers):
            sSalida = registers[auxSecond]
            arregloSalida[1].append(sSalida)
        salida = functions[line] + " " + arregloSalida[0][0] + ", " + arregloSalida[1][0]
        return salida
    return "Codigo invalido"
