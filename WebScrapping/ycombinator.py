from bs4 import BeautifulSoup
import requests



response= requests.get("https://news.ycombinator.com/news")

#print (response.text)

yc_wb_text=BeautifulSoup(response.text, "html.parser")

title_tag= yc_wb_text.find_all(name="span", class_="titleline")
print(title_tag)
for tag in title_tag:
    print(tag.getText())