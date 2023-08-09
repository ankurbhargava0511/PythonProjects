'''
import ws_websitehtml

ws_websitehtml.webscrap_website_html()

'''
from bs4 import BeautifulSoup
with open("website.html", errors="ignore") as file:
    contents = file.read()

soup= BeautifulSoup(contents,"html.parser" )
'''

# Basic tages
print (soup.title)
print(soup.title.name)

# GET THE STRING OR TEXT WITHIN tags
print(soup.title.string)
print(soup.prettify())

print(soup.a)
print(soup.p)

'''


# get all the tag of certain type
all_anchor_tags= soup.find_all(name='a')
all_paragraph_tags= soup.find_all(name='p')
#

for tag in all_anchor_tags:
    # Get inner text
    print(tag.getText())
    # Get
    print(tag.get("href"))


#get item by id attributes
heading= soup.find_all(name="h1", id="name")
print(heading)

class_attribute= soup.find(name="h3", class_="heading")

print(class_attribute)
print(class_attribute.name)

company_url= soup.select_one(selector="p a")

print(company_url)


heading= soup.select(".heading")
print(heading)
print(heading[0].text)