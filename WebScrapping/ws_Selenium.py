from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path=""
driver= webdriver.Chrome(chrome_driver_path)

driver.get=""
article_count= driver.find.element_by_cs_selector("#dkljldjlkd a")
# article_count.click()

all_portals= driver.find_element_by_link_text("All xyz")
# all_portal.click()


search= driver.find_elementby_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)