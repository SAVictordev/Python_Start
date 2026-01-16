## Faça um algoritmo que efetue o cálculo do salário líquido de um professor.
## As informações fornecidas serão: valor da hora aula, número de aulas lecionadas no mês e percentual de desconto do INSS. Imprima na tela o salário líquido final.

valor_hora_aula = float(input("Digite o valor da hora aula: "))
qtd_horas_aula_dia = int(input("Digite o número de horas aula: "))
numero_aulas = int(input("Digite o número de aulas lecionadas no mês: "))
inss = float(input("Digite o percentual de desconto do INSS: "))

def calc_salario_liquido(a,b,c,d):
    salario_liquido = (a * b * c) - d
    return salario_liquido

print(calc_salario_liquido(valor_hora_aula, qtd_horas_aula_dia, numero_aulas, inss))