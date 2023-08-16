# Cálculo do Índice de Massa Corporal
import os

print("Para calculartmos seu IMC, digite abaixo suas informações:")
print("Informe sua altura em metros. Exemplo: 1.75 (cm) ")
altura = float(input("Altura:"))
print("Digite seu peso atual em Kg. Exemplo: 68.3 (kg) ")
peso = float(input("Peso Atual: "))

imc = peso / altura**2

print("Seu IMC é: %.4f" % imc)

if imc < 16:
	print("Magreza grave")
elif imc < 17:
	print("Magreza moderada")
elif imc < 18.5:
	print("Magreza leve")
elif imc < 25:
	print("Saudável")
elif imc < 30:
	print("Sobrepeso")
elif imc < 35:
	print("Obesidade Grau I")
elif imc < 40:
	print("Obesidade Grau II (severa)")
else:
	print("Obesidade Grau III (mórbida)")

os.system("pause")
