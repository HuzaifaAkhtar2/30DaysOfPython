from requests import *
from bs4 import *
from json import *

# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').
url = "http://www.bu.edu/president/boston-university-facts-stats/"
r = get(url)
soup = BeautifulSoup(r.text, "html.parser")

title = soup.find("h1").text
items = [i.text for i in soup.find_all("li")]

data = {
    "title": title,
    "items": items
}

with open("scraped1.json", "w", encoding="utf-8") as f:
    dump(data, f, indent=4)

