import concurrent.futures
import openpyxl
import requests

# Função para fazer requisições à API Fipe
def make_request(endpoint, params=None):
    base_url = "https://parallelum.com.br/fipe/api/v2"
    url = f"{base_url}{endpoint}"
    response = requests.get(url, params=params)
    return response.json() if response.status_code == 200 else None

# Função para buscar o histórico de preços e adicionar à lista
def fetch_and_append_data(vehicle_type, brand, model, data_to_append):
    # Obtendo anos para o modelo
    years = make_request(f'/{vehicle_type}/brands/{brand["code"]}/models/{model["code"]}/years')
    if years:
        for year in years:
            # Obtendo o histórico de preços para o ano específico
            history_info = make_request(f'/{vehicle_type}/brands/{brand["code"]}/models/{model["code"]}/years/{year["code"]}/history')
            if history_info:
                for price_entry in history_info.get('priceHistory', []):
                    # Adicionando dados ao histórico de preços
                    data_row = [
                        vehicle_type,
                        brand["name"],
                        model["name"],
                        year["name"],
                        price_entry["month"],
                        price_entry["price"]
                    ]
                    data_to_append.append(data_row)

# Função para popular uma tabela Excel com informações da API Fipe
def populate_excel():
    # Criar um novo arquivo Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Adicionar cabeçalho
    sheet.append(['Vehicle Type', 'Brand', 'Model', 'Year', 'Month', 'Price'])

    # Populando a tabela com dados da API Fipe
    vehicle_types = ['cars', 'motorcycles', 'trucks']
    data_to_append = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for vehicle_type in vehicle_types:
            print(f'Processing {vehicle_type}')
            # Obtendo marcas para o tipo de veículo
            brands = make_request(f'/{vehicle_type}/brands')
            if brands:
                for brand in brands:
                    # Obtendo modelos para a marca
                    models = make_request(f'/{vehicle_type}/brands/{brand["code"]}/models')
                    if models:
                        for model in models:
                            # Adicionando tarefa de busca e inserção
                            futures.append(
                                executor.submit(fetch_and_append_data, vehicle_type, brand, model, data_to_append)
                            )

    # Aguardar a conclusão de todas as operações
    concurrent.futures.wait(futures)

    # Adicionar dados à planilha
    for data_row in data_to_append:
        sheet.append(data_row)

    # Salvar o arquivo Excel
    workbook.save('fipe_history_prices.xlsx')

if __name__ == "__main__":
    populate_excel()