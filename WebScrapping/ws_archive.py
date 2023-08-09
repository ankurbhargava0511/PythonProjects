from bs4 import BeautifulSoup
import requests

URL="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"



response= requests.get(URL)

#print(response.text)

soup= BeautifulSoup(response.text, "html.parser")

#print(soup.prettify())

titles=soup.find_all(name="h3" , class_="title")

movies_titles=[title.getText() for title in titles]


sorted_list=movies_titles[::-1]


with open("movies.txt", mode= "w") as file:
    for i in sorted_list:
        file.write(f"{i}\n" )



