import requests
from bs4 import BeautifulSoup
search = input("Plz type weather in and city or state Name: ")
url = f"https://www.google.com/search?&q={search}"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe").text
print("Weather In Your city or State :",update)
