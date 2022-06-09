import random
from printlista import printlista

arquivo = open("palavras.txt", "r")
palavras = []

for linha in arquivo:
    linha = linha.strip()
    if len(linha) == 5:
        palavras.append(linha)

arquivo.close()


sel = random.choice(palavras).upper()

lista=['_____','_____','_____','_____','_____','_____']

printlista(lista,sel)

for c in range(0,6):
    lista[c]=str(input( )).upper()
    while len(lista[c]) !=5:
        lista[c] = str(input()).upper()
    printlista(lista,sel)
    if lista[c] == sel:
       break