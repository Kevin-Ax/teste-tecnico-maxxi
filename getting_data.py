import requests
import csv

# função que fará a a chama das requisições, extração dos dados e passará para os arquivos passados como parâmetro
def get_data_from_API(file_name, api_url):
    files_path = file_name    #Criando o path e o arquivo para inserção dos dados
    with open(files_path, mode='w', newline='') as file:    # Iniciando o processo de escrita no arquivo criado
        res = requests.get(api_url + "1")    # Fazendo a requisição da primeira página de forma separada, para já
                                                                # sabermos os nomes dos campos que serão escritos no arquivo e fazer
                                                                # as colunas do nosso csv
        # já que já temos os primeiros dados, vamos escrevê-los no arquivo
        if res.status_code == 200:
            data = res.json()   # Pegando os dados da reposta da API
            writer = csv.DictWriter(file, data.keys())  # Criando o escritor do arquivo
            writer.writeheader()    # Escrevendo o 'cabeçalho' do csv
            writer.writerow(data)   # Escrvenedo a primeira linha 
            # agora precisamos escrever as outroas linhas do arquivo, com as 4 páginas restantes da API
            for i in range(2,5):
                # fazendo a url para a requisição, agora para cada página
                url_people = api_url + str(i)
                # fazendo a requisição para a api 
                res = requests.get(url_people)
                if res.status_code == 200:
                    data = res.json()   # Pegando os dados da resposta
                    writer.writerow(data)   # Escrevendo a respectiva linha no arquivo

# Chamando as funções para criação de todos os dataFrames
get_data_from_API("raw/people.csv", "https://swapi.dev/api/people/")
get_data_from_API("raw/planets.csv", "https://swapi.dev/api/planets/")
get_data_from_API("raw/films.csv", "https://swapi.dev/api/films/")