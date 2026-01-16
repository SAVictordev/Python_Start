## Faça um algoritmo que calcule a quantidade de litros de combustível gastos em uma viagem, 
## sabendo que o carro faz 12km com um litro. 
## Deve-se fornecer ao usuário o tempo que será gasto na viagem a sua velocidade média,
## distância percorrida e a quantidade de litros utilizados para fazer a viagem.
## Fórmula: distância = tempo x velocidade.
## litros usados = distância / 12.
vel = int(input("Digite a velocidade média da viagem: "))
tempo = int(input("Digite o tempo gasto na viagem: "))

def calc_qtd_litros(vel,tempo):
    distancia = vel * tempo
    litros_usados = distancia / 12
    return litros_usados

print(f'Para uma viagem com velocidade média de {vel} km/h e gastando {tempo} hora(s), você gastará {calc_qtd_litros(vel,tempo)} litro(s) de combustível.')
