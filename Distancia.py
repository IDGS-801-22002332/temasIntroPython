'''Calcular la distancia de 2 puntos'''

class Distancia:
    x1=0
    x2=0
    y1=0
    y2=0
    res=0
    def __init__(self):
        self.x1=0
        self.x2=0
        self.y1=0
        self.y2=0
    def resultado(self):
        self.res=((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5
        print("La distancia de ambos de los lados es {}".format(self.res))
    def datos(self):
        print('Dame el primer punto')
        self.x1=int(input('Ingresa el primer punto x1: '))
        self.x2=int(input('Ingresa el segundo punto x2: '))
        print('Dame el segundo punto')
        self.y1=int(input('Ingresa el primer punto y1: '))
        self.y2=int(input('Ingresa el segundo punto y2: '))

def main():
    obj=Distancia()
    obj.datos()
    obj.resultado()

if __name__ == "__main__":
    main()