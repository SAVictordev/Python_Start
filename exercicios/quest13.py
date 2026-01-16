## Faça algoritmo que leia o nome e a idade de uma pessoa e imprima na tela o nome da pessoa e se ela é maior ou menor de idade. 

nome = str(input("Qual o seu nome? "))
idade = int(input("Qual a sua idade? "))

if (idade > 0 and idade < 18):
    print("Olá, ",nome, "você é menor de idade!")
elif(idade > 18):
    print("Olá ",nome, " você é maior de idade")
else:
    print("Idade inválida")