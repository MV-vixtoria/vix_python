
#programa para calcular IMC
#desenvolvido por Victoria

print("********************************")
print("*     CALCULADORA DE IMC       *")
print("********************************")
print()

#criação das variáveis

nome = ""
peso = 0
altura = 0.0
imc = 0.0

#entrada dos dados

nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

#processamento dos valores p/ obter o IMC (peso/altura^2)

imc = peso / altura ** 2

#saida do processamento

print()
print("********************************")
print("*          RESULTADO           *")
print("********************************")
print("NOME: " + nome)
print("PESO: " + str(peso))
print("ALTURA: " + str(altura))
print("IMC: " + str(imc))
