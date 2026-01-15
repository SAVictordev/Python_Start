## O que são estruturas condicionais?

### A estrutura condicional é uma seção que ajuda a definir condições para a execução de determinados blocos de comandos.
### No lugar de executar tudo de vez, sem nenhuma interrupção, o programa deve parar para executar um teste e decidir qual caminho seguir.

#### IF ( SE A CONDIÇÃO FOR VERDADEIRA PARA O CÓDIGO AO EXECUTAR O QUE HÁ DENTRO DO IF)

estado = 'PE';

if (estado == 'PE') :
    print("Estado encontrado na primeira instância");

#### ELIF (SERÁ CONFERIDO CASO A CONDIÇÃO ANTERIOR NÃO SEJA VERDADEIRA E VERIFICA A PRÓXIMA CONDIÇÃO, CASO SEJA VERDADEIRA O CÓDIGO PARA AO EXECUTAR O QUE HÁ DENTRO DO ELIF)

if (estado == 'RJ'):
    print("Estado encontrado na primeira instância");
elif (estado == 'PE'):
    print('Estado encontrado na segunda instância');

### ELSE SERÁ A ÚLTIMA CONDIÇÃO A SER ATENDIDA, É O CASO GERAL PARA QUANDO AS EXECEÇÕES NÃO FOREM ATENDIDAS

if (estado == 'RJ'):
    print("Estado encontrado na primeira instância");
elif (estado == 'PB'):
    print('Estado encontrado na segunda instância');
else:
    print('Estado não encontrado');