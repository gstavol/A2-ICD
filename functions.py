import requests
from bs4 import BeautifulSoup
import re
import limpeza

# Função para obter o texto do parágrafo
# que contenha uma palavra-chave
def get_p_info(p_elements, info):
    for p in p_elements:
        if info in p.text:
            info_text = p.text.strip()
    return info_text

# Função para obter o texto do href
# de um elemento html
def find_href(elemento):
    match = re.search(r'<a\s+href="([^"]*)"', str(elemento))
    if match: return match.group(1)
    else: return '-'


# Obtém os códigos dos filmes 
# das primeiras "n paginas"
def get_codes_n_pages(n):
    codes = []
    for x in range(1, n, 1):
        url = "https://www.themoviedb.org/movie?page=" + str(x)
        page = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.9'})
        soup = BeautifulSoup(page.text, "lxml")
        codes_raw = soup.find_all("h2")[4:]
        for code in codes_raw:
            name = re.findall(r"movie/(\d+)-", str(code))
            if name:
                codes.append(name[0])
    return codes

# Retorna uma lista com as resenhas do
# filme de código "code"
def get_reviews_from_code(code):
    reviews = []
    url = 'https://www.themoviedb.org/movie/' + code
    response = requests.get(url, allow_redirects=True)
    url = response.url + '/reviews'
    page = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.9'})
    soup = BeautifulSoup(page.text, "lxml")
    cards = soup.find_all("div", {"class": "card"})
    
    # Para cada resenha, obtém o texto e a nota
    for card in cards:
        info = card.find("div", {"class":'info'})
        nota = limpeza.noneformat(info.find("div", {"class":'rating_border rating'}))

        link = 'https://www.themoviedb.org' + find_href(info.find("h3"))
        pagina = requests.get(link, headers={'Accept-Language': 'en-US,en;q=0.9'})
        sopa = BeautifulSoup(pagina.text, "lxml")
        elementos_p = sopa.find_all("p")
        texto_resenha_lista = []
        for elemento_p in elementos_p:
            elemento_p = elemento_p.text.strip()
            texto_resenha_lista.append(elemento_p)
        texto_resenha = '\n'.join(texto_resenha_lista[:-2])
        reviews.append([nota, texto_resenha])
    return(reviews)

# Scrapping dos filmes
def scrapping(codes):
    film_list = []
    for y in range(len(codes)):
        url = "https://www.themoviedb.org/movie/" + codes[y]
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "lxml")

        # Otimização
        p_elements = soup.find_all('p')
        h2_elements = soup.find('h2')
        
        # Obtenção dos elementos
        nome = h2_elements.find('a').text.strip()
        ano = limpeza.limpa_ano(h2_elements.find('span').text)
        score = re.findall(r'icon-r(\w{2})', str(soup.find('div', {'class':'percent'})))
        classification = limpeza.noneformat(soup.find('span', {'class':'certification'}))
        genres = limpeza.limpa_genero(soup.find('span', {'class':'genres'}).text).split(',')
        budget = limpeza.limpa_orcamento(get_p_info(p_elements, 'Orçamento'))
        revenue = limpeza.limpa_receita(get_p_info(p_elements, 'Receita'))
        reviews = get_reviews_from_code(codes[y])

        # Adiciona o scrapping do filme à lista
        if reviews and budget!='-' and revenue!='-':
            film_list.append([nome, ano, score[0], classification, genres, budget, revenue, reviews])
            print(codes[y])

    return film_list
