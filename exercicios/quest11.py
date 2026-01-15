##  Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas,
##  imprima na tela o nome do aluno e se o aluno foi aprovado ou reprovado.
##  para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.


nome = str(input("Digite o nome do aluno: "))
nota1 = int(input("Digite a primeira nota do aluno: "))
nota2 = int(input("Digite a segunda nota do aluno: "))
nota3 = int(input("Digite a terceira nota do aluno: "))
nota4 = int(input("Digite a quarta nota do aluno"))

notasvetor = [nota1, nota2, nota3, nota4]
mediaaluno = sum(notasvetor)/len(notasvetor)

if (mediaaluno >= 7) :
    print("Aluno",nome, " aprovado!")
else:
    print("Aluno",nome, " reprovado!")