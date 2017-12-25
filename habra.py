import requests
from bs4 import BeautifulSoup
import config

def habr_news():
    news = []
    habr = requests.get(config.habr).text
    soup = BeautifulSoup(habr, 'lxml')
    div = soup.find_all('div', {'class': 'posts_list'})
    for zagolovok in div:
        post = zagolovok.find_all('h2', {'class': 'post__title'})
        for links in post:
            links = links.find_all('a')
            for link in links:
                link = link.get('href')
                news.append(link)
    return news