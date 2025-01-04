# workshop-aberto-dw-do-zero

## Parte 1 - extracao e carregamento de dados

etapa 1 - criação das pastas

etapa 2 - ativar ambiente virtual
```bash
python -m venv .venv
source .venv/scripts/activate
```

etapa 3 - Instala as bibliotecas necessárias
```bash
pip install -r src/requirements.txt
```

etapa 4 - desenvolver scripts extração e carregamento de dados

etapa 5 - criação do banco de dados na render

etapa 6 - salvar dados no banco de dados


## Parte 2 - Transformação de dados com DBT-Core

etapa 1 - Instalar o DBT:
```bash
pip install dbt-core dbt-postgres  
```

etapa 2 - Inicializar DBT-Core:
```bash
dbt init
```

etapa 3 - Configurar o DBT:
- Configure o arquivo profiles.yml para se conectar ao seu Data Warehouse. O arquivo deve estar no diretório ~/.dbt/ ou no diretório especificado pela variável de ambiente DBT_PROFILES_DIR.

Exemplo de profiles.yml:

```yaml
datawarehouse: # Name your project!
  target: dev
  outputs:
    dev:
      type: postgres
      host: "{{ env_var('DB_HOST_PROD') }}"
      user: "{{ env_var('DB_USER_PROD') }}"
      password: "{{ env_var('DB_PASS_PROD') }}"
      port: "{{ env_var('DB_PORT_PROD') | int }}"
      dbname: "{{ env_var('DB_NAME_PROD') }}"
      schema: "{{ env_var('DB_SCHEMA_PROD') }}"
      threads: "{{ env_var('DB_THREADS_PROD') | int }}"
      keepalives_idle: 0
```

obs: Todos os comando do dbt são executados dentro do diretório do dbt.
```bash
cd datawarehouse 
```

etapa 4 - Verificar se a conexão entre o dbt e o banco de dados está ok:
```bash
dbt debug
```

etapa 5 - carregar os dados do excel para o banco de dados:
-obs: no desafio temos uma parte dos dados em um csv e precisamos carregar os dados do excel para o banco de dados, com o dbt basta adicioná-lo na pasta seeds e executar o comando
```bash
dbt seerds
```



