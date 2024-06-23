################### ROTEIRO ###################
# Conseguir os IDs (OK)
# Pesquisar os IDs no TMDB (OK)
# Obter: nome(OK), ano de lançamento(OK), 
# avaliação(OK), classificação(OK), depoimentos
# e info de usuários
###############################################

################### LEGENDA ###################
# Comentário (pronto)
#&&& Ainda falta fazer
###############################################

import requests
import pandas as pd
from bs4 import BeautifulSoup
import re
from functions import get_codes_n_pages, get_p_info


# Expressões regulares
find_parenteses = r'\([^)]*\)'
find_score = r'icon-r(\w{2})'


# Formatação da tabela
lines = []
titles = ['nome', 'ano de estreia', 'avaliação', 'classificação', 'gêneros', 'orçamento', 'receita']

# Obtém os códigos de filmes das
# primeiras 'codepags' páginas
codepags = 1
codes = get_codes_n_pages(codepags)


# Scrapping dos filmes
for y in range(len(codes)):
    url = "https://www.themoviedb.org/movie/" + codes[y]
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "lxml")
    p_elements = soup.find_all('p')
    name_ano = soup.find('h2')
    name = name_ano.find('a').text.strip()
    ano = name_ano.find('span').text.strip().replace("(", "").replace(")", "")
    score = re.findall(find_score, str(soup.find('div', {'class':'percent'})))
    classification = soup.find('span', {'class':'certification'})
    if classification != None:
        classification = classification.text.strip()
    else:
        classification = '-'
    genres = soup.find('span', {'class':'genres'}).text.strip().replace('\xa0',"").split(',')
    budget = get_p_info(p_elements, 'Orçamento').replace('Orçamento ', "")
    revenue = get_p_info(p_elements, 'Receita').replace('Receita', "")
    lines.append([name, ano, score[0], classification, genres, budget, revenue])
    
print(lines)