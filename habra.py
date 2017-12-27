import requests
from bs4 import BeautifulSoup
import config

news = []


def habr_news():
    last_news = []
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
    with open('last_news.txt', 'r') as file:
        last_url = file.readline()
    for i in news:
        if i > last_url:
            last_news.append(i)
        with open('last_news.txt', 'w') as f:
            f.write(news[0])
    return last_news
