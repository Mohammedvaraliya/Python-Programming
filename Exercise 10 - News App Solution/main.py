import requests
import json

query = input("What type of news are you interested in? ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=7d3b590442b547308b4c218dc5c7ddcb"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))

for article in news["articles"]:
    print(article["title"])
    print("\t", article["description"])
    print("--------------------------------------------------")