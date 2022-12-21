from cryptography.fernet import Fernet
from geopy.geocoders import Nominatim
from pandas import DataFrame
from google.cloud import bigquery


def get_state(lat, lon):
    """
        Get state from latitude and longitude
    """
    geolocator = Nominatim(user_agent="geoapiExercises")
    location=str(geolocator.reverse(str(lat)+","+str(lon))).split(',')
    state=location[-4]
    if 'Região' in state:
        state=location[-3]
    return state.strip()

def decrypt_cpf(cpf, fernet_key):
    """
        Decrypt cpf based on fernet key
    """
    fernet=Fernet(fernet_key)
    return fernet.decrypt(cpf.encode()).decode()

def read_bigquery(query, client):
    """
        Read bigquery data and return a pandas dataframe
    """
    query_job = client.query(query)
    dataframe = (
        query_job
        .result()
        .to_dataframe()
    )
    return dataframe

def auth_bq(project):
    """
        Authenticate to bigquery
    """
    client = bigquery.Client(project=project)
    return client
