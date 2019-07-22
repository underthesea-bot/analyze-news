import requests
import xmltodict

def normalize(title):
    return title
content = requests.get("https://vnexpress.net/rss/tin-moi-nhat.rss").text
data = xmltodict.parse(content)
items = data['rss']['channel']['item']
titles = [item["title"] for item in items]
titles = [normalize(title) for title in titles]
f = open("titles.txt", "w")
f.write("\n".join(titles))
