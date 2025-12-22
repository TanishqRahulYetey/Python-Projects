import requests
from bs4 import BeautifulSoup

year = "2018"
url = "https://www.imdb.com/search/title?release_date=" + year + "," + year + "&title_type=feature"

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/120.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.title.text)

i = 1
movie_list = soup.find_all("h3", class_="lister-item-header")
for header in movie_list:
    title = header.find("a").text
    print(f"{i}. Movie: {title}")
    i += 1