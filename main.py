import sys
from palavra import Palavra
from os import system
from forca import Forca
''''
Jogo da Forca: esse miniprograma foi portado para windows, para usa-lo em outro systema operacional mude os metodos system(cls) e system(pause)

'''


class main:
   plv = Palavra()
   forc = Forca()
   plv_inicial = plv.word
   fechada = ['~']*plv.tamanho()
   usadas = []
   ganhou = False
   tentativas = 6
  
   while(tentativas > 0):
       system("cls")
       print("as palavras nao usam acento nem caracteres especiais!")
       print("letras usadas: ")
       print(usadas)
       forc.mostrar(6 - tentativas)
       print(" ".join(fechada))
       print("------------------------------")
       letra = input("Digite uma letra: ")
       while(letra.isspace() |( not letra.isalpha())):
            letra = input("Digite uma letra valida: ")
    
       try:
        while( (letra[0].lower() in usadas)):
           letra = input("Digite uma letra nao usada anteriormente: ")
       
            
       
        if(letra[0].lower() in plv.word):
            while(letra[0].lower() in plv.word):
                pos = plv.word.rfind(letra[0].lower())
                plv.substituir(pos,"*")
                fechada[pos] = letra[0].lower()
        else:
            tentativas = tentativas - 1
        
        if("".join(fechada) == plv_inicial):
            ganhou = True
            break

        usadas.append(letra[0].lower())
       except:
           print("digite uma letra!")

   if(ganhou == True):
        print("ganhou!")
        print("A palavra era: "+plv_inicial)

   else:
        system("cls")
        forc.mostrar(6)
        print(" ".join(fechada))
        print("-- perdeu! --")
        print("A palavra era: "+plv_inicial)
system("pause")

       


