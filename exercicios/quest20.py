## Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.


valor_inteiro = int(input("Digite um valor inteiro: "))

def tabuada(valor_inteiro):
    for i in range(1,11):
        print(f'{valor_inteiro} x {i} = {valor_inteiro * i}')

tabuada(valor_inteiro)