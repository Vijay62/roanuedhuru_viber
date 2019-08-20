#-*- coding: utf-8 -*-
#libraries
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from urllib.request import Request, urlopen

class News:
    @staticmethod
    def sun():
        req = Request('https://sun.mv', headers={'User-Agent': 'Mozilla/5.0'})
        sun = urlopen(req)
        divs = SoupStrainer('main')
        soup = BeautifulSoup(sun, 'lxml', parse_only=divs)

        news = []

        main_article = []
        main = soup.find('div', class_='component-featured-big')
        main_title = main.find('h1').text
        main_link = main.find('a').get('href')
        main_image = main.find('img').get('src')
        main_article.append(main_title)
        main_article.append(main_link)
        main_article.append(main_image)
        news.append(main_article)
        
        featured_div = soup.find('div', class_='component-featured-thumb --auto-fix-height')
        featured_list = featured_div.find_all('li')
        for featured in featured_list:
            article = []
            title = featured.find('h2').text
            link = featured.find('a').get('href')
            image = featured.find('img').get('src')
            article.extend((title, link, image))
            news.append(article)
        return news

    @staticmethod
    def raajje():
        req = Request('https://raajje.mv', headers={'User-Agent': 'Mozilla/5.0'})
        raajje = urlopen(req)
        soup = BeautifulSoup(raajje, 'lxml')

        news = []

        main_article = []
        main = soup.find('div', class_='main-news')
        main_title = main.find('h2').text
        main_link = main.find('a', class_='text-dark-gray link-hover').get('href')
        main_image = main.find('img').get('src')
        main_article.extend((main_title,main_link,main_image))
        news.append(main_article)

        featured_list =  soup.find_all('div', class_='col-md-6 my-3 priority-news')
        for featured in featured_list:
            article = []
            title = featured.find('h4').text
            link = featured.find('a').get('href')
            image = featured.find('img').get('src')
            article.extend((title, link, image))
            news.append(article)
        return news

    @staticmethod
    def vaguthu():
        req = Request('https://vaguthu.mv', headers={'User-Agent': 'Mozilla/5.0'})
        vaguthu = urlopen(req)
        soup = BeautifulSoup(vaguthu, 'lxml')

        news = []

        main_article = []
        main = soup.find('div', class_='cell small-12 medium-9')
        main_title = main.find('h2').text
        main_link = main.find('a').get('href')
        main_image = main.find('img').get('src')
        main_article.extend((main_title, main_link, main_image))
        news.append(main_article)

        featured_list = soup.find_all('div', class_='cell small-12 medium-3 featured-post-main')
        for featured in featured_list:
            article = []
            title = featured.find('h3').text
            link = featured.find('a').get('href')
            image = featured.find('img').get('src')
            article.extend((title, link, image))
            news.append(article)
        return news
    
    @staticmethod
    def mihaaru():
        req = Request('https://mihaaru.com/', headers={'User-Agent': 'Mozilla/5.0'})
        mihaaru = urlopen(req)
        soup = BeautifulSoup(mihaaru, 'lxml')

        news = []

        main_article = []
        main = soup.find('div', class_='main-news-row main_news_enhanced_size_8')
        main_title = main.find('a',class_='title').text
        main_link = main.find('a').get('href')
        main_image = main.find('img').get('src')
        main_article.extend((main_title, main_link, main_image))
        news.append(main_article)

        featured_list = soup.find_all('div', class_='col-md-2 col-sm-3 col-xs-6 float-right small')
        for featured in featured_list:
            article = []
            title = featured.find('a',class_='title').text
            link = featured.find('a').get('href')
            image = featured.find('img').get('data-src')
            article.extend((title, link, image))
            news.append(article)
        return news


sun = News.sun()
raajje = News.raajje()
vaguthu = News.vaguthu()
mihaaru = News.mihaaru()

#print(raajje)

