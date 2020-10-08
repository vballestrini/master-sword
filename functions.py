import copy
from queue import PriorityQueue

#Variaveis globais
GRAMA = 10
AREIA = 20
FLORESTA= 100
MONTANHA = 150
AGUA = 180
OBJETIVO = (0, 0)

def leMapa(nomeArquivo):
    mapa = open(nomeArquivo).read()
    mapa = [item.split() for item in mapa.split('\n')[:-1]]
    return mapa

MAPA = leMapa('mapa-hyrule.txt')

class Terreno:
    def __init__(self, linha, coluna):
        self.tipo = MAPA[linha][coluna]
        self.vizinhos = []
        self.anterior = Terreno
        self.linha = linha
        self.coluna = coluna

    def getPosicao(self):
        return self.linha, self.coluna

    def getCusto(self):
        g, h = 0, 0
        if self.tipo == 'G':
            g = 10
        elif self.tipo == 'A':
            g = 20
        elif self.tipo == 'F':
            g = 100
        elif self.tipo == 'M':
            g = 150
        elif self.tipo == 'H':
            g = 180
        x1, y1 = self.linha, self.coluna
        x2, y2 = OBJETIVO
        h = abs(x1 - x2) + abs(y1 - y2)
        return g + h

    def setAnterior(self, terreno):
        self.anterior = terreno



def imprimeMapa(mapa):
    linhas = len(mapa)
    colunas = len(mapa[0])
    for i in range(linhas):
        for j in range(colunas):
            print('%s' %mapa[i][j], end = '')
        print()

def encontraCaminho (casa, msword, pverde, pazul, pvermelho):
    
    global OBJETIVO
    objetivo = pverde
    expandidos = {casa}
    visitados = {}

    while expandidos:
        pass