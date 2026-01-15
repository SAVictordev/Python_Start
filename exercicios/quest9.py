## 9 - Faça um algoritmo que calcule o IMC (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua condição 

##  Tabela Condições IMC
##  Abaixo de 18,5   | Abaixo do peso          
##  Entre 18,6 e 24,9 | Peso ideal (parabéns)  
##  Entre 25,0 e 29,9 | Levemente acima do peso
##  Entre 30,0 e 34,9 | Obesidade grau I 
##  Entre 35,0 e 39,9 | Obesidade grau II (severa)
##  Maior ou igual a 40 | Obesidade grau III (mórbida)

alt = float(input("Qual sua altura? "))
peso = float(input("Qual o seu peso? "))
imc = (peso/(alt*alt))

if (imc <= 18.5):
    print("Você está abaixo do peso")
elif(imc > 18.5 and imc <= 24.9):
    print("Você está no peso idela, parabéns")
elif (imc >= 25 and imc <= 29.9 ):
    print("Você está levemente acima do peso")
elif((imc >= 30 and imc <= 34.9 )):
    print("Você está com Obesidade grau I")
elif(imc >= 35 and imc <= 39.9):
    print("Você está com Obesidade grau II (Severa)")
else:
    print("Você está com Obessidade grau III (Mórbida)")