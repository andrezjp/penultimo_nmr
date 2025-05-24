# Solicita ao usuário que insira três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Cria uma lista com os números
numeros = [num1, num2, num3]

# Ordena a lista em ordem crescente
numeros.sort()

# O segundo maior número será o penúltimo elemento da lista
segundo_maior = numeros[-2]

print(f"O segundo maior número é: {segundo_maior}")