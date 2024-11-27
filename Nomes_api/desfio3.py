import requests
import csv

# Consultar a API para obter os estados com seus IDs
url_estados = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos?orderBy=nome'
response_estados = requests.get(url_estados)

if response_estados.status_code == 200:
    localidade = response_estados.json()

    # Dicionário para armazenar estados com seus IDs
    lista_estado = {}
    for estado in localidade:
        lista_estado[estado['municipio']['microrregiao']['mesorregiao']['UF']['nome']] = \
            estado['municipio']['microrregiao']['mesorregiao']['UF']['id']
else:
    print("Erro ao consultar a API de estados.")
    exit()

# Lista de nomes (os 10 escolhidos)
lista_nomes = ["mozart", "paulo", "maria", "gustavo", "paula", 
               "jaqueline", "ricardo", "vivane", "daniele", "clara"]

# Nome do arquivo CSV
nome_arquivo = "dados_nomes_com_total.csv"

# Criar e abrir o arquivo CSV para escrita
with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    
    # Escrever o cabeçalho no CSV
    escritor.writerow(["nome", "estado", "decada", "frequencia", "frequencia_total_geral"])
    
    # Iterar pelos nomes para calcular o total geral
    for nome in lista_nomes:
        frequencia_total_geral = 0  # Somatório geral para o nome
        
        for estado, estado_id in lista_estado.items():
            # Construir a URL
            url = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}?localidade={estado_id}'
            
            # Fazer a requisição
            response = requests.get(url)
            
            if response.status_code == 200:
                # Processar os dados retornados
                dados = response.json()
                
                for item in dados:
                    if 'res' in item:
                        for decada in item['res']:
                            frequencia_total_geral += decada['frequencia']
                            # Escrever os dados no arquivo CSV
                            escritor.writerow([nome, estado, decada['periodo'], decada['frequencia'], ""])
            else:
                print(f"Erro ao consultar nome: {nome} no estado: {estado} (Status: {response.status_code})")
        
        # Adicionar a linha com o total geral para o nome
        escritor.writerow([nome, "Todos os estados", "Todas as décadas", "", frequencia_total_geral])

print(f"Dados salvos no arquivo '{nome_arquivo}'.")