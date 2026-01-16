## Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. Imprima na tela as duas temperaturas.

## Fórmula: C = (5 * ( F-32) / 9)

temperatura_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
temperatura_celsius = (5 * (temperatura_fahrenheit - 32) / 9)

print("A temperatura em Fahrenheit é: ", temperatura_fahrenheit)
print("A temperatura em Celsius é: ", temperatura_celsius)
