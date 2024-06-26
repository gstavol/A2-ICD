# A2-ICD
trabalho de A2 de introdução a ciência de dados

projeto de scrapping e análise de dados

Dados retirados de themovie Database, em que se coleta nota (em porcentagem), gênero, orçamento e classificação indicativa filmes são retirados da página de "popular" do site, resultando em grande número de filmes recentes/com picos de popularidade, somados com clássicos mais famosos Filmes sem receita, orçamento ou resenhas são descartados.

Resenhas são traduzidas, resumidas e avaliadas pela API da openAI, uma nota dada pelo openAI é então comparada com a nota original da review (ou usada para completar reviews incompletas),

Depois de extraídos e tratados, os dados são enviados para arquivos '.csv'
Os arquivos .csv são unidos em planilhas xlsx, então transformadas em peças de análise, sendo um dashboard feito para destrinchar dados de um filme escolhido pelo usuário, um segundo usado para overview de diversos filmes, e um terceiro usado para análise de gêneros específicos. (lista de gêneros dada pelo site) 

São analisadas e plotadas informações como o lucro do filme, a relação entre lucro/avaliação, quais pontos de destaque em cada gênero, a relação entre notas gerais e de análises completas, além de pontos em comum entre todos os filmes, como década de lançamento e distribuição de gêneros

peças de análise contidas nos arquivos "peças.xlsx" e "Peças design 1 & 2.slsx" 
