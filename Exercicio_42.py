salario_base=float(input("Digite o seu salario base: "))
imposto=(7/100)*salario_base
gratificação=(5/100)*salario_base
salario=salario_base+gratificação-imposto
print(f"O seu salario real é igual a: {salario} Reais.")