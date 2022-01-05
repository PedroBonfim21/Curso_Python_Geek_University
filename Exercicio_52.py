premio=float(input("Digite o valor do premio: "))
apostador1=float(input("Digite o valor apostado pelo 1°: "))
apostador2=float(input("Digite o valor apostado pelo 2°: "))
apostador3=float(input("Digite o valor apostado pelo 3°: "))

apostatotal= apostador1+apostador2+apostador3 
porcentagem1= apostador1/apostatotal
porcentagem2= apostador2/apostatotal
porcentagem3= apostador3/apostatotal
ganho1= porcentagem1*premio
ganho2= porcentagem2*premio
ganho3= porcentagem3*premio
print(f" O valor que cada o jogador 1 ganhou foi: {ganho1} \n o valor que o jogador 2 ganhou foi: {ganho2} \n O valor que o jogador 3 ganhou foi: {ganho3}")