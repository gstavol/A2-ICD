import pandas as pd

listinha = []
dataset = pd.read_csv('./Filmes.csv')
nddata = dataset.values

headers = ['Filme', 'Animação', 'Família', 'Aventura', 'Comédia', 'Ficção científica', 'Ação', 'Drama', 'Crime', 'Thriller', 'Fantasia', 'Guerra', 'Terror', 'Mistério', 'Romance', 'História', 'Música']
dataset = pd.DataFrame(columns=headers)

rows = []
# body

for filme in nddata:
    row = []
    nome = filme[1]
    row.append(nome)
    for genero in headers[1:]:
        if genero in eval(filme[5]):
            row.append(1)
        else:
            row.append(0)
    rows.append(row)

for each_row in rows:
    dataset.loc[len(dataset)] = each_row

dataset.to_csv("Generos.csv")