import requests
from bs4 import BeautifulSoup

LOGIN_URL = 'http://127.0.0.1:8000/login/'

if __name__ == '__main__':
    with requests.Session() as session:
        page = session.get(LOGIN_URL, timeout=10)
        page.raise_for_status()
        soup = BeautifulSoup(page.text, 'lxml')
        token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']
        data = {
            'username': 'test_parser_user', 'password': 'testpassword',
            'csrfmiddlewaretoken': token,
        }
        response = session.post(LOGIN_URL, data=data, timeout=10)
        response.raise_for_status()
        print(response.status_code)
        print(response.text)
