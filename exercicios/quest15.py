##  Faça um algoritmo que leia o ano em que uma pessoa nasceu, imprima na tela quantos anos, meses e dias essa pessoa ja viveu. Leve em 
##  consideração o ano com 365 dias e o mês com 30 dias.
##  (Ex: 5 anos, 2 meses e 15 dias de vida)

from datetime import date

data_atual = date.today()
dia_nascimento = int(input("Qual o dia do seu nascimento?"))
mes_nascimento = int(input("Qual o mês que você nasceu? Obs: 1 - Janeiro & 12 - Dezembro "))
ano_nascimento = input("Qual o seu ano de nascimento? Ex: 2000: ")

if ((dia_nascimento > 0 and dia_nascimento <= 30) and (mes_nascimento >= 1 and mes_nascimento <= 12) and (len(ano_nascimento) == 4 and ano_nascimento.isdigit())):
    
    ## Manipulação das datas 
    ano_nascimento = int(ano_nascimento) ##   transforma o anonascimento em um valor inteiro para ser manipulado matemáticamente
    data_nascimento = date(ano_nascimento, mes_nascimento, dia_nascimento) ## manipula as informações inputadas para o padrão de data (ano,mês,data), para que possa ser comparada a data estipulada pelo metodo date.today()
    if(data_nascimento <= data_atual):
        diferença_datas = data_atual - data_nascimento ## faz a diferença matemática da data atual para a data inputada e retorna um valor com padrão em dias e horas
    ## Calculando anos, meses e dias 
        dias_totais = diferença_datas.days ## transforma o padrão diferença em somente dias
        dias_em_anos = (dias_totais // 365) ## operação matemática simples para obter apenas a quantidade de anos sem considerar os valores quebrados (dias que não formam 1 ano completo)
        resto_de_ano = (dias_totais % 365) ## mesma coisa que o passo anterior, sendo que aqui, no lugar de obter a divisão inteira, queremos os valores quebrados para descobrir quantos meses excedentes temos
        resto_de_ano_em_meses = resto_de_ano // 30 ## mesma ideia de obter a quantidade exata de meses por meio de uma divisão inteira
        dias_restantes = resto_de_ano_em_meses % 30 ## mesma ideia de obter o resto da divisão para saber quantos dias que não formam 1 mês
        print("Você tem ", dias_em_anos,"ano(s)", resto_de_ano_em_meses," mes(es) e ", dias_restantes," dia(s).")
    else:
        print("Data de nascimento inválida")  

elif ((len(ano_nascimento) != 4 and ano_nascimento.isdigit())): ## Tratamento para validação da escrita do ano
    print("Ano de nascimento inválido")
elif((dia_nascimento < 0 or dia_nascimento > 30)): ## Tratamento para validação da data
    print("Data inválida")
elif(mes_nascimento < 1 or mes_nascimento > 12): ## Tratamento para validação do mês
    print("Mês inválido")


