# Formatação de resultado vazio
def noneformat(texto):
    if texto != None:
        texto = texto.text.strip()
    else:
        texto = '-'
    return texto

# Modulos de limpeza

def limpa_ano(ano):
    return ano.strip().replace("(", "").replace(")", "")

def limpa_genero(genero):
    return genero.strip().replace('\xa0',"")

def limpa_orcamento(orcamento):
    return orcamento.replace('Orçamento ', "")

def limpa_receita(receita):
    return receita.replace('Receita ', "")