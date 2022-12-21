from helpers import read_bigquery, auth_bq
import os

project='begrowth-user-api-demo'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'data-engineer-test.json'
client=auth_bq(project)

query="""
# INCLUA AQUI A QUERY QUE DESEJA VER O RESULTADO
# NA PASTA sql/ TEMOS ALGUMAS QUERYS PARA PERGUNTAS DO DESAFIO
# EX:
# SELECT * FROM `begrowth-user-api-demo.bg_users.bg_data_enginner_test_lucasAlvarenga` LIMIT 10
# DESCOMENTE A LINHA PARA VER OS RESULTADOS
"""

df=read_bigquery(query=query, client=client)
# PARA VER OS RESULTADOS
print(df)