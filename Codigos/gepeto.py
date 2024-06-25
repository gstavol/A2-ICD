from openai import OpenAI

# Recebe uma lista [nota, resenha].
# Traduz e resume a resenha, depois
# gera uma nota para o filme e
# retorna uma lista [nota, resenha]

def resumo_gpt_e_nota(lista_recebida):
    client = OpenAI(api_key='')

    prompt = [{"role":"user", "content":'''
        Resuma a seguinte resenha, como se fosse você quem escreveua resenha. Evite termos como "a resenha", "uma crítica":
        {lista_recebida[1]}
        Dê também uma nota que reflita esta resenha para o filme.
        Lembre-se que a nota deve ser condizente com a resenha.
        A sua resposta deve ser formatada da seguinte forma:
        ['NOTA', 'RESUMO']
        A nota deve estar no formato XX%.
        Lembre-se de adicionar os apóstrofos e colchetes.
        A sua resposta não deve conter nada além disso.
            '''
            }]

    response = client.chat.completions.create(
        messages = prompt,
        model = 'gpt-3.5-turbo-0125',
        max_tokens = 1200,
        temperature = 1
    )

    return eval(response.choices[0].message.content)