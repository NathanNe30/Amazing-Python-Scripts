# import requests module first
from bs4 import BeautifulSoup
from security import safe_requests

url = input("Enter Link: ")  # input link by user

if ("https" or "http") in url:
    data = safe_requests.get(url)
else:
    data = safe_requests.get("https://" + url)

soup = BeautifulSoup(data.text, "html.parser")

links = []

for link in soup.find_all("a"):
    links.append(link.get("href"))

with open("myLinks.txt", 'w') as saved:
    print(links[:20], file=saved)
