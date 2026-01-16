##  Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago,
##  conforme a escolha da forma de pagamento
##  pelo comprador e imprima na tela o valor final do produto a ser pago. 
##  utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

##  Tabela de Código de Condições de Pagamento
## 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
## 2 - À Vista no cartão de crédito, recebe 10% de desconto
## 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
## 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%


valor_produto = float(input("Qual o preço do produto? "))
metodo_de_pagamento = int(input("Qual o método de pagamento?: "))
numero_de_parcelas = 0

if (metodo_de_pagamento == 1):
        valor_final_produto = valor_produto - ((valor_produto*15)/100)
        print("O valor do produto por pix é: ", valor_final_produto)
elif(metodo_de_pagamento == 2 ):
        valor_final_produto = valor_produto - ((valor_produto*10)/100)
        print("O valor do produto à vista no cartão de crédito é: ", valor_final_produto)
elif(metodo_de_pagamento == 3):
        valor_final_produto = valor_produto
        print("O valor de cada parcela é: " , (valor_final_produto/2), " e o total é: ", valor_final_produto)
elif(metodo_de_pagamento == 4 ):
        numero_de_parcelas = int(input("Digite o número de parcelas (máx: 12)"))
        if (numero_de_parcelas > 0 and numero_de_parcelas < 13):
                valor_final_produto = valor_produto + ((valor_produto*10)/100)
                print("O valor de cada parcela é: ",(valor_final_produto / numero_de_parcelas), "total do produt é: ", valor_final_produto)
        else:
                print("Número de parcelas inválido.")
else:
        print("Método de pagamento inválido")