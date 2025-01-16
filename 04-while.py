'''Convertir entero a string
    Ejemplo
    tem=""
    tem+=str(x)+"+"
'''

x=0

while x<10:
    print(x)
    x=x+1
    
'''operacion de multiplicacion de a x b utilizando sumas
    a=3
    b=4
    salida: s
'''

print('Dame un numero')
print('')
a=int(input('Ingresa un numero: '))
b=int(input('Cuentas veces se va a sumar: '))

salida=0
cont=0

while cont < b:
    salida += a
    cont +=1
print(salida)
