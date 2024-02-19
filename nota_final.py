
#programa para cálculo de nota

print()
print("********************************")
print("*        MÉDIA FINAL           *")
print("********************************")
print()


#criação das variáveis

nome = ""
nota1 = 0.0
nota2 = 0.0
nota3 = 0.0
nota4 = 0.0
notaF = 0.0

#entrada de dados

nome = input("Nome do aluno: ")
nota1 = float(input("Nota do bimestre 1: "))
nota2 = float(input("Nota do bimestre 2: "))
nota3 = float(input("Nota do bimestre 3: "))
nota4 = float(input("Nota do bimestre 4: "))

#processamento dos valores dados

notaF = (nota1 + nota2 + nota3 + nota4) / 4

media = ""

if notaF >= 7.0:
    media = "APROVADO!"
elif notaF < 5.0:
    media = "REPROVADO!"
else:
    media = "para a RECUPERAÇÃO"


#saida do processamento

print()
print("---------------------------------")
print()
print(nome + ", sua nota final é " + str(notaF) + ", então você foi " + str(media))
print()
print("---------------------------------")
