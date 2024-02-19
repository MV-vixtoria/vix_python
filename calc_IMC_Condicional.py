
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

situacao = ""

if imc < 18.5:
    situacao = "Abaixo do peso"
elif imc >= 18.5 or imc < 24.9:
    situacao = "Peso normal"
elif imc >= 25 or imc < 29.9:
    situaçao = "Sobrepeso"
elif imc >= 30 or imc < 34.9:
    situacao = "Obesidade Grau 1"
elif imc >= 35 or imc < 39.9:
    situacao = "Obesidade Grau 2"
else:
    situacao = "Obesidade Grau 3 ou Mórbida"


#saida do processamento

print()
print("********************************")
print("*          RESULTADO           *")
print("********************************")
print("NOME: " + nome)
print("PESO: " + str(peso))
print("ALTURA: " + str(altura))
print("IMC é %.3f: " % imc)
print("SITUAÇÃO: " + str(situacao))



