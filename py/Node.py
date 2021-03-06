class Node:
    def __init__(self, simbolo = "Null",esquerda = None,direita=None):
        self.__simbolo = simbolo
        self.__frequencia = 0
        self.__esquerda = esquerda
        self.__direita = direita

    def ehFolha(self):
        return self.__esquerda is None and self.__direita is None

    def getFrequencia(self):
        if self.ehFolha():
            return self.__frequencia
        return self.__esquerda.getFrequencia() + self.__direita.getFrequencia()

    def getSimbolo(self):
        return self.__simbolo

    def getEsquerda(self):
        return self.__esquerda

    def getDireita(self):
        return self.__direita

    def incrementar(self):
        self.__frequencia += 1

    def __str__(self):
        return u'Char {0:s} : Frequencia {1:d}'.format(self.__simbolo, self.__frequencia)

    def __lt__(self, no):
        return self.getFrequencia() < no.getFrequencia()

    def __eq__(self, no):
        return self.getFrequencia() == no.getFrequencia()

    def __gt__(self, v):
        return self.getFrequencia() > no.getFrequencia()

    def preencherDicionario(self, dicionario, path):
        """

        :type dicioario: map
        """
        if self.ehFolha():
            dicionario[self.getSimbolo()] = path
            return
        self.__esquerda.preencherDicionario(dicionario, path = path + "0" )
        self.__direita.preencherDicionario(dicionario, path = path + "1")
