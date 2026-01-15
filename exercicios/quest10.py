##  10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

## Solução inicial
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

notamed = ((nota1 + nota2 + nota3)/3)

print("Sua média é: ", notamed)

## Solução usando metodos de vetores

vetornota = [nota1, nota2, nota3]

print ("Sua média é: ",média := (sum(vetornota) / len(vetornota)))
