##  10 - Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

## Solução inicial
nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))

nota_med = ((nota1 + nota2 + nota3)/3)

print("Sua média é: ", nota_med)

## Solução usando metodos de vetores

vetor_nota = [nota1, nota2, nota3]

print ("Sua média é: ",media := (sum(vetor_nota) / len(vetor_nota)))
