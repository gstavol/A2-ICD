import pandas as pd
from functions import get_codes_n_pages, scrapping

# Cabeçalho
headers = ['nome', 'ano de estreia', 'avaliação', 'classificação', 'gêneros', 'orçamento', 'receita', 'resenhas']
dataset = pd.DataFrame(columns=headers)


# Obtém os códigos de filmes das
# primeiras 'codepags' páginas
codepags = 1
codes = get_codes_n_pages(codepags)

# Scrapping dos filmes obtidos
rows = scrapping(codes)

# Corpo
for each_row in rows:
    dataset.loc[len(dataset)] = each_row

dataset.to_csv("Filmes.csv")