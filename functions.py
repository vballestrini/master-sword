import copy

#Variaveis globais
cgrama = 10
careia = 20
cfloresta= 100
cmontanha = 150
cagua = 180

def leMapa(nomeArquivo):
    mapa = open(nomeArquivo).read()
    mapa = [item.split() for item in mapa.split('\n')[:-1]]
    return mapa

def imprimeMapa(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])
    
    for i in range(linhas):
        for j in range(colunas):
            print('%s' %mapa[i][j], end = '')
        print()
