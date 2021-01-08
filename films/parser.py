import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt



HOST = "https://animekisa.tv"
URL = "https://animekisa.tv/latest/1"

HOST2 = "https://rezka.ag/"
URL2 = "https://rezka.ag/cartoons/foreign/"

URL3 = "https://rezka.ag/films/"
HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
              'application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/83.0.4103.116 '
                  'Safari/537.36 '
}

################ parser anime:

@csrf_exempt
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

@csrf_exempt
def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='episode-box test')
    anime = []

    for item in items:
        anime.append(
            {
                'title': item.find('div', class_='title-box-2').get_text(strip=True),
                'image': HOST + item.find('div', class_='image-box').find('img').get('src')
            }
        )
    return anime

@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            anime.extend(get_content(html.text))
            return anime
    else:
        raise ValueError('error in ANIME parser, baby')

################ parser shows:

def get_shows_html(url2, params=''):
    r = requests.get(url2, headers=HEADERS, params=params)
    return r

def get_shows_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    shows = []

    for item in items:
        shows.append(
            {
                'title': item.find('div', class_='b-content__inline_item-link').get_text(strip=True),
                'image': URL2 + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
            }
        )
    return shows

def parser_shows():
    html = get_shows_html(URL2)
    if html.status_code == 200:
        shows = []
        for page in range(0, 1):
            html = get_shows_html(URL2, params={'page': page})
            shows.extend(get_shows_content(html.text))
            return shows

    else:
        raise ValueError('error in SHOWS parser, baby')

#                    parser films:

def get_films_html(url3, params=''):
    r = requests.get(url3, headers=HEADERS, params=params)
    return r

def get_films_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_="b-content__inline_item")
    films = []

    for item in items:
        films.append(
            {
                'title': item.find('div', class_='b-content__inline_item-link').get_text(strip=True),
                'image': URL3 + item.find('div', class_='b-content__inline_item-cover').find('img').get('src')
            }
        )
    return films

def parser_films():
    html = get_films_html(URL3)
    if html.status_code == 200:
        films = []
        for page in range(0, 1):
            html = get_films_html(URL3, params={'page': page})
            films.extend(get_films_content(html.text))
            return films

    else:
        raise ValueError('error in FILMS parser, baby')
