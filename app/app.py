#import
import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import streamlit as st

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

# Consultar os dados da tabela dm_commodities
def get_data():
    query = f"""
    SELECT
        data,
        simbolo,
        valor_fechamento,
        acao,
        quantidade,
        valor,
        ganho
    FROM
        public.dm_commodities;
    """
    df = pd.read_sql(query, engine)
    return df

# Configurar a página do Streamlit
st.set_page_config(page_title='Dashboard do diretor', layout='wide')

# Título do Dashboard
st.title('Dashboard de Commodities')

# Descrição
st.write("""
Este dashboard mostra os dados de commodities e suas transações.
""")

# Obter os dados
df = get_data()

st.dataframe(df)