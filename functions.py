import requests
from bs4 import BeautifulSoup
import re

# Expressões regulares
find_num = r"movie/(\d+)-"

# Função para obter o texto do parágrafo
# que contenha uma palavra-chave
def get_p_info(p_elements, info):
    for p in p_elements:
        if info in p.text:
            info_text = p.text.strip()
    return info_text

# Obtém os códigos dos filmes das primeiras "n paginas"
def get_codes_n_pages(n):
    # Troca o idioma do site para inglês
    headers = {
    'Accept-Language': 'en-US,en;q=0.9'
    }
    codes = []
    for x in range(n):
        url = "https://www.themoviedb.org/movie?page=" + str(x)
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.text, "lxml")
        codes_raw = soup.find_all("h2")[4:]
        for code in codes_raw:
            name = re.findall(find_num, str(code))
            codes.append(name[0])
    return codes
