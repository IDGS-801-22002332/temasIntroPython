class OperacionesBas:
    #Declaracion de propiedades public, private _, protected __
    num1=0
    num2=0
    res=0
    #Declaracion del constructor this = self  Para seleccionar las propiedades de una clase
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    #Declaracion de metodos de clase
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es : {}".format(self.res))
    
    def resta(self):
        self.res=self.num1-self.num2
        print("La resta es : {}".format(self.res))

def main():
    obj=OperacionesBas(3,4)
    obj.suma()
    obj.resta()
    
if __name__ == "__main__":
    main()




