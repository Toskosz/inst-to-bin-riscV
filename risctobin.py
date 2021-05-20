# instruções:
# bote este programa em uma pasta junto com seu programa.txt
# certifique-se de que as intruções tenham apenas um espaço
# sendo este localizado entre o nome da instrução e os argumentos
# seguindo o seguinte formato: "instrucao arg1,arg2,imm"
#
# Exemplo de formato errado é:
#   - add a0, a1, a2
#   - add a0, a1,a2
#   - add a0,a1, a2

# Pseudo instruções não foram incluidas assim como algumas outras
# A lista de instruções implementadas está abaixo separadas for familia de instrução

inst_tipoJ = {
    'jal': ['1101111']
}

inst_tipoB = {
    'beq':['1100011', '000'],
    'bne':['1100011', '001'],
    'blt':['1100011', '100'],
    'bge':['1100011', '101'],
    'bltu':['1100011', '110'],
    'bgeu':['1100011', '111']
}

inst_tipoR = {
    'add': ['0110011', '000', '0000000'],
    'sub': ['0110011', '000', '0100000'],
    'sll': ['0110011', '001', '0000000'],
    'slt': ['0110011', '010', '0000000'],
    'sltu': ['0110011', '011', '0000000'],
    'xor': ['0110011', '100', '0000000'],
    'srl': ['0110011', '101', '0000000'],
    'sra': ['0110011', '101', '0100000'],
    'or': ['0110011', '110', '0000000'],
    'and': ['0110011', '111', '0000000'],
    'mul': ['0110011', '000', '0000001'],
    'mulh': ['0110011', '001', '0000001'],
    'mulhsu': ['0110011', '010', '0000001'],
    'mulhu': ['0110011', '011', '0000001'],
    'div': ['0110011', '100', '0000001'],
    'divu': ['0110011', '101', '0000001'],
    'rem': ['0110011', '110', '0000001'],
    'remu': ['0110011', '111', '0000001'],
    'feq.s': ['1010011', '010', '1010000'],
    'fle.s': ['1010011', '000', '1010000'],
    'flt.s': ['1010011', '001', '1010000'],
    'fmax.s': ['1010011', '001', '0010100'],
    'fmin.s': ['1010011', '000', '0010100'],
    'fmv.s.x': ['1010011', '000', '111100000000'],
    'fmv.x.s': ['1010011', '000', '111000000000'],
    'fsgnj.s': ['1010011', '000', '0010000'],
    'fsgnjn.s': ['1010011', '001', '0010000'],
    'fsgnjx.s': ['1010011', '010', '0010000'],
}

inst_tipoS = {
    'sb': ['0100011', '000'],
    'sh': ['0100011', '001'],
    'sw': ['0100011', '010'],
    'fsw':['0100111', '010']
}

inst_tipoU = {
    'auipc': ['0010111'],
    'lui': ['0110111'],
}

inst_tipoI = {
    'lb': ['0000011', '000'],
    'lh': ['0000011', '001'],
    'lw': ['0000011', '010'],
    'lbu': ['0000011', '100'],
    'lhu': ['0000011', '101'],
    'addi': ['0010011', '000'],
    'slli': ['0010011', '001', '0000000'],
    'slti': ['0010011', '010'],
    'sltiu': ['0010011', '011'],
    'xori': ['0010011', '100'],
    'srli': ['0010011', '101', '0000000'],
    'srai': ['0010011', '101', '0100000'],
    'ori': ['0010011', '110'],
    'andi': ['0010011', '111'],
    'jalr': ['1100111', '000'],
    'flw': ['0000111', '010']
}

registradores = {
    'zero': '00000',
    'ra': '00001',
    'sp': '00010',
    'gp': '00011',
    'tp': '00100',
    't0': '00101',
    't1': '00110',
    't2': '00111',
    's0': '01000',
    's1': '01001',
    'a0': '01010',
    'a1': '01011',
    'a2': '01100',
    'a3': '01101',
    'a4': '01110',
    'a5': '01111',
    'a6': '10000',
    'a7': '10001',
    's2': '10010',
    's3': '10011',
    's4': '10100',
    's5': '10101',
    's6': '10110',
    's7': '10111',
    's8': '11000',
    's9': '11001',
    's10': '11010',
    's11': '11011',
    't3': '11100',
    't4': '11101',
    't5': '11110',
    't6': '11111',
}


def complemento_de_dois(num):
    num_bin = format(int(num), '032b')
    bin_invertido = ''.join(['1' if n == '0' else '0' for n in num_bin])
    um = '00000000000000000000000000000001'
    resultado = bin(int(bin_invertido, 2) + int(um, 2))
    resultado = resultado[2:34]
    return resultado


arquivo = open('programa.txt', 'r')
instrucoes = arquivo.readlines()
arquivo.close()

instrucoes_em_binario = []

for instrucao in instrucoes:

    instrucao = instrucao.strip().split()
    montagem_binario = []

    if instrucao[0] in inst_tipoR.keys():
        argumentos = instrucao[1].split(',')
        x = inst_tipoR[instrucao[0]]

        if instrucao[0] in ['fmv.s.x', 'fmv.x.s']:
            montagem_binario.append(x[2])
            montagem_binario.append(registradores[argumentos[1]])
            montagem_binario.append(x[1])
            montagem_binario.append(registradores[argumentos[0]])
            montagem_binario.append(x[0])
        else:
            montagem_binario.append(x[2])
            montagem_binario.append(registradores[argumentos[2]])
            montagem_binario.append(registradores[argumentos[1]])
            montagem_binario.append(x[1])
            montagem_binario.append(registradores[argumentos[0]])
            montagem_binario.append(x[0])

    elif instrucao[0] in inst_tipoI.keys():
        x = inst_tipoI[instrucao[0]]
        if '(' not in instrucao[1]:
            argumentos = instrucao[1].split(',')
            if int(argumentos[2]) < 0:
                numero = argumentos[2]
                imediato = complemento_de_dois(numero[1:])
            else:
                imediato = format(int(argumentos[2]), '032b')
            montagem_binario.append(imediato[20:32])
            montagem_binario.append(registradores[argumentos[1]])
            montagem_binario.append(x[1])
            montagem_binario.append(registradores[argumentos[0]])
            montagem_binario.append(x[0])
        else:
            argumentos = instrucao[1].replace('(', ',')
            argumentos = argumentos.replace(')', '')
            argumentos = argumentos.split(',')
            if int(argumentos[1]) < 0:
                numero = argumentos[1]
                imediato = complemento_de_dois(numero[1:])
            else:
                imediato = format(int(argumentos[1]), '032b')
            montagem_binario.append(imediato[20:32])
            montagem_binario.append(registradores[argumentos[2]])
            montagem_binario.append(x[1])
            montagem_binario.append(registradores[argumentos[0]])
            montagem_binario.append(x[0])
    elif instrucao[0] in inst_tipoS.keys():
        x = inst_tipoS[instrucao[0]]
        argumentos = instrucao[1].replace('(', ',')
        argumentos = argumentos.replace(')', '')
        argumentos = argumentos.split(',')
        if int(argumentos[1]) < 0:
            numero = argumentos[1]
            imediato = complemento_de_dois(numero[1:])
        else:
            imediato = format(int(argumentos[1]), '032b')
        montagem_binario.append(imediato[20:27])
        montagem_binario.append(registradores[argumentos[0]])
        montagem_binario.append(registradores[argumentos[2]])
        montagem_binario.append(x[1])
        montagem_binario.append(imediato[27:32])
        montagem_binario.append(x[0])
    elif instrucao[0] in inst_tipoU.keys():
        x = inst_tipoU[instrucao[0]]
        argumentos = instrucao[1].split(',')
        if int(argumentos[1]) < 0:
            numero = argumentos[1]
            imediato = complemento_de_dois(numero[1:])
        else :
            imediato = format(int(argumentos[1]), '032b')
        montagem_binario.append(imediato[12:32])
        montagem_binario.append(registradores[argumentos[0]])
        montagem_binario.append(x[0])
    elif instrucao[0] in inst_tipoJ.keys():
        x = inst_tipoJ[instrucao[0]]
        argumentos = instrucao[1].split(',')
        if int(argumentos[1]) < 0:
            numero = argumentos[1]
            imediato = complemento_de_dois(numero[1:])
        else:
            imediato = format(int(argumentos[1]), '032b')
        montagem_binario.append(imediato[11])
        montagem_binario.append(imediato[21:31])
        montagem_binario.append(imediato[20])
        montagem_binario.append(imediato[12:20])
        montagem_binario.append(registradores[argumentos[0]])
        montagem_binario.append(x[0])
    elif instrucao[0] in inst_tipoB.keys():
        x = inst_tipoB[instrucao[0]]
        argumentos = instrucao[1].split(',')
        if int(argumentos[2]) < 0:
            numero = argumentos[2]
            imediato = complemento_de_dois(numero[1:])
        else:
            imediato = format(int(argumentos[2]), '032b')
        montagem_binario.append(imediato[19])
        montagem_binario.append(imediato[21:27])
        montagem_binario.append(registradores[argumentos[1]])
        montagem_binario.append(registradores[argumentos[0]])
        montagem_binario.append(x[1])
        montagem_binario.append(imediato[27:31])
        montagem_binario.append(imediato[20])
        montagem_binario.append(x[0])

    binario = ''.join(montagem_binario)
    instrucoes_em_binario.append(binario)

with open('resultadoMSB.drs', 'w') as arquivo_handler:
    arquivo_handler.write('#A 0000h\n')
    arquivo_handler.write('#B\n')
    arquivo_handler.write('\n\n\n')
    for linha in instrucoes_em_binario:
        arquivo_handler.write('%s\n' % linha[:16])
        arquivo_handler.write('0000000000000000\n')
        arquivo_handler.write('0000000000000000\n')
        arquivo_handler.write('0000000000000000\n')

with open('resultadoLSB.drs', 'w') as arquivo_handler:
    arquivo_handler.write('#A 0000h\n')
    arquivo_handler.write('#B\n')
    arquivo_handler.write('\n\n\n')
    for linha in instrucoes_em_binario:
        arquivo_handler.write('%s\n' % linha[16:32])
        arquivo_handler.write('0000000000000000\n')
        arquivo_handler.write('0000000000000000\n')
        arquivo_handler.write('0000000000000000\n')