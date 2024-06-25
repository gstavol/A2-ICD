# A2-ICD
trabalho de A2 de introdução a ciência de dados

projeto de scrapping e analise de dados, retirados de themovie Database

Dados retirados de themovie Database, em que se coleta nota (em porcentagem), gênero, orçamento e classificação indicativa filmes são retirados da pagina de "popular" do site, resultando em grande número de filmes recentes/com picos de popularidade, somados com clássicos mais famosos Filmes sem receita, orçamento ou resenhas são descartados.

Resenhas são traduzidas, resumidas e avaliadas pela API da openAI, a nota dada pelo openAI é então comparada com a nota original da review (ou usada para completar reviews incompletas),

Depois de extraidos e tratados, os dados são enviados para arquivos '.csv'
