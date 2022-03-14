import random
'''''
classe responsavel por ler um arquivo txt com as palavras e escolher uma aleatoriamente
obs: as palavras nao usam acento nem caracteres especiais
'''
class Palavra:
    word = ""


    def ler_arq(self):
        lista_pal = []
        arq = open("palavras.txt")
        for linha in arq:
            lista_pal.append(linha.split())
        tam = len(lista_pal)
        escolhido = random.randint(0, tam-1)
        self.word = lista_pal[escolhido][0]
        arq.close()


    def __init__(self):
        self.ler_arq()
        self.word.lower()
    
    def tamanho(self):
        return len(self.word)
    
    def substituir(self,posicao,caractere):
        lista_pal = list(self.word)
        lista_pal[posicao] = caractere
        s = ''.join(lista_pal)
        self.word = s
   
