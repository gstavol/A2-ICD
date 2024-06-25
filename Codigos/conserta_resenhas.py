import pandas as pd
from gepeto import resumo_gpt_e_nota
import re

dataset = pd.read_csv('../Filmes.csv')
nddata = dataset.values
x = 0

max_len = 0
for filme in nddata:
    if len(eval(filme[-1])) > max_len:
        max_len = len(eval(filme[-1]))

headers_resenhas = ['Filme']
headers_notas = ['Filme']

for x in range(1, max_len + 1, 1):
    headers_resenhas.append("Resenha " + str(x))
    headers_notas.append("Nota " + str(x))

dataset_resenhas = pd.DataFrame(columns=headers_resenhas)
dataset_notas = pd.DataFrame(columns=headers_notas)


for filme in nddata:
    nome = filme[1]
    resenhas_formatadas = []

    resenhas = eval(filme[-1])
    for resenha_nao_formatada in resenhas:
        resenha_formatada = []
        resenha_formatada_gpt = resumo_gpt_e_nota(resenha_nao_formatada)
        if resenha_nao_formatada[0] == '-':
            resenha_formatada = resenha_formatada_gpt
        else:
            diferença = abs(int(re.sub(r'%', '', resenha_nao_formatada[0])) - int(re.sub(r'%', '', resenha_formatada_gpt[0])))
            if diferença > 25:
                resenha_formatada = resenha_formatada_gpt
            else:
                resenha_formatada = [resenha_nao_formatada[0], resenha_formatada_gpt[1]]
        resenhas_formatadas.append(resenha_formatada)
    
    row_resenhas = [nome]
    row_notas = [nome]
    for review in resenhas_formatadas:
        row_notas.append(review[0])
        row_resenhas.append(review[1])
    while len(row_notas) < len(headers_notas):
        row_notas.append('')
        row_resenhas.append('')

    dataset_notas.loc[len(dataset_notas)] = row_notas
    dataset_resenhas.loc[len(dataset_resenhas)] = row_resenhas

dataset_notas.to_csv("Notas.csv")
dataset_resenhas.to_csv("Resenhas.csv")