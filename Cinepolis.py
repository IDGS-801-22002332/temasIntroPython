class Cinepolis:
    precioBoletos = 12

    def __init__(self):
        self.nombre = ""
        self.cantPersonas = 0
        self.cantBoletos = 0
        self.totalCompra = 0
        self.comprasRealizadas = []  

    def datos(self):
        self.nombre = input("Ingrese su nombre: ")
        self.cantPersonas = int(input("Ingrese el numero de personas que lo a compañan: "))
        self.cantBoletos = int(input("¿Cuantos boletos desea comprar? "))

    def boletos(self):
        cantMaxima = self.cantPersonas * 7
        while self.cantBoletos > cantMaxima:
            print(f"Lo sentimos, no puedes comprar mas de {cantMaxima} boletos.")
            print("1. Cambiar numero de boletos")
            print("2. Cambiar numero de personas")
            opcion = input("Seleccione una opcion nueva: ")

            if opcion == "1":
                self.cantBoletos = int(input("Ingrese la nueva cantidad de boletos: "))
            elif opcion == "2":
                self.cantPersonas = int(input("Ingrese la nueva cantidad de personas: "))
                cantMaxima = self.cantPersonas * 7 
            else:
                print("Opcion invalida, intente de nuevo.")

    def total(self):
        self.totalCompra = self.cantBoletos * self.precioBoletos

        if self.cantBoletos > 5:
            self.totalCompra *= 0.85  

        while True:
            print("\nSeleccione su metodo de pago:")
            print("1. Efectivo")
            print("2. Tarjeta CINECO (10% de descuento adicional)")
            opcion = input("Ingrese su opcion de pago: ")

            if opcion == "1":
                print("Su pago sera en efectivo")
                break
            elif opcion == "2":
                self.totalCompra *= 0.90
                print("Al pagar Tarjeta CINECO se le aplicara un 10% de descuento adicional.")
                break
            else:
                print("Opcion invalida, intente de nuevo.")

        print(f"Su total a pagar es de: ${self.totalCompra:.2f}")

        self.comprasRealizadas.append(f"{self.nombre}: ${self.totalCompra:.2f}")

    def guardarCompras(self):
        with open("compraCineco.txt", "w") as compras:  
            for compra in self.comprasRealizadas:
                compras.write(compra + "\n")

    def mostrarCompra(self):
        print("\nLas compras de hoy fueron:")
        total_pagar = 0 

        if not self.comprasRealizadas:
            print("No se han registrado compras.")
        else:
            for compra in self.comprasRealizadas:
                print(compra)  
                try:
                    total_venta = float(compra.split(": $")[1].strip())
                    total_pagar += total_venta
                except (IndexError, ValueError):
                    print("Error:", compra)

        print(f"\nEl total de compras de hoy fueron: ${total_pagar:.2f}") 
        self.guardarCompras()

def main():
    obj = Cinepolis()
    
    opcion = "1"
    while opcion != "2":
        print("\nMENU PRINCIPAL")
        print("1. Comprar boletos")
        print("2. Terminar ejecución")
        opcion = input("Seleccione una opcion correcta: ")

        if opcion == "1":
            obj.datos()
            obj.boletos()
            obj.total()
        elif opcion == "2":
            obj.mostrarCompra()
        else:
            print("Opcion invalida, elija una opcion correcta.")

if __name__ == "__main__":
    with open("compraCineco.txt", "w"):
        pass  
    main()
