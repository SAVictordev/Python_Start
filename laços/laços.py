## O que é uma estrutura de repetição?

### Uma estrutura de repetição é uma lógica que repete as ações de um mesmo bloco de código por um número de vezes determinado a partir do tipo de estrutura de repetição.


## FOR 

### Estrutura para ler cada item de uma lista

estados = ['PE','PB','RN','PI','BA']

for estado in estados:
    print(estado)
print('Fim do primeiro laço for.')

### Estrutura que lê ao mesmo tempo o indice de cada item em uma lista e o seu conteúdo.

for i in range (5):
    print(i, estados[i])
print('Fim do segundo laço for.')

## While

### Estrutura para aumentar um contador 

cont = 0

while (cont < 5) :
    print(cont)
    cont += 1
print ('Fim do laço while.')