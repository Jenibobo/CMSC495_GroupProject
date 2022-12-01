import datetime
from django.shortcuts import render
import requests


def index(request):
    today = str(datetime.date.today())

    url = 'https://newsapi.org/v2/everything?q=Climate&from='+ today + '&sortBy=popularity&pageSize=20&apiKey=fbda378575da4f6bb90055f467a1ddab'
    news = requests.get(url).json()

    a = news['articles']
    news_description = []
    news_title = []
    news_img = []
    news_url = []

    for i in range(len(a)):
        article = a[i]
        news_title.append(article['title'])
        news_description.append(article['description'])
        news_img.append(article['urlToImage'])
        news_url.append(article['url'])
    mylist = zip(news_title, news_description, news_url, news_img)
    context = {'mylist': mylist}
    return render(request, 'base.html', context)

    return render(request, 'base.html')
