import pandas as pd
from openpyxl import Workbook

# Gera dados fictícios de vendas
def gerar_dados_vendas():
    dados = {
        'Produto': ['Produto A', 'Produto B', 'Produto C', 'Produto D'],
        'Quantidade': [10, 20, 15, 25],
        'Preco_Unitario': [30.0, 15.0, 25.0, 20.0]
    }
    return pd.DataFrame(dados)

# Cria 50 arquivos Excel com dados fictícios de vendas
for i in range(1, 51):
    dados_vendas = gerar_dados_vendas()

    # Cria um novo arquivo Excel
    workbook = Workbook()
    sheet = workbook.active

    # Adiciona os dados ao arquivo Excel
    for index, row in dados_vendas.iterrows():
        sheet.append(row)

    # Salva o arquivo Excel
    nome_arquivo = f"vendas_{i}.xlsx"
    workbook.save(nome_arquivo)

    print(f"Arquivo '{nome_arquivo}' gerado com sucesso.")
