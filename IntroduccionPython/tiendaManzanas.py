print("--------- Bienvenido a la tienda de manzanas ------------\n")
print("Seleccione cuantas manzanas quiere comprar:\n ")

cantidad = float(input())

precio = 15

cobro = precio * cantidad

print("Cantidad a pagar: ", cobro, "\n" )
print("Ingrese su dinero: \n")

pago = float(input())

cambio = pago - cobro

print("Tome su cambio: ", cambio)

    

