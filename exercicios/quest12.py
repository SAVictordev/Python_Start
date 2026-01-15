##  Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago,
##  conforme a escolha da forma de pagamento
##  pelo comprador e imprima na tela o valor final do produto a ser pago. 
##  utilize os códigos da tabela de condições de pagamento para efetuar o cálculo adequado.

##  Tabela de Código de Condições de Pagamento
## 1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
## 2 - À Vista no cartão de crédito, recebe 10% de desconto
## 3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
## 4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%


valprod = float(input("Qual o preço do produto? "))
metodpagamento = int(input("Qual o método de pagamento?: "))
nmrparcelas = 0

if (metodpagamento == 1):
        valorprodfinal = valprod - ((valprod*15)/100)
        print("O valor do produto por pix é: ", valorprodfinal)
elif(metodpagamento == 2 ):
        valorprodfinal = valprod - ((valprod*10)/100)
        print("O valor do produto à vista no cartão de crédito é: ", valorprodfinal)
elif(metodpagamento == 3):
        valorprodfinal = valprod
        print("O valor de cada parcela é: " , (valorprodfinal/2), " e o total é: ", valorprodfinal)
elif(metodpagamento == 4 ):
        nmrparcelas = int(input("Digite o número de parcelas (máx: 12)"))
        if (nmrparcelas > 0 and nmrparcelas < 13):
                valorprodfinal = valprod + ((valprod*10)/100)
                print("O valor de cada parcela é: ",(vlrparcelaprod := valorprodfinal / nmrparcelas), "total do produt é: ", valorprodfinal)
        else:
                print("Número de parcelas inválido.")
else:
        print("Método de pagamento inválido")