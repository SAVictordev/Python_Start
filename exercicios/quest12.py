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
opcpagamento = [1,2,3,4]

if (metodpagamento == 1 and metodpagamento in opcpagamento):
        valorprodfinal = valprod - ((valprod*15)/100)
        print("O valor do produto por pix é: ", valorprodfinal)
elif(metodpagamento == 2 and metodpagamento in opcpagamento):
        valorprodfinal = valprod - ((valprod*10)/100)
        print("O valor do produto à vista no cartão de crédito é: ", valorprodfinal)
elif(metodpagamento == 3    and metodpagamento in opcpagamento):
        valorprodfinal = valprod
        print("O valor de duas parcelas do produto é: " , (valorprodfinal/2), " e o total é: ", valorprodfinal)
elif(metodpagamento == 4    and metodpagamento in opcpagamento):
        valorprodfinal = valprod + ((valprod*10)/100)
        print("O valor da parcela do produto é: ", (valorprodfinal/3), " e o valor total é: ", valorprodfinal)
else:
        print("Metódo de pagamento inválido")