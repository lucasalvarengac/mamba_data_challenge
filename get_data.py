from requests import get
from pandas import DataFrame
from datetime import datetime
from helpers import decrypt_cpf, get_state
from json import load
from os import getenv

def get_data(api_url, fernet_key):
    response=get(
        url=api_url
    )
    date_etl=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data=[
        {
            'id': row['id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'email': row['email'],
            'gender': row['gender'],
            'address_geo_latitude': row['address']['geo_latitude'],
            'address_geo_longitude': row['address']['geo_longitude'],
            'address_country': row['address']['country'],
            'address_state': get_state(row['address']['geo_latitude'], row['address']['geo_longitude']),
            'utm': row['utm'],
            'cpf': decrypt_cpf(row['cpf'], fernet_key),
            'dt_insert': date_etl,
            'candidate_name': 'Lucas Alvarenga'
        } for row in response.json()
    ] 
    data=DataFrame(data)
    return data

if __name__ == "__main__":
    AUTH_JSON=load(open('auth.json'))
    API_DATA_URL=getenv('API_DATA_URL', 'https://begrowth.deta.dev/token')
    API_URL='{}={}'.format(API_DATA_URL, AUTH_JSON['API Token'])
    FERNET_KEY=b'ekkxXo0uHWRkIbHqHrLS4gaMj2hWTYMJyPTAbi9INGI='
    try:
        data=get_data(api_url=API_URL, fernet_key=FERNET_KEY)
        data.to_csv('data.csv', index=False, header=True)
        print('Data saved to data.csv')
    except Exception as e:
        print('Error: {}'.format(e))

