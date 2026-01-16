velocidade = int(input("Qual a velocidade? unidade de medida: KM/H  "))
tempo = int(input("Qual o tempo? unidade de medida: H  "))

def calc_espaco_percorrido(velocidade, tempo):
    espaco_percorrido = velocidade / tempo
    return espaco_percorrido
 
print((calc_espaco_percorrido(velocidade, tempo)), "KM")
