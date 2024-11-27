
# Analisador de Frequência de Nomes por Estado

Este projeto consulta a API do IBGE para coletar informações sobre a frequência de nomes por estado no Brasil. O código permite buscar dados históricos de nomes, separados por estado e década, e exporta as informações para um arquivo CSV.

## Funcionalidades

- Consulta a API do IBGE para obter dados sobre a frequência de nomes por estado.
- Coleta dados sobre a frequência de nomes em diferentes décadas e seus totais.
- Salva os dados em um arquivo CSV, contendo as colunas:
  - `nome`: Nome pesquisado.
  - `estado`: Estado no qual o nome foi registrado.
  - `decada`: Década do registro.
  - `frequencia`: Número de ocorrências do nome na respectiva década.
  - `frequencia_total_geral`: Soma total das ocorrências do nome ao longo de todas as décadas.


### Como Funciona

O código realiza as seguintes etapas:

1. **Obtenção de dados de estados**: O código consulta a API do IBGE para obter uma lista de estados com seus respectivos IDs.
2. **Coleta de dados de frequência de nomes**: Para cada nome na lista predefinida, o código consulta a API para obter as ocorrências do nome por estado e década.
3. **Geração do arquivo CSV**: Todos os dados coletados são armazenados em um arquivo CSV para fácil análise e manipulação.

## Exemplo de Saída no CSV

O arquivo CSV gerado terá a seguinte estrutura:

```csv
nome,estado,decada,frequencia,frequencia_total_geral
mozart,Acre,1930,5,
mozart,Acre,1940,3,
mozart,Bahia,1930,2,
paulo,Bahia,2000,120,
paulo,Feira de Santana,2010,130,
paulo,Todos os estados,Todas as décadas,,250
...
```

