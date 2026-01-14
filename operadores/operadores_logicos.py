## Operadores de lógicos

## and (Todas as codições precisam ser verdadeiras ao mesmo tempo)

## or ( uma das condições precisam ser verdadeiras)

## not (inverte o valor do resultado da condição, se a condição resultasse normalmente em um verdadeiro, se tornará falso por causa do "not")

num1 = int(input("Digite o primeiro número: "));
num2 = int(input("Digite o segundo número: "));
trueorfalse = True;
                   
if num1 > num2 and num1 / num2 == 0:
    print("As duas condições do and foram atendidas");
elif num1 > num2 or num1 == num2:
    print("Uma das duas condições foram atendidas");
else:
    trueorfalse = not(trueorfalse);
print(trueorfalse);