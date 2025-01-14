print("Ingresa lo que quieres que diga el periquito:")
frase = input()
print("Cuantas veces quieres que lo diga?")
numero = float(input())

def periquito(frase, numero):
    while numero > 0 :
        print(frase)
        numero-=1

periquito(frase, numero)

    