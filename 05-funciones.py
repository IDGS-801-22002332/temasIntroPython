import os

def funcion1():
    os.system('cls')
    num1=int(input('Numero 1: '))
    num2=int(input('Numero 2: '))
    res=num1+num2
    print(f'Resultado: {res}')
    
def funcion2():
    os.system('cls')
    num1=int(input('Numero 1: '))
    num2=int(input('Numero 2: '))
    res=num1-num2
    print(f'Resultado: {res}')

def funcion3():
    os.system('cls')
    num1=int(input('Numero 1: '))
    num2=int(input('Numero 2: '))
    res=num1*num2
    print(f'Resultado: {res}')

def funcion4():
    os.system('cls')
    num1=int(input('Numero 1: '))
    num2=int(input('Numero 2: '))
    res=num1/num2
    print(f'Resultado: {res}')


def run():
    i=0
    
    while i!=5:
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicacion')
        print('4. Division')
        print('5. Salir')
        op=int(input('Opcion: '))
        os.system('cls')
        if op==1:
            funcion1()
        if op==2:
            funcion2()
        if op==3:
            funcion3()
        if op==4:
            funcion4()
        i=op


if __name__ == "__main__":
    run()