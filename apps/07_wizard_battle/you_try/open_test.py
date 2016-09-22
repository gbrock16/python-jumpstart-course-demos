import requests
from bs4 import BeautifulSoup


def get_links(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    return {a_tag['href']: a_tag.text for a_tag in soup.find_all('a')}


for link, text in get_links('https://www.yahoo.com/').items():
    print(text.strip(), link)
