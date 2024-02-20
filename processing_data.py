import pandas as pd

# Função responsável pelo processamentos dos dados
def processing_data(selected_df, new_file_name):
    # selecionamos as colunas do dataFrame que contéms strings, e aplicamos a função str.lower() para passar todas as letras da determinada coluna para letras minúsculas
    selected_df[selected_df.select_dtypes(include=['object']).columns] = selected_df.select_dtypes(include=['object']).apply(lambda x: x.str.lower())
    # Fazemos a mesma seleção de colunas, mas ao invés de passar as letras para minúsculas, nós agora usamos a função str.replace para substituir todos os caracteres não alfanuméricos na string ""
    # A expressão regular '[^a-zA-Z\s]+' removerá os caracteres especiais com excessão do caracter " " (o espaço em branco)
    selected_df[selected_df.select_dtypes(include=['object']).columns] = selected_df.select_dtypes(include=['object']).apply(lambda x: x.str.replace(r'[^a-zA-Z\s]+', '', regex=True))
    selected_df.to_csv(new_file_name, index=False)  # Com os dados processados, apenas salvamos os mesmos
                                                    # em um novo arquivo csv, na pasta especificada

# Lendo os arquivos que foram criados com os dados
people_df = pd.read_csv("raw/people.csv")
planets_df = pd.read_csv("raw/planets.csv")
films_df = pd.read_csv("raw/films.csv")

# Fazendo as chamadas da função para processar os dados de todos os dataFrames
processing_data(people_df, "work/new_people.csv")
processing_data(planets_df, "work/new_planets.csv")
processing_data(films_df, "work/new_films.csv")