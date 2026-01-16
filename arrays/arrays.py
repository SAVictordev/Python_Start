## Array

## Array é uma estrutura capaz de armazenar uma lista de informações ou um arranjo de valores, um vetor multidimensional. 
print("Exemplo de Array\n ")
estados_array = [["PE","PB","RN","PI","BA"],
                ["AM","RO","AC","RR","AP"]]
print(estados_array , "\n")

print("Exemplo de como percorrer o todo o array (usando for em duas direções)\n ")
## Como percorrer o todo o array (usando for em duas direções)
for i in estados_array:
    for j in i:
        print(j)

print("Exemplo de como encontrar um item específico no array\n ")
## Como encontrar um item específico no array
print(estados_array[0][1], "\n")

print("Exemplo de como adicionar um item no array\n ")
## Como adicionar um item no array
estados_array[0].append("CE")
print(estados_array , "\n")

print("Exemplo de como remover um item do array\n ")
## Como remover um item do array
estados_array[0].pop(1)
print(estados_array , "\n")

print("Exemplo de como organizar o array\n ")
## Como organizar o array
estados_array[0].sort()
print(estados_array , "\n")

print("Exemplo de como contar quantos itens tem no array\n ")
## Como contar quantos itens tem no array
print(len(estados_array[0]), "\n")

print("Exemplo de como limpar o array\n ")
## Como limpar o array
estados_array[0].clear()
print(estados_array , "\n")

print("Exemplo de como somar os valores do array\n ")
## Como somar os valores do array
print(sum(estados_array[0]), "\n")


