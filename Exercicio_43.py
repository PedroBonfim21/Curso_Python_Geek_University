valor_lido=float(input("Digite o valor: "))
desconto=valor_lido-valor_lido*(10/100)
parcela=valor_lido/3
comissao_desconto=(5/100)*desconto
comissao_parcela=(5/100)*valor_lido
print(f"O valor do produto com desconto é igual a: {desconto} .")
print(f"O valor de cada parcela é igual a: {parcela} .")
print(f"O valor da comissão para o produto pago a vista é de {comissao_desconto} .")
print(f"O valor da comissão para o produto pago parcelado é de {comissao_parcela} .")
