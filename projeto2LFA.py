estados = input().split(" ")
alfabeto = input().split(" ")
transicoes = int(input())

afnd = {}

for estado in estados:
    afnd[estado] = {}

while (0 < transicoes):

    Inicial, Atual, Final = input().split(" ")
    if Atual not in afnd[Inicial]:
        afnd[Inicial][Atual] = [Final]
    else:
        afnd[Inicial][Atual].append(Final)
    transicoes=transicoes-1

inicio = input()
fim = input().split(" ")
palavras = input().split(" ")

estadosFinais = {}

for i in fim:
    estadosFinais[i] = 1

for palavra in palavras:
    estadosAtuais = [inicio]
    isFinal = 0

    for letra in palavra:
        novosEstados = []

        for estado in estadosAtuais:
            if(afnd[estado].get(letra)):

                for novoEstado in afnd[estado][letra]:
                    if(novoEstado not in novosEstados):
                        novosEstados.append(novoEstado) 

        estadosAtuais = novosEstados
    for estado in estadosAtuais:
        if(estadosFinais.get(estado)):
            isFinal = 1
 
    if(isFinal == 1):
        print('S')
    else:
        print('N')
