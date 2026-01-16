## Francisco tem 1,50m e cresce 2 centímetros por ano, enquanto Sara tem 1,10m e cresce 3 centímetros por ano.
## Faça um algoritmo que calcule e imprima na tela em quantos anos serão necessários para que Sara seja maior que Francisco.

altura_inicial_francisco = 1.50
altura_inicial_sara = 1.10
taxa_crescimento_francisco = 0.02
taxa_crescimento_sara = 0.03
anos = 0

while altura_inicial_francisco > altura_inicial_sara:
    altura_inicial_francisco += taxa_crescimento_francisco
    altura_inicial_sara += taxa_crescimento_sara
    anos += 1

print(f'Serão necessários {anos} anos para que Sara seja maior que Francisco.')
