import requests
from bs4 import BeautifulSoup

URL = 'https://www.twitter.com/KevalinKetcham'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

tweets = soup.find_all("div")
print(tweets)


# , attrs={"class"="css-1dbjc4n"}