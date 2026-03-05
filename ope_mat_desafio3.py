num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (soma, subtração, multiplicação, divisão): ")

if operacao == "soma":
    resultado = num1 + num2
elif operacao == "subtração":
    resultado = num1 - num2
elif operacao == "multiplicação":
    resultado = num1 * num2
elif operacao == "divisão":
    resultado = num1 / num2
else:
    resultado = "Operação inválida"

print("O resultado da operação é:", resultado)