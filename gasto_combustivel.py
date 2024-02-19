
#programa para cálculo de combustível

print()
print("--------------------------------------")
print("        CONSUMO DE COMBUSTÍVEL        ")
print("--------------------------------------")
print()

#criação de variáveis

mod = ""
auton = 0
dist = 0.0
val_comb = 0.0
total_comb = 0.0
total = 0.0

#entrada de dados

mod = input("Modelo do carro? ")
auton = int(input("Autonomia do carro? "))
dist = float(input("Distância da viagem? "))
val_comb = float(input("Preço do combustível? "))

#processamento dos valores

total_comb = dist / auton
total = total_comb * val_comb

#saida do processamento

print()
print("--------------------------------------")
print("          R E S U L T A D O           ")
print("--------------------------------------")
print()
print(f"Modelo do veículo: {mod}")
print(f"Autonomia do veículo: {auton} Km/1")
print(f"Distância percorrida: {dist} Km/1")
print(f"Valor do combustível: R$ {val_comb} ,00")
print()
print("--------------------------------------")
print()
print(f"Quantidade de combustível utilizado: {total_comb:.2f} L")
print(f"Total gasto com a viagem: R$ {total:.2f} ")
print()
print("--------------------------------------")

