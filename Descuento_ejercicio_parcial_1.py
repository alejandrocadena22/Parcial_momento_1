#Entrada
Compra = float(input("ingrese el monto de la compra: "))
Descuento = Compra * 0.05
Descuento2 = Compra * 0.1
#Caja Negra
if Compra<50:
    print("Descuento aplicado: ", 0)
    print("Total a pagar:", Compra)
elif 50<=Compra<=100:
    print("El descuento es: ",Descuento)
    print("Total a pagar: ", Compra - Descuento)  
elif Compra>100:
    print("El descuento es: ",Descuento2)
    print("Total a pagar: ", Compra - Descuento2)