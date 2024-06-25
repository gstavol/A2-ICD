import pandas as pd

# Importação da tabela para ndarray
dataset = pd.read_csv('Filmes.csv')
datand = dataset.values

# Cabeçalho da tabela
headers = ['Filme', 'Animação', 'Família', 'Aventura', 'Comédia', 'Ficção científica', 'Ação', 'Drama', 'Crime', 'Thriller', 'Fantasia', 'Guerra', 'Terror', 'Mistério', 'Romance', 'História', 'Música']
dataset = pd.DataFrame(columns=headers)

rows = []

# Corpo da tabela
for filme in datand:
    row = []
    nome = filme[1]
    row.append(nome)

    # Retorna "1" se o filme é do gênero,
    # e uma string vazia caso contrário  
    for genero in headers[1:]:
        if genero in eval(filme[5]):
            row.append(1)
        else:
            row.append("")
    rows.append(row)

# Término da tabela
for each_row in rows:
    dataset.loc[len(dataset)] = each_row

dataset.to_csv("Generos.csv")
