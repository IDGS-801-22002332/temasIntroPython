range(20) #0,1,2 ... 19
x=range(10,20)
y=range(1,20, 2)

for i in range(20):
    print(i)
    
    
''' Pide un numero y que te de la tabla de multiplicacion hasta el 10 '''

print('Dame un numero para encontrar su tabla de multiplicacion')
print('')
num=int(input('Ingresa el numero: '))

range = range(11)

for multiplicacion in range:
    resultado = multiplicacion * num 
    print(f' {multiplicacion } * {num} = ', resultado)
