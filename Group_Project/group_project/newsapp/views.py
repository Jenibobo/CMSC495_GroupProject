from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient


# Create your views here.

# global vars
newsapi = NewsApiClient(api_key="492204b5fab24074b7e237e955eb3218")

def Sports(request):
    top_sports= newsapi.get_top_headlines(category="sports")

    s_articles = top_sports["articles"]
    sport_desc = []
    sport_title = []
    sport_img = []
    sport_url = []

    for i in range(len(s_articles)):
        f = s_articles[i]
        sport_title.append(f["title"])
        sport_desc.append(f["description"])
        sport_url.append(f["urlToImage"])
        sport_img.append(f["url"])
    mylist = zip(sport_title, sport_desc, sport_img, sport_url)
    return render(request, "sports.html", context={"mylist": mylist})


def Technology(request):
    top_tech = newsapi.get_top_headlines(category="technology")

    t_articles = top_tech["articles"]
    tech_desc = []
    tech_title = []
    tech_img = []
    tech_url = []

    for i in range(len(t_articles)):
        f = t_articles[i]
        tech_title.append(f["title"])
        tech_desc.append(f["description"])
        tech_url.append(f["urlToImage"])
        tech_img.append(f["url"])
    mylist = zip(tech_title, tech_desc, tech_img, tech_url)
    return render(request, "technology.html", context={"mylist": mylist})


def Entertainment(request):
    top_entertainment = newsapi.get_top_headlines(category="entertainment")

    e_articles = top_entertainment["articles"]
    Entertainment_desc = []
    Entertainment_title = []
    Entertainment_img = []
    Entertainment_url = []

    for i in range(len(e_articles)):
        f = e_articles[i]
        Entertainment_title.append(f["title"])
        Entertainment_desc.append(f["description"])
        Entertainment_url.append(f["urlToImage"])
        Entertainment_img.append(f["url"])
    mylist = zip(Entertainment_title, Entertainment_desc, Entertainment_img, Entertainment_url)
    return render(request, "entertainment.html", context={"mylist": mylist})


def Health(request):
    top_health = newsapi.get_top_headlines(category="health")

    h_articles = top_health["articles"]
    health_desc = []
    health_title = []
    health_img = []
    health_url = []

    for i in range(len(h_articles)):
        f = h_articles[i]
        health_title.append(f["title"])
        health_desc.append(f["description"])
        health_url.append(f["urlToImage"])
        health_img.append(f["url"])
    mylist = zip(health_title, health_desc, health_img, health_url)
    return render(request, "health.html", context={"mylist": mylist})


def Science(request):
    top_sci = newsapi.get_top_headlines(category="science")

    s_articles = top_sci["articles"]
    sci_desc = []
    sci_title = []
    sci_img = []
    sci_url = []

    for i in range(len(s_articles)):
        f = s_articles[i]
        sci_title.append(f["title"])
        sci_desc.append(f["description"])
        sci_url.append(f["urlToImage"])
        sci_img.append(f["url"])
    mylist = zip(sci_title, sci_desc, sci_img, sci_url)
    return render(request, "science.html", context={"mylist": mylist})


def Business(request):
    top_bus = newsapi.get_top_headlines(category="business")

    b_articles = top_bus["articles"]
    bus_desc = []
    bus_title = []
    bus_img = []
    bus_url = []

    for i in range(len(b_articles)):
        f = b_articles[i]
        bus_title.append(f["title"])
        bus_desc.append(f["description"])
        bus_url.append(f["urlToImage"])
        bus_img.append(f["url"])
    mylist = zip(bus_title, bus_desc, bus_img, bus_url)
    return render(request, "business.html", context={"mylist": mylist})
