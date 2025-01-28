from io import open
import math

'''w para crear uno nuevo o sobreescribir'''
'''a para escribir en segunda linea'''
'''r para lectura'''

lectura=""
texto=open("archivo.txt","r")
lectura=texto.readlines()
print(type(lectura))
print(lectura)
for i in lectura:
    print(i)
texto.close()
