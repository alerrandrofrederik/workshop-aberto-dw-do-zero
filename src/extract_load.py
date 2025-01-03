#import
import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Obter as variáveis do arquivo .env
load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

# Criar a URL de conexão do banco de dados
DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)


# Lista de commodities
commodities = ['CL=F', 'GC=F', 'SI=F']  # Petróleo bruto, Ouro, Prata

# Extrair os dados de cotação do Yahoo Finance
def buscar_dados_commodities(simbolo, periodo='5d', intervalo='1d'):
    '''
    Função para buscar os dados de cotação do Yahoo Finance
    que retorna um DataFrame com os dados de cotação
    '''
    ticker = yf.Ticker(simbolo)
    dados = ticker.history(period=periodo, interval=intervalo)[['Close']]
    dados['simbolo'] = simbolo #coluna para referenciar o simbolo
    return dados

# concatenar os dados (1..2..3..) -> (1)
def buscar_todos_dados_commodities(commodities):
    '''
    Função para concatenar os dados de cotação de todos os commodities
    '''
    todos_dados = []
    for simbolo in commodities:
        dados = buscar_dados_commodities(simbolo)
        todos_dados.append(dados)
    return pd.concat(todos_dados) #concatenar os dados

# Salvar os dados no banco de dados
def salvar_no_postgres(df, schema='public'):
    '''
    Função para salvar os dados de cotação no banco de dados
    '''
    df.to_sql('commodities', engine, if_exists='replace', index=True, index_label='Date', schema=schema)

# teste
if __name__ == '__main__':
    dados_concatenados = buscar_todos_dados_commodities(commodities)
    salvar_no_postgres(dados_concatenados, schema='public')