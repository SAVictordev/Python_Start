## Operador de identidade 

### Operador is 
### Verifica se dois  são o mesmo objeto na memória, ou seja, ocupam o mesmo endereço de memória, em vez de apenas comparar seus valores.

num1 = 45;
num2 = num1;

resp = num1 is num2;
print(resp);


## Operador de pertencimento

### Operador in
### É usado para verificar se um elemento está presente em uma coleção, como listas, dicionários ou strings.

estados = ['PE','PB','RN','PI','BA'];

resp2 = 'PE' in estados;
print(resp2);
