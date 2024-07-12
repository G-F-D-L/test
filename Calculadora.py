opr = str(input(""""Escolha a operação que deseja fazer dentre as opções abaixo))
            + = soma
            * = multiplicação
            / = divisão
            - = subtração
            Digite a operação que deseja fazer: """))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
if opr == "+": 
    print("O resultado é:", num1 + num2)
elif opr == "*":
    print("O resultado é:", num1 * num2)
elif opr == "/":
    if num2 == 0:
        print("Operação inválida")
    else:
        print("O resultado é:", num1 / num2)
elif opr == "-":
    print("O resultado é:", num1 - num2)