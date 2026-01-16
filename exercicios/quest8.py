## Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

## Forma com metódos de array
num1 = 0
num2 = 5
num3 = 10

vetor_num = [num1, num2, num3]

vetor_num.sort(reverse=True)
print(vetor_num)

## Forma pura com condicionais

if (num1 >= num2 >= num3 ):
    print(num1,num2,num3)
elif(num1 >= num3 >= num2):
    print(num1,num3,num2)
elif(num2 >= num1 >= num3):
    print(num2,num1,num3)
elif(num2 >= num3 >= num1):
    print(num2,num3,num1)
elif(num3 >= num1 >= num2):
    print(num3,num1,num2)
else:
    print(num3,num2,num1)
