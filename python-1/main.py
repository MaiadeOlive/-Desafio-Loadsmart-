# coding=utf-8
# Todas as perguntas são referentes ao arquivo `data.csv`
# Você * não * pode utilizar o pandas e nem o numpy para este desafio.

import csv

raw_data = []

with open('data.csv', mode='r', encoding="utf8")as dp:  # dados jogadores

    linha = csv.reader(dp)

    for dinfo in linha:
        raw_data.append(dinfo)


# *Q1.* Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?

def q_1():
    nacionalidades = set()
    column_num = [a.lower().strip() for a in raw_data[0]].index('nationality')
    for c in raw_data[1:]:
        nacionalidades = nacionalidades.union([c[column_num]])

    num_nacionalidades = len(nacionalidades)
    return num_nacionalidades


print(q_1())


# *Q2.* Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    clubes = set()  # cria um conjunto de itens unicos
    for c in raw_data[1:]:
        clubes = clubes.union([c[3]])

    num_clubes = len(clubes)
    return num_clubes

print(q_2())

# *Q3.* Liste o nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.

def q_3():
    nomes = []
    for i in range(1, 21):
        c = raw_data[i]
        nomes.append(c[2])

    return nomes

print(q_3())

# *Q4.* Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    sub_lista = [[c[2], float(c[17])] for c in raw_data[1:]]
    sub_lista.sort(reverse=True, key=lambda x: x[1])
    sublista = sub_lista[:10]
    jogadores_salario = [i[0] for i in sublista]
    return jogadores_salario

print(q_4())


# *Q5.* Quem são os 10 jogadores mais velhos?
def q_5():
    lista_idade = [[c[2], int(c[6])] for c in raw_data[1:]]
    lista_idade.sort(reverse=True, key=lambda x: x[1])
    listaidade = lista_idade[:10]
    jogadores_idade = [i[0] for i in listaidade]
    return jogadores_idade

print(q_5())


# *Q6.* Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.
def q_6():
    lista_idade = []

    for c in raw_data[1:]:
        lista_idade.append(int(c[6]))
    contador_idade = {}

    for i in lista_idade:
        if i in contador_idade.keys():
            contador_idade[i] += 1
        else:
            contador_idade[i] = 1

    return contador_idade

print(q_6())
     

