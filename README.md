# :rocket: Desafio Mamba Culture

## :bulb: Preparando Ambiente

Primeiramente, precisamos preparar o ambiente para rodar os scripts propostos (lembrando que estou utilizando a versao 3.10.6 do Python e o `pip` como gerenciador de ambiente):
Criando um Env para o projeto
`python3 -m venv challenge_mamba`

Ativando:
`source challenge_mamba/bin/activate`

Instalando as dependencias:
`python3 -m pip install -r requirements.txt`

## :checkered_flag: Rodando a Pipeline

Agora que ja temos o ambiente separado, vamos executar cada etapa da Pipeline. Comecamos com a criacao de usuario na API, para isso, basta executar o script `create_user.py`, ele vai armazenar a resposta num arquivo .json (`auth.json`), que utilizaremos mais tarde":

`python3 create_user.py`

Com a autenticacao, podemos prosseguir para a extracao dos dados da API, o script `get_data.py` vai requisitar os dados, fazer os tratamentos solicitados e salvar o output num arquivo .csv (`data.csv`) para posteriormente carregarmos no BigQuery. No tratamento, utilizamos a biblioteca `geopy` para fazer o **reverse geocode** (poderia ter utilizado a api do Google Maps, mas preferi fazer isso sem muito trabalho de infra).
Para executar o script, rode o comando a seguir:

`python3 get_data.py`

Finalmente, com o output da API tratado devidamente, e com o auxilio das funcoes que estao no script `helpers.py` vamos aplicar o schema, criar a tabela e inserir os dados no BigQuery. Utilizei a insercao a partir de um arquivo csv para isolar os processos. Com o seguinte comando, vamos fechar a pipeline:

`python3 insert_data.py`

## :stars: Resposta as perguntas propostas

    .
    └── sql                 # Arquivos contendo a query que responde a pergunta solicitada (41 -> topico 4.1)

Temos 5 arquivos `.sql` que responde cada uma das perguntas solicitadas no desafio. Para rodar, via python, deixei um script `analysis.py` como template para rodar as queries.

OBS: E necessario incluir o arquivo `data-engineer-test.json` na pasta raiz do repositorio com as credenciais para autenticar com o GCP.
