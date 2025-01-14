print("Ingrese el primer numero")
num1 = float(input())
print("Ingrese el signo")
signo = input()
print("Ingrese el segundo numero")
num2 = float(input())

def calculadora(signo, num1, num2):
    match signo:
        case "+":
            print(num1, signo, num2, " = ", num1 + num2)
        case "-":
            print(num1, signo, num2, " = ", num1 - num2)
        case "x":
            print(num1, signo, num2, " = ", num1 * num2)
        case "/":
            print(num1, signo, num2, " = ", num1 / num2)
        case "_":
            print("Ingresa un signo valido (+,-,x,/)")

calculadora(signo, num1, num2)
