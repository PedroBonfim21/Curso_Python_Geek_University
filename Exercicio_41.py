hora=float(input("Digite o valor da sua hora trabalhada em reais: "))
h_trabalhada=float(input("Digite quantas horas trabalhou no mês: "))
valor= hora*h_trabalhada
valorpago= valor+((10/100)*valor)
print(f"o valor que deverá ser pago é igual a: {valorpago} Reais.")
