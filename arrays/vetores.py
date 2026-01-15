## Vetores 

## Vetor é uma estrutura capaz de armazenar uma lista de informações ou um arranjo de valores

estadosvetor = ['PE','PB','RN','PI','BA']
numerosvetor =[1,2.4,3,4,5,6]

## .append() Adiciona um elemento no fim do vetor

estadosvetor.append("AM")
print(estadosvetor)

## .insert() Adiciona um elemento em um índice específico
estadosvetor.insert(1,"RO")
print(estadosvetor)

## .sort() Organiza o array baseado em seus valores ( De forma crescente como padrão e descrecente usando Reverse)

estadosvetor.sort()
print(estadosvetor)

estadosvetor.sort(reverse=True)
print(estadosvetor)

## .pop() função para remover um item do array.
##  O índice do vetor começa em 0, logo o primeiro item do vetor tem o índice 0, e assim sucessivamente.

estadosvetor.pop(2)
print(estadosvetor)

## .count() conta quantas vezes o parâmetro se repete dentro do vetor

print(estadosvetor.count("RO"))

## .clear() limpa a lista completa armazenada

estadosvetor.clear()
print(estadosvetor)

## sum(vetor) Soma de todos os valores (inteiros ou flutuantes) do vetor 
print(sum(numerosvetor))

## len(vetor) mostra o tamanho do vetor (quantos itens tem dentro de um vetor)
print(len(estadosvetor))
print(len(numerosvetor))