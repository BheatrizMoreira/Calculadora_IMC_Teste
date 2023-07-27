# -*- coding: utf-8 -*-
"""Calculadora de massa corporal

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EBZrtcBV_3CsyNgBiHTf6ew2GYRVB5d2
"""

# Cálculo do Índice de Massa Corporal
import os

altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em Kg: "))

imc = peso / altura**2

print("Seu IMC é: %.4f" % imc)

if imc < 18:
	print("Magreza grave")
elif imc > 18:
	print("Saudável")
elif imc < 25:
	print("Saudável")
elif imc > 30:
	print("Sobrepeso Grau I")
elif imc > 35:
	print("Obesidade Grau II")
elif imc > 40:
	print("Obesidade Grau III (severa)")


os.system("pause")