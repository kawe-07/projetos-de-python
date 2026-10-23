print("bem vindo, à calculadora em python!")

num1 = float(input("digite um numero: "))
num2 = float(input("digite outro numero: "))
print("digite uma operação matematica, + | - | x ou * | ou /.")
oper = input("digite a operação:")

if oper == "+":
    soma = num1 + num2
    print(f"este é o resultado da sua soma: {soma}")

elif oper == "-":
    subtra = num1 - num2
    print(f"este é o resultado da sua subtração: {subtra} ")

elif oper in ("x", "*"):
    mult = num1 * num2
    print(f"este é o resultado da sua multiplicação: {mult}")

elif oper == "/":
    
    if num2 == 0:
        print("não é possivel dividir nenhum numero por zero.")
    else:
        div = num1 / num2
        print(f"este é o resultado da sua divisão: {div}")

else:
    print("está não é uma operação matematica! digite uma operação valida.")