from bs4 import BeautifulSoup

from browser_session import BrowserHTMLSession

if __name__ == '__main__':
    with BrowserHTMLSession() as session:
        response = session.get('https://httpbin.org/', timeout=20)
        response.raise_for_status()
        response.html.render(sleep=3, timeout=30)
        soup = BeautifulSoup(response.html.html, 'lxml')
        swagger = soup.find(id='swagger-ui')
        print(swagger.prettify())
