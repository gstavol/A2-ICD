import pandas as pd

#cria uma lista vazia, depois cria um dataset com base no csv de filmes
listinha = []
dataset = pd.read_csv('../Filmes.csv')
datand = dataset.values

#é formada uma coluna para cada genero dentre os filmes analisados, mais a primeira coluna para os filmes
headers = ['Filme', 'Animação', 'Família', 'Aventura', 'Comédia', 'Ficção científica', 'Ação', 'Drama', 'Crime', 'Thriller', 'Fantasia', 'Guerra', 'Terror', 'Mistério', 'Romance', 'História', 'Música']
dataset = pd.DataFrame(columns=headers)

rows = []

# cada filme é adicionado como linha do dataset
for filme in datand:
    row = []
    nome = filme[1]
    row.append(nome)
    # é adicionado um valor binario, retornando 1 sempre que o filme (linha) contêm o genero (coluna), para fim de analise de distribuição  
    for genero in headers[1:]:
        if genero in eval(filme[5]):
            row.append(1)
        else:
            row.append(0)
    rows.append(row)

for each_row in rows:
    dataset.loc[len(dataset)] = each_row

#o dataset criado é transformado em um novo arquivo .csv, contendo informações de distribuição de gênero dos filmes analisados
dataset.to_csv("Generos.csv")
