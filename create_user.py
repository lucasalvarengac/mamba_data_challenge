import requests
import os

API_ACCESS_URL = os.getenv('API_ACCESS_URL', 'https://begrowth.deta.dev/user/')
FULL_NAME = os.getenv('FULL_NAME', 'Lucas Alvarenga')
EMAIL = os.getenv('EMAIL', 'lucas.alvarenga92@gmail.com')

if __name__ == '__main__':
    response=requests.post(
        url=API_ACCESS_URL, 
        json={
            'full_name': FULL_NAME,
            'email': EMAIL
        },
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
    )

    with open('auth.json', 'w') as file:
        file.write(response.text)