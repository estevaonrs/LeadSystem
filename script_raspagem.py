import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL da página
url = 'https://pt.wikipedia.org/wiki/Lista_de_municípios_do_Ceará_por_população'

# Requisição para a página
response = requests.get(url)

# Verificar se a requisição foi bem sucedida
if response.status_code == 200:
    # Analisar o conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontrar a tabela pelo seu atributo class
    table = soup.find('table', {'class': 'wikitable sortable'})

    # Inicializar uma lista para armazenar os dados
    data = []

    # Iterar pelas linhas da tabela, pulando o cabeçalho
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        if cols:
            # Extrair os dados das colunas
            pos = cols[0].text.strip()
            municipio = cols[1].text.strip()
            populacao = cols[2].text.strip()

            # Adicionar os dados à lista
            data.append([pos, municipio, populacao])

    # Criar um DataFrame com os dados
    df = pd.DataFrame(data, columns=['Posição', 'Município', 'População'])

    # Salvar os dados em um arquivo Excel
    df.to_excel('lista_municipios_ceara_populacao.xlsx', index=False)

    print('Dados salvos com sucesso em lista_municipios_ceara_populacao.xlsx')
else:
    print('Falha na requisição da página')
