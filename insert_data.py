from helpers import auth_bq, read_bigquery
from google.cloud.bigquery import LoadJobConfig, SchemaField, SourceFormat
from os import getenv, environ

def write_bigquery_from_csv(file_path, project, dataset_id, table_id):
    client = auth_bq(project)

    BIGQUERY_SCHEMA=[
        SchemaField('id', 'INTEGER', mode='REQUIRED'),
        SchemaField('first_name', 'STRING', mode='NULLABLE'),
        SchemaField('last_name', 'STRING',mode='NULLABLE'),
        SchemaField('email', 'STRING',mode='NULLABLE'),
        SchemaField('gender', 'STRING',mode='NULLABLE'),
        SchemaField('address_geo_latitude', 'FLOAT',mode='NULLABLE'),
        SchemaField('address_geo_longitude', 'FLOAT',mode='NULLABLE'),
        SchemaField('address_country', 'STRING',mode='NULLABLE'),
        SchemaField('address_state', 'STRING',mode='NULLABLE'),
        SchemaField('utm', 'STRING',mode='NULLABLE'),
        SchemaField('cpf', 'INTEGER',mode='NULLABLE'),
        SchemaField('dt_insert', 'DATETIME',mode='NULLABLE'),
        SchemaField('candidate_name', 'STRING', mode='NULLABLE')
    ]

    job_config = LoadJobConfig(
        schema=BIGQUERY_SCHEMA,
        source_format=SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
    )

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    n_rows=read_bigquery(
        query="""SELECT COUNT(*) AS n_rows FROM {}.{}.{}""".format(project, dataset_id, table_id),
        client=client
    )['n_rows'][0]
    
    if n_rows > 0:
        read_bigquery(
            query="""DELETE FROM {} WHERE 1=1""".format(table_ref),
            client=client
        )
        print('deleting {} rows from table'.format(n_rows))
    try:
        with open(file_path, "rb") as source_file:
            job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

        job.result()
        print("Loaded {} rows into `{}.{}`".format(job.output_rows, dataset_id, table_id))
    except Exception as e:
        print('Error loading data into BigQuery: '.format(e))
    finally:
        client.close()
    

if __name__ == '__main__':
    FILE_PATH='data.csv'
    BQ_PROJECT=getenv('BQ_PROJECT', 'begrowth-user-api-demo')
    BQ_DATASET=getenv('BQ_DATASET', 'bg_users')
    BQ_TABLE=getenv('BQ_TABLE', 'bg_data_enginner_test_lucasAlvarenga')
    environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'data-engineer-test.json'

    write_bigquery_from_csv(FILE_PATH, BQ_PROJECT, BQ_DATASET, BQ_TABLE)