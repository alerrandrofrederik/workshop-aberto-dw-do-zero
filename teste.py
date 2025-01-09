#import
import pandas as pd
import yfinance as yf

# Obter os dados de cotação da Microsoft
commodities = ['MSFT','CL=F'] #lista de commodities que serão buscados

def buscar_dados_commodities(simbolo, periodo='3d', intervalo='1d'):
    """
    Função para buscar os dados de cotação do Yahoo Finance
    que retorna um DataFrame com os dados de cotação
    """
    dat = yf.Ticker(simbolo)                   #buscar os dados do simbolo
    data = dat.history(period="1d")[['Close']] #define o periodo e seleciona a coluna close
    data['simbolo'] = simbolo                  #adicionar a coluna simbolo
    return data                                #retornar os dados como um DataFrame

def buscar_todos_dados_commodities(commodities):
    """
    Função para concatenar os dados de cotação de todos os commodities
    """
    todos_dados = []                                     #lista vazia para armazenar os dados
    for simbolo in commodities:                          # para cada simbolo na lista de commodities
        dados = buscar_dados_commodities(simbolo)        #buscar os dados do simbolo
        todos_dados.append(dados)                        #adicionar os dados a lista
        dados_concatenados = pd.concat(todos_dados)      #concatenar os dados
    return dados_concatenados                            #retornar os dados concatenados como um DataFrame

print(buscar_todos_dados_commodities(commodities))       #imprimir os dados concatenados

'''
Output exemplo:
                                Close simbolo
Date
2025-01-08 00:00:00-05:00  424.559998    MSFT
2025-01-08 00:00:00-05:00   73.040001    CL=F
'''