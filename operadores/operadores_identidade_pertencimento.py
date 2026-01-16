## Operador de identidade 

### Operador is 
### Verifica se dois  são o mesmo objeto na memória, ou seja, ocupam o mesmo endereço de memória, em vez de apenas comparar seus valores.

num1 = 45
num2 = num1

comparacao = num1 is num2
print(comparacao)


## Operador de pertencimento

### Operador in
### É usado para verificar se um elemento está presente em uma coleção, como listas, dicionários ou strings.

estados = ['PE','PB','RN','PI','BA']

busca = 'PE' in estados
print(busca)
